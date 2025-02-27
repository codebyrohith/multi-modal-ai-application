import cv2
from transformers import pipeline
from PIL import Image

# Load Image Captioning Model (Reusing for video frame analysis)
image_captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Function for Video Analysis
def analyze_video(video_path, frame_interval=30):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    captions = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:  # Process frames at intervals
            frame_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            caption = image_captioner(frame_image)
            captions.append(f"Frame {frame_count}: {caption[0]['generated_text']}")
        
        frame_count += 1
    
    cap.release()
    return captions
