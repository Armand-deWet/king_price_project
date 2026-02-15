import pandas as pd
import joblib
from bs4 import BeautifulSoup
from datetime import datetime
from .config import Config

class FeatureExtractionError(Exception):
    """Raised when the XML format is invalid or missing critical fields."""
    pass

class SuperheroProcessor:
    def __init__(self):
        try:
            artifacts = joblib.load(Config.MODEL_PATH)
            self.model = artifacts["model"]
            self.required_features = artifacts["features"]
        except Exception as e:
            raise RuntimeError(f"Could not load model: {str(e)}")

    def extract_features(self, xml_string: str) -> pd.DataFrame:
        if not xml_string or not isinstance(xml_string, str):
            raise FeatureExtractionError("The provided XML string is empty or invalid.")
        
        soup = BeautifulSoup(xml_string, "xml")

        if not soup.find():
            raise FeatureExtractionError("The XML content could not be parsed. Please check the format.")
        
        # Age Logic
        dob_tag = soup.find("DateOfBirth")
        age = Config.MEAN_AGE
        if dob_tag:
            try:
                dob = datetime.strptime(dob_tag.text, '%Y-%m-%d')
                today = datetime(2026, 2, 14)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            except: 
                pass

        try:
            data = {
                "property_count": len(soup.find("PropertiesOwnedBySuperhero").find_all("item")) if soup.find("PropertiesOwnedBySuperhero") else 0,
                "age": age,
                "credit_score": int(soup.find("CreditScore").text) if soup.find("CreditScore") else 600,
                "power_teleportation": 1 if any("teleportation" in item.text for item in soup.find_all("item")) else 0
            }
        except Exception as e:
            # This catches attribute errors if the XML structure is completely unexpected
            raise FeatureExtractionError(f"Critical fields missing or malformed: {str(e)}")

        return pd.DataFrame([data])

    def predict(self, xml_string: str) -> int:
        features_df = self.extract_features(xml_string)
        X = features_df[self.required_features]
        prediction = self.model.predict(X)[0]
        return int(max(0, round(prediction)))