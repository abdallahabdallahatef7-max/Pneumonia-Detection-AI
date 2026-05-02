# 🏥 Pneumonia Detection AI - Production Grade Service

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

An advanced, production-ready medical diagnostic service that leverages Deep Learning to detect Pneumonia from Chest X-Ray images. This system combines a powerful **CNN (Convolutional Neural Network)** with a modern, high-performance **FastAPI** backend and a sleek **Glassmorphic** web interface.

---

## ✨ Key Features

- 🧠 **High-Accuracy CNN:** Custom-built model with multiple convolutional layers for robust feature extraction.
- ⚡ **High Performance:** Built on FastAPI, delivering ultra-fast asynchronous inference.
- 🎨 **Premium UI:** Modern, responsive web interface featuring:
    - Drag-and-drop file uploads.
    - Real-time result visualization with probability bars.
    - Glassmorphism design language.
    - Smooth micro-animations.
- 📦 **Containerized:** Ready for instant deployment using Docker.
- 🛡️ **Scalable Architecture:** Modular project structure following industry best practices.

---

## 📂 Project Architecture

```bash
project_nti/
├── src/
│   ├── components/
│   │   ├── data_transformation.py # Image preprocessing & Normalization
│   │   ├── model_prediction.py    # Core Prediction Engine
│   │   └── structure_model.py     # CNN Model Architecture (Keras)
│   └── controller/
│       └── image_controller.py    # API Endpoint Management
├── static/
│   ├── script.js                  # Dynamic UI Interactions
│   └── style.css                  # Modern Glassmorphic Styling
├── templates/
│   └── index.html                 # Main Web Interface
├── notebooks/
│   └── model.keras                # Pre-trained Weights (Keras v3)
├── main.py                        # Application Entry Point
├── Dockerfile                     # Deployment Container
└── requirements.txt               # Dependency Management
```

---

## 🚀 Getting Started

### 1. Environment Setup
Clone the repository and create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Installation
Install the required production dependencies:
```bash
pip install -r requirements.txt
```

### 3. Launching the Application
Start the uvicorn server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Visit `http://localhost:8000` in your browser.

---

## 🐳 Docker Deployment

To run the application in a completely isolated environment:

```bash
# Build the image
docker build -t pneumonia-detection-ai .

# Run the container
docker run -p 8000:8000 pneumonia-detection-ai
```

---

## 🛠️ Tech Stack

- **Core:** Python 3.12
- **Deep Learning:** TensorFlow 2.18, Keras 3
- **Image Processing:** OpenCV
- **Backend:** FastAPI, Uvicorn, Jinja2
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript (ES6+)

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Developed with ❤️ for Medical AI Research
</p>
