import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import json
import google.generativeai as genai
import os

# --- Configuration ---
st.set_page_config(page_title="LeafGuard - Plant Disease Detector", layout="centered")
st.title("🌿 LeafGuard")
st.subheader("Detect plant diseases from leaf images using AI")

# --- Load Model and Labels ---
model = tf.keras.models.load_model("leafguard_model.keras")

with open("class_labels.json", "r") as f:
    class_labels = json.load(f)  # str keys

# --- Set up Gemini ---
genai.configure(api_key="AIzaSyCv9seHM3bt14bjmcyS5M0UZEJ93wNueG8")
gemini_model = genai.GenerativeModel('gemini-2.5-flash')

# --- Upload Image ---
uploaded_file = st.file_uploader("Upload a clear image of the leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="📷 Uploaded Leaf Image", use_column_width=True)

    # --- Preprocess ---
    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    # --- Predict ---
    predictions = model.predict(img_array)
    confidence = float(np.max(predictions))
    class_index = int(np.argmax(predictions))
    predicted_class = class_labels[str(class_index)]

    st.markdown(f"### 🧠 Prediction: `{predicted_class}`")
    st.markdown(f"### ✅ Confidence: `{confidence * 100:.2f}%`")

    # --- Gemini Treatment Suggestion ---
    with st.spinner("💊 Getting treatment suggestions from Gemini..."):
        disease_name = predicted_class.replace("___", " ").replace("_", " ")
        prompt = f"What is a simple treatment plan for {disease_name} in crops?"
        response = gemini_model.generate_content(prompt)
        remedy = response.text.strip()

    st.markdown("### 💡 Suggested Treatment (Gemini):")
    st.write(remedy)
