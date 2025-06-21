# backend/hf_client.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

# Model URLs
MISTRAL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
SUMMARY_MODEL_URL = "https://api-inference.huggingface.co/models/pszemraj/led-large-book-summary"

def call_huggingface_model(prompt: str, model_url: str, max_tokens: int = 300) -> str:
    try:
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_tokens,
                "temperature": 0.5
            },
            "options": {"wait_for_model": True}
        }
        response = requests.post(model_url, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()

        # 1. If response is a list
        if isinstance(result, list) and result:
            # Try generated_text
            if "generated_text" in result[0]:
                return result[0]["generated_text"].strip()
            # Try summary_text
            if "summary_text" in result[0]:
                return result[0]["summary_text"].strip()

        # 2. If response is a dict (some models return dict directly)
        if isinstance(result, dict):
            if "generated_text" in result:
                return result["generated_text"].strip()
            if "summary_text" in result:
                return result["summary_text"].strip()

        return "⚠️ The model didn't return a valid summary. Try reducing the input size."

    except requests.exceptions.RequestException as e:
        return f"❗ HuggingFace API error: {str(e)}"


# 🔹 Mistral for Q&A and Challenge
def chat_with_mistral(prompt: str) -> str:
    return call_huggingface_model(prompt, MISTRAL_URL, max_tokens=300)

# 🔹 LED for Summarization
def summarize_with_led(prompt: str) -> str:
    return call_huggingface_model(prompt, SUMMARY_MODEL_URL, max_tokens=300)
