from backend.hf_client import summarize_with_led

def generate_summary(text):
    safe_text = text[:4000].strip()
    if not safe_text:
        return "⚠️ No content to summarize."

    # No instruction needed — LED is trained for summarization
    return summarize_with_led(safe_text)
