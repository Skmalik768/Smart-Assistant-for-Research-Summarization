from backend.hf_client import chat_with_mistral

def generate_questions(document_text):
    prompt = f"""
From the following document, generate **exactly 3** logic-based or comprehension-focused questions. 
Only return the questions numbered 1, 2, and 3. Do not include explanations or any extra text.

Document:
{document_text[:4000]}
"""
    return chat_with_mistral(prompt)

def evaluate_answer(question, user_answer, document_text):
    prompt = f"""
Evaluate the user's answer based only on the document below. 
Give a **short verdict (correct/incorrect)** and a **1–2 sentence explanation** referencing the document. 
Do not return the full document again.

Question: {question}
User's Answer: {user_answer}

Document:
{document_text[:4000]}
"""
    return chat_with_mistral(prompt)
