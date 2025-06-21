import streamlit as st
from backend.qa import ask_question
from backend.summarizer import generate_summary
from backend.challenge import generate_questions, evaluate_answer
from backend.utils import extract_text_from_file

# Set page config
st.set_page_config(
    page_title="GenAI Research Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔬"
)

# Custom CSS with research-themed background
custom_css = f"""
<style>
    /* Very subtle research-themed background */
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1532094349884-543bc11b234d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=10");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-color: rgba(255,255,255,0.9);
        background-blend-mode: overlay;
    }}

    /* Main content container */
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.96);
        border-radius: 12px;
        padding: 3rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(0,0,0,0.05);
    }}

    /* Content boxes with strong contrast */
    .summary-box {{
        background: rgba(236, 253, 245, 0.95) !important;
        border-left: 4px solid #10b981 !important;
    }}

    .answer-box {{
        background: rgba(239, 246, 255, 0.95) !important;
        border-left: 4px solid #3b82f6 !important;
    }}

    .challenge-box {{
        background: rgba(255, 251, 235, 0.95) !important;
        border-left: 4px solid #f59e0b !important;
    }}

    /* Ensure text remains dark and readable */
    .summary-box, .answer-box, .challenge-box {{
        color: #1e293b !important;
    }}

    /* Enhanced contrast for headers */
    h1, h2, h3 {{
        color: #1e293b !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.7);
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# App header
st.markdown("""
<div style="text-align:center; margin-bottom:2rem;">
    <h1 style="font-size:2.5rem;">🔬 Research AI Assistant</h1>
    <p style="color:#475569; font-size:1.1rem;">Advanced document analysis for researchers</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - File Upload
with st.sidebar:
    st.header("📂 Document Upload")
    uploaded_file = st.file_uploader(
        "Upload research document",
        type=["pdf", "txt"],
        help="Supports academic papers, technical reports, and research documents"
    )
    st.markdown("---")
    st.caption("🔍 Tip: For best results, use well-structured research documents")

# Main content
if uploaded_file:
    # Process document
    with st.spinner("Analyzing document..."):
        document_text = extract_text_from_file(uploaded_file)
        st.session_state["doc_text"] = document_text

    # Auto Summary
    st.subheader("📋 Research Summary")
    with st.spinner("Generating concise summary..."):
        summary = generate_summary(document_text)
    st.markdown(f"""
    <div class="summary-box" style="padding:1.5rem; border-radius:8px; margin:1rem 0;">
        {summary}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Interaction mode
    tab1, tab2 = st.tabs(["🧐 Ask Research Questions", "🔍 Comprehension Challenge"])

    with tab1:
        question = st.text_input(
            "Enter your research question:",
            placeholder="What methodology did the authors use?"
        )
        if st.button("Get Answer", type="primary"):
            with st.spinner("Searching document..."):
                answer = ask_question(document_text, question)
            st.markdown(f"""
            <div class="answer-box" style="padding:1.5rem; border-radius:8px; margin:1rem 0;">
                <strong>Research Answer:</strong><br><br>
                {answer}
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        if st.button("Generate Challenge Questions"):
            with st.spinner("Creating assessment questions..."):
                questions = generate_questions(document_text)
                st.session_state.questions = questions.split("\n")[:3]  # Limit to 3 questions
        
        if "questions" in st.session_state:
            for i, q in enumerate(st.session_state.questions):
                st.markdown(f"**Question {i+1}:** {q}")
                user_answer = st.text_area(
                    f"Your response to Question {i+1}",
                    key=f"ans_{i}",
                    height=100
                )
                if st.button(f"Evaluate Response {i+1}"):
                    with st.spinner("Assessing answer..."):
                        feedback = evaluate_answer(q, user_answer, document_text)
                    st.markdown(f"""
                    <div class="challenge-box" style="padding:1.5rem; border-radius:8px; margin:1rem 0;">
                        <strong>Expert Feedback:</strong><br><br>
                        {feedback}
                    </div>
                    """, unsafe_allow_html=True)