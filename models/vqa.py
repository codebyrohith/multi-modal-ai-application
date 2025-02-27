import torch
from transformers import pipeline
from PIL import Image

# Ensure device compatibility (CPU/GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Visual Question Answering (VQA) Model
vqa_model = pipeline("visual-question-answering", model="Salesforce/blip-vqa-base", device=0 if device == "cuda" else -1)

# Function for Visual Question Answering (VQA)
def answer_question(image_path, question):
    image = Image.open(image_path).convert("RGB")
    answer = vqa_model(image=image, question=question)

    # Ensure a more descriptive answer
    if isinstance(answer, list) and len(answer) > 0:
        if 'generated_text' in answer[0]:
            return answer[0]['generated_text']
        elif 'answer' in answer[0]:
            return f"Detailed Answer: {answer[0]['answer']}."

    return "No answer generated. Try rephrasing the question."