"""
app.py
------
Main Streamlit application for the AI Interview Screening & Feedback
System. Ties together:
  - question_bank.py   (question data)
  - nlp_scorer.py       (NLP / DL semantic similarity)
  - ml_classifier.py    (ML quality classification)
  - llm_feedback.py     (LLM-generated feedback)

Run with:
    streamlit run app.py
"""

import streamlit as st

from question_bank import get_roles, get_questions
from nlp_scorer import score_answer
from ml_classifier import classify_answer
from llm_feedback import generate_feedback

st.set_page_config(page_title="AI Interview Screener", page_icon="🎤", layout="centered")

st.title("🎤 AI-Powered Interview Screening & Feedback")
st.caption("NLP + ML + DL + LLM based mock interview evaluator")

# --- Sidebar: role & question selection ---
st.sidebar.header("Setup")
role = st.sidebar.selectbox("Choose interview track", get_roles())
questions = get_questions(role)
question_labels = [q["question"] for q in questions]
q_index = st.sidebar.selectbox(
    "Choose a question",
    range(len(question_labels)),
    format_func=lambda i: question_labels[i],
)
selected_q = questions[q_index]

st.subheader("Question")
st.write(selected_q["question"])

# --- Candidate answer input ---
answer = st.text_area("Your answer", height=180, placeholder="Type your answer here...")

if st.button("Submit Answer", type="primary"):
    if not answer.strip():
        st.warning("Please type an answer before submitting.")
    else:
        with st.spinner("Scoring your answer..."):
            scores = score_answer(
                answer=answer,
                ideal_answer=selected_q["ideal_answer"],
                keywords=selected_q["keywords"],
            )
            quality = classify_answer(
                similarity_score=scores["similarity_score"],
                keyword_coverage=scores["keyword_coverage"],
                answer_length=scores["answer_length"],
            )
            feedback = generate_feedback(
                question=selected_q["question"],
                ideal_answer=selected_q["ideal_answer"],
                candidate_answer=answer,
                quality=quality,
                similarity_score=scores["similarity_score"],
                keyword_coverage=scores["keyword_coverage"],
            )

        st.divider()
        st.subheader("Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Relevance", f"{scores['similarity_score'] * 100:.0f}%")
        col2.metric("Concept Coverage", f"{scores['keyword_coverage'] * 100:.0f}%")
        col3.metric("Quality", quality)

        st.caption(f"Scoring method used: {scores['method']} | Answer length: {scores['answer_length']} words")

        st.subheader("Feedback")
        st.info(feedback)

        with st.expander("See ideal answer (for reference)"):
            st.write(selected_q["ideal_answer"])

st.divider()
st.caption(
    "Tip: Set the ANTHROPIC_API_KEY environment variable to enable real LLM-generated "
    "feedback. Without it, the app uses rule-based feedback automatically."
)

