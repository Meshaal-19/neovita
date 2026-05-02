# Neovita — AI Maternal & Infant Care Assistant

A Streamlit-based AI assistant that provides postpartum and infant care guidance using natural language interaction and image-based analysis.

---

## Overview

Neovita is a multimodal AI application designed to support new mothers with accessible, reassuring, and actionable care guidance.

The system allows users to:
- Ask questions about postpartum or baby care
- Upload images (e.g., baby rash) for AI-based observations
- Receive structured, easy-to-understand advice

---

## Key Features

- Natural language Q&A for maternal and infant care  
- Image-based analysis using AI vision models  
- Structured and reassuring response generation  
- Daily care tips for postpartum well-being  
- Simple and accessible UI built with Streamlit  

---

## Tech Stack

- Python  
- Streamlit  
- Google Gemini API (LLM + Vision)  
- Pillow (image processing)  

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set API key:
```bash
export GOOGLE_API_KEY=your_api_key
```
3. Run the app:
```bash
streamlit run app.py
```

## Project Focus

This project demonstrates:

Multimodal AI (text + image) integration
Prompt design for sensitive domains (healthcare)
Building user-facing AI applications
Designing safe, non-alarming responses
