from transformers import pipeline
from PIL import Image

# Load Image Captioning Model
image_captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Function for Image Captioning
def generate_image_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    caption = image_captioner(image)
    return caption[0]['generated_text']
