import re
def calculate_ats_score(text, detected_skills, missing_skills):
    score = 100
    text = text.lower()
    if not re.search(r'\S+@\S+\.\S+', text):
        score -= 10
    if not re.search(r'\+?\d[\d\s\-]{8,}\d', text):
        score -= 5
    if "github" not in text:
        score -= 5
    if "linkedin" not in text:
        score -= 5
    education_keywords = [
        "b.tech",
        "btech",
        "bachelor",
        "degree",
        "cgpa",
        "university",
        "college",
        "education"
    ]
    if not any(word in text for word in education_keywords):
        score -= 10
    project_keywords = [
        "project",
        "developed",
        "implemented",
        "designed",
        "created"
    ]
    if not any(word in text for word in project_keywords):
        score -= 10
    if len(detected_skills) < 5:
        score -= 20
    elif len(detected_skills) < 8:
        score -= 10
    score -= min(len(missing_skills) * 3, 20)
    words = text.split()
    if len(words) < 200:
        score -= 10
    elif len(words) > 900:
        score -= 5
    score = max(0, min(score, 100))
    return score

def get_ats_feedback(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    elif score >= 60:
        return "Average"
    return "Needs Improvement"