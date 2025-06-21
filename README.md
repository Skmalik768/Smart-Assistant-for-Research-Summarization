# 📄 GenAI Smart Document Assistant

This project is a GenAI-powered assistant that reads, understands, and reasons through long-form PDF or TXT documents. It automatically summarizes research papers, technical manuals, and reports, answers user questions with document-based justifications, and challenges users with logical questions — all through a clean, interactive Streamlit web interface.

---

## 🚀 Features

- 📂 Upload PDF or TXT
- 📌 Auto-summary (150 words or less)
- 💬 Ask questions about the document
- 🧠 Challenge mode (3 logic questions)
- ✅ Every answer comes with justification
- 🌐 Runs in the browser with Streamlit

---

## 🧠 Technologies Used

- Streamlit
- Hugging Face Transformers (Mistral + LED)
- Python
- PyMuPDF
- dotenv

---

## ⚙️ Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/your-username/Smart-PDF-Summarizer.git
cd Smart-PDF-Summarizer
```

### 2. Create Virtual Environment (your env is named `genai_envi`)

```bash
python -m venv genai_envi
```

### 3. Activate Environment

- **Windows:**
```bash
genai_envi\Scripts\activate
```

### 4. Install All Required Libraries

```bash
pip install -r requirements.txt
```

### 5. Add Hugging Face API Token

Create a file called `.env` and add your token like this:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Get your token from: https://huggingface.co/settings/tokens

---

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📸 Screenshots

_(Optional – you can add screenshots later here)_

---

## 📜 License

This project is licensed under the MIT License.
