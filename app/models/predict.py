import time
import joblib
import pdfplumber
from docx import Document
from app.models.preprocessing import clean_text
from app.models.skills import (
    extract_skills,
    get_missing_skills,
    calculate_skill_match
)
from app.models.ats import (
    calculate_ats_score,
    get_ats_feedback
)
from app.models.suggestions import (
    generate_suggestions
)
model = joblib.load("app/models/resume_model.pkl")
vectorizer = joblib.load("app/models/tfidf.pkl")

def extract_pdf_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

def extract_docx_text(file):
    document = Document(file)
    text = ""
    for para in document.paragraphs:
        text += para.text + " "
    return text

def predict_resume(uploaded_file):
    start_time = time.time()
    filename = uploaded_file.filename.lower()
    if filename.endswith(".pdf"):
        resume_text = extract_pdf_text(uploaded_file)
    elif filename.endswith(".docx"):
        resume_text = extract_docx_text(uploaded_file)
    else:
        return {
            "success": False,
            "message": "Only PDF and DOCX files are supported."
        }
    cleaned_text = clean_text(resume_text)
    vector = vectorizer.transform([cleaned_text])
    prediction = model.predict(vector)[0]
    top_predictions = []
    confidence = None
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(vector)[0]
        confidence = round(max(probabilities) * 100, 2)
        ranking = sorted(
            zip(model.classes_, probabilities),
            key=lambda x: x[1],
            reverse=True
        )
        top_predictions = [
            {
                "role": role,
                "score": round(score * 100, 2)
            }
            for role, score in ranking[:5]
        ]
    else:
        top_predictions.append(
            {
                "role": prediction,
                "score": None
            }
        )
    detected_skills = extract_skills(cleaned_text)
    missing_skills = get_missing_skills(
        prediction,
        detected_skills
    )

    ats_score = calculate_ats_score(
        resume_text,
        detected_skills,
        missing_skills
    )

    ats_feedback = get_ats_feedback(
        ats_score
    )
    suggestions = generate_suggestions(
        prediction,
        ats_score,
        detected_skills,
        missing_skills,
        resume_text
    )
    processing_time = round(
        time.time() - start_time,
        2
    )
    return {
        "success": True,
        "prediction": prediction,
        "confidence": confidence,
        "top_predictions": top_predictions,
        "skills": detected_skills,
        "missing_skills": missing_skills,
        "ats_score": ats_score,
        "ats_feedback": ats_feedback,
        "suggestions": suggestions,
        "processing_time": processing_time,
        "model": type(model).__name__
    }