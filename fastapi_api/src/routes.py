from fastapi import APIRouter, Request, HTTPException
from .processor import SuperheroProcessor, FeatureExtractionError

router = APIRouter()
processor = SuperheroProcessor()

@router.post("/predict")
async def predict_destruction(request: Request):
    try:
        raw_body = await request.body()
        xml_data = raw_body.decode("utf-8")
        
        if not xml_data:
            raise ValueError("Empty request body")

        result = processor.predict(xml_data)
        
        return {
            "status": "success",
            "predicted_annual_destruction_events": result
        }
    except FeatureExtractionError as e:
        # This returns a clean, specific message to the user/client
        raise HTTPException(
            status_code=422, 
            detail={
                "error": "Data Extraction Failed",
                "message": str(e)
            }
        )
    except Exception as e:
        # Fallback for unexpected system errors
        raise HTTPException(status_code=500, detail="An internal server error occurred.")