import fitz  # PyMuPDF

def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return ""

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
