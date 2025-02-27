import streamlit as st
from models.image_captioning import generate_image_caption
from models.video_analysis import analyze_video
from models.vqa import answer_question
from PIL import Image
import os

st.title("Multi-Modal AI Application 🚀")

# Image Captioning
st.header("📸 Image Captioning")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_image:
    img_path = f"static/{uploaded_image.name}"
    with open(img_path, "wb") as f:
        f.write(uploaded_image.getbuffer())

    st.image(img_path, caption="Uploaded Image", use_column_width=True)
    caption = generate_image_caption(img_path)
    st.write(f"**Generated Caption:** {caption}")

# Video Analysis
st.header("🎥 Video Analysis")
uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
if uploaded_video:
    video_path = f"static/{uploaded_video.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())

    st.video(video_path)
    captions = analyze_video(video_path)
    st.write("**Generated Captions for Key Frames:**")
    for cap in captions:
        st.write(cap)

# Visual Question Answering
st.header("🧠 Visual Question Answering")
uploaded_vqa_image = st.file_uploader("Upload an image for VQA", type=["jpg", "png", "jpeg"], key="vqa")
question = st.text_input("Enter a question about the image")
if uploaded_vqa_image and question:
    vqa_img_path = f"static/{uploaded_vqa_image.name}"
    with open(vqa_img_path, "wb") as f:
        f.write(uploaded_vqa_image.getbuffer())

    st.image(vqa_img_path, caption="Uploaded Image for VQA", use_column_width=True)
    answer = answer_question(vqa_img_path, question)
    st.write(f"**Answer:** {answer}")

