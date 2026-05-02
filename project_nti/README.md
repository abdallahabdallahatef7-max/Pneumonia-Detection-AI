# Pneumonia Detection AI

A production-ready deep learning service that detects Pneumonia from Chest X-Ray images. This project provides a powerful, modern Web UI powered by FastAPI and a Keras/TensorFlow model.

## Features
- **Deep Learning Model:** A Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify Chest X-Ray images.
- **FastAPI Backend:** Fast, asynchronous backend to handle image uploads and model inference.
- **Modern Web UI:** A premium, responsive front-end interface featuring drag-and-drop uploads, sleek animations, and dynamic probability bars.
- **Docker Support:** Fully containerized application for easy deployment across environments.

## Project Structure
```
project_nti/
├── src/
│   ├── components/
│   │   ├── data_transformation.py # Image preprocessing logic
│   │   ├── model_prediction.py    # Inference logic
│   │   └── structure_model.py     # CNN Architecture definition
│   └── controller/
│       └── image_controller.py    # FastAPI routes for image upload
├── notebooks/
│   └── model.keras                # Trained Keras model
├── static/
│   ├── script.js                  # Frontend JS logic
│   └── style.css                  # Frontend styling (Glassmorphism)
├── templates/
│   └── index.html                 # Frontend HTML view
├── main.py                        # FastAPI entry point
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration
└── README.md
```

## Running Locally

### 1. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Open your browser and navigate to `http://localhost:8000` to interact with the UI.

## Running with Docker

### 1. Build the Docker Image
```bash
docker build -t pneumonia-detection-ai .
```

### 2. Run the Docker Container
```bash
docker run -p 8000:8000 pneumonia-detection-ai
```
Open your browser and navigate to `http://localhost:8000` to interact with the UI.

## Technologies Used
- **Backend:** Python, FastAPI, Uvicorn
- **Machine Learning:** TensorFlow, Keras, OpenCV, Numpy
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Deployment:** Docker
