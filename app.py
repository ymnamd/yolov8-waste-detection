# app.py (run this command in terminal to install dependencies first: pip install -r requirements.txt)

import gradio as gr
from ultralytics import YOLO
import numpy as np
from PIL import Image

# Load trained model
model = YOLO("best.pt")

def detect(image, conf_thresh):
    # Ensure input is a valid image
    if isinstance(image, Image.Image):
        image = np.array(image)

    # Run inference with specified confidence threshold
    results = model(image, conf=conf_thresh)

    # Draw bounding boxes on the image
    result_image = results[0].plot()
    return Image.fromarray(result_image)

# Gradio UI with confidence threshold slider
gr.Interface(
    fn=detect,
    inputs=[
        gr.Image(type="pil", label="Upload an image or use webcam"),
        gr.Slider(0, 1, value=0.5, step=0.05, label="Confidence Threshold")
    ],
    outputs=gr.Image(type="pil", label="Detected Objects"),
    title="YOLOv8 Waste Detection Dashboard",
    description="Upload an image or use webcam to detect waste objects (e.g., paper, plastic, glass). Adjust the confidence threshold below to filter predictions."
).launch()