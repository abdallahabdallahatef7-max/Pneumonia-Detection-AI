from fastapi import File, UploadFile, APIRouter
import cv2
import numpy as np
from src.components.model_prediction import prediction

routes = APIRouter()
predictor = prediction()

@routes.post("/upload/image")
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Predict
    result, probability = predictor.predict_from_array(img)
    
    return {
            "filename": image.filename,
            "width": img.shape[1],
            "height": img.shape[0],
            "channels": img.shape[2],
            "prediction": result,
            "probability": f"{probability:.4f}"
        }