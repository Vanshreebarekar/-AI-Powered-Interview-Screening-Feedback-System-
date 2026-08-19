# 🎤 AI-Powered Interview Screening & Feedback System

> An end-to-end NLP, ML, and LLM-powered mock interview evaluation platform built with Streamlit.

 
 <img width="1907" height="887" alt="Screenshot 2026-08-19 183946" src="https://github.com/user-attachments/assets/62e42f8e-a13d-4c81-8aea-7b23b701c70f" />

---



## 📌 Project Overview

Preparing for technical interviews requires both strong conceptual depth and concise communication. **AI Interview Screener** acts as an automated technical interviewer that evaluates candidate responses in real time. 

The system leverages a multi-layer evaluation pipeline:
1. **NLP / Semantic Similarity**: Measures alignment between the candidate's answer and benchmark ideal answers.
2. **Concept Coverage Analysis**: Evaluates technical keywords and terminology presence.
3. **ML Quality Classifier**: Categorizes the overall response tier using pre-trained machine learning models.
4. **LLM-Powered Feedback Engine**: Delivers actionable insights and structured recommendations for continuous improvement.

---

## 🚀 Key Features

* **Multi-Domain Technical Tracks**:
  * 📊 **Data Science** (Bias-Variance tradeoff, Overfitting, EDA, Handling missing data)
  * 🧠 **Machine Learning & Deep Learning** (Activation functions, CNNs, Vanishing gradients, Regularization)
  * 💬 **NLP & Generative AI** (Transformers, Self-attention, RAG, Word embeddings)
  * 👁️ **Computer Vision & IoT** (Edge AI, Data augmentation, IoT protocols, Convolutions)
  * 🐍 **Python & Backend Development** (Decorators, GIL, Memory management, APIs)
  * 🗄️ **SQL & Database Engineering** (Indexing, Normalization, Joins, Relational vs NoSQL)
* **Real-Time Evaluation Metrics**: Instant scoring across **Relevance %**, **Concept Coverage %**, and **Quality Category**.
* **Intelligent Feedback**: Hybrid evaluation powered by LLM integration with an automated rule-based fallback.
* **Interactive Web Interface**: Clean, lightweight, and responsive dashboard built using Streamlit.

---

## 🏗️ Architecture & Pipeline

```text
       Candidate Answer Input
                 │
                 ▼
       ┌───────────────────┐
       │   Preprocessing   │
       └─────────┬─────────┘
                 │
   ┌─────────────┴─────────────┐
   ▼                           ▼
┌──────────────────┐   ┌──────────────────┐
│   NLP Scorer     │   │ Keyword Coverage │
│ (Semantic Sim.)  │   │     Analysis     │
└─────────┬────────┘   └─────────┬────────┘
          │                      │
          └──────────┬───────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │   ML Quality Classifier   │
       │     (quality_model)       │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │    LLM Feedback Engine    │
       │    (Anthropic / Rules)    │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │  Streamlit Results View   │
       └───────────────────────────┘
