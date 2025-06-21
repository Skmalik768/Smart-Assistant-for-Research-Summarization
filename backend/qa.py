from backend.hf_client import chat_with_mistral

def ask_question(document_text, user_question):
    if not document_text.strip():
        return "⚠️ Document content is empty."
    if not user_question.strip():
        return "⚠️ Please enter a valid question."

    prompt = f"""
You are a helpful assistant. Based on the document below, answer the user's question using only the content inside. 
Keep your answer short (2–5 lines), and justify it with reference to the document content (e.g., 'This is found in section 2').
Avoid restating the entire document.

Document:
{document_text[:4000]}

Question: {user_question}
Answer:"""
    return chat_with_mistral(prompt)
