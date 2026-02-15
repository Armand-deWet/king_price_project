import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    MEAN_AGE = int(os.getenv("MEAN_AGE", 35))
    MODEL_PATH = os.path.join(BASE_DIR, os.getenv("MODEL_PATH", "superhero_model.joblib"))