import streamlit as st
import google.generativeai as genai
from PIL import Image
import random

import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

chat_model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
vision_model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

st.set_page_config(page_title="Maacare Buddy", layout="centered")
st.title("🤱 Neovita")
st.markdown("Your postpartum & baby care AI assistant 💗")

st.subheader("💬 Ask Neovita")
user_prompt = st.text_input("Type your question (e.g. breast pain, baby crying)")

if user_prompt:
    with st.spinner("Neovita is thinking..."):
        response = chat_model.generate_content(user_prompt)
        st.success(response.text)

st.subheader("🖼️ Upload a photo for advice")
img = st.file_uploader("Upload photo (e.g. baby rash, sore area)", type=["jpg", "jpeg", "png"])

if img:
    image = Image.open(img)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing with Gemma..."):
        prompt = (
            "You are an expert in maternal and infant care. "
            "Analyze this photo of a newborn baby. "
            "Please provide:\n"
            "1. A possible diagnosis or observations based on the image.\n"
            "2. Care tips for the mother and baby.\n"
            "3. Clear advice on when to seek medical help.\n"
            "Make sure the response is simple and reassuring."
        )

        img_response = vision_model.generate_content([
            prompt,
            image
        ])
        st.info(img_response.text)


st.subheader("🌸 Daily Mama Tip")
tips = [
    "Stay hydrated & rest when baby rests 💧😴",
    "Keep feeding frequent to avoid engorgement 🍼",
    "Use warm compress for sore breasts 🧖‍♀️",
    "Keep baby’s diaper area clean and dry 👶",
    "Talk to loved ones if feeling low 💕",
    "Trust your instincts—you're doing better than you think 💪",
    "It's okay to ask for help. You're not alone 🤗",
    "Skin-to-skin contact soothes both mama & baby 🤱",
    "Gentle massage can ease colic or gas pains 👣",
    "Don’t ignore your mental health, mama. You matter too 🌸"
]
if st.button("Give me a tip 💌"):
    st.success(random.choice(tips))
