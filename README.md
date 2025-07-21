
# 🌿 LeafGuard: AI-Powered Plant Disease Detection

LeafGuard is a machine learning web app that helps farmers and gardeners **detect plant diseases** from images of leaves. It uses a deep learning model (MobileNetV2) trained on plant leaf images to classify diseases and offers **remedies** via Gemini API integration.

---

## 🚀 Features

- 🌱 Upload leaf images
- 🧠 Detect plant diseases using a TensorFlow model
- 💊 Get remedies via Google Gemini API (optional)
- 🖼️ Built with Streamlit — runs in the browser
- 💻 Works locally and in the cloud (e.g. Streamlit Community Cloud)

---

## 📁 Project Structure

```
LeafGuard/
├── app.py                     # Streamlit app
├── leafguard_mobilenetv2.h5      # Trained Keras model
├── class_labels.json          # Class index to name mapping
├── requirements.txt           # Dependencies
├── README.md                  # This file

```

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/kunal22260/LeafGuard.git
cd LeafGuard
```

### 2. Create and Activate Virtual Environment

#### On Windows
```bash
python -m venv venv
.env\Scriptsctivate
```

#### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 Use Python 3.10 and TensorFlow 2.13 for best compatibility.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🧠 How It Works

- Loads a trained MobileNetV2-based model (`.keras`)
- Accepts uploaded images of plant leaves
- Preprocesses to 224x224 + normalization
- Predicts disease class and confidence
- fetches remedies using Gemini API

---

## 🧾 Example `requirements.txt`

```txt
streamlit==1.35.0
tensorflow==2.13.0
numpy
Pillow
requests
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to https://streamlit.io/cloud
3. Link your repo and set `app.py` as the entry point
4. Make sure to include `leafguard_model.keras` and `class_labels.json`

---

## 🛠️ Troubleshooting

- **Model load fails?** → Ensure `.keras` extension and `model.save()` used.
- **TensorFlow install fails?** → Use Python 3.10, not 3.12+.
- **PowerShell activation error (Windows)?**
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- **Streamlit not found?**
  ```bash
  pip install streamlit
  ```

---

## 🙌 Credits

- Model: TensorFlow/Keras + MobileNetV2
- UI: Streamlit
- Remedies: Gemini Pro (Google Generative AI)
- Dataset: [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease)

---


## 📬 Contact

**Your Name**  
📧 kunal90098@gmail.com  
🔗 GitHub: [@kunal22260](https://github.com/kunal22260)
