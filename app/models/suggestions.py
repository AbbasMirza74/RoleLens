def generate_suggestions(
    predicted_role,
    ats_score,
    detected_skills,
    missing_skills,
    resume_text
):
    """
    Generate resume improvement suggestions.
    """
    suggestions = []
    resume_text = resume_text.lower()
    if ats_score < 70:
        suggestions.append(
            "Improve your resume structure and add more role-relevant skills."
        )
    elif ats_score < 85:
        suggestions.append(
            "Your resume is good but can be strengthened with additional technical skills."
        )
    if missing_skills:
        suggestions.append(
            "Consider learning: " +
            ", ".join(missing_skills[:5])
        )

    if "github" not in resume_text:
        suggestions.append(
            "Add your GitHub profile to showcase your projects."
        )
    if "linkedin" not in resume_text:
        suggestions.append(
            "Include your LinkedIn profile for better recruiter visibility."
        )
    project_keywords = [
        "project",
        "developed",
        "implemented",
        "created"
    ]
    if not any(word in resume_text for word in project_keywords):
        suggestions.append(
            "Include at least 2 technical projects with measurable outcomes."
        )
    achievement_keywords = [
        "cgpa",
        "award",
        "certification",
        "hackathon",
        "achievement"
    ]
    if not any(word in resume_text for word in achievement_keywords):
        suggestions.append(
            "Mention certifications, achievements or hackathon participation."
        )
    if "%" not in resume_text and "improved" not in resume_text:
        suggestions.append(
            "Quantify your achievements using numbers wherever possible."
        )
    if len(resume_text.split()) < 180:

        suggestions.append(
            "Expand project descriptions using action verbs and technical details."
        )
    role_tips = {

        "Python Developer":
        "Strengthen your profile with Flask/Django, REST APIs, Docker and deployment projects.",

        "Java Developer":
        "Include Spring Boot, Hibernate, JDBC and backend development experience.",

        "Data Science":
        "Add ML projects, model evaluation metrics and visualization libraries.",

        "DevOps Engineer":
        "Showcase Docker, Kubernetes, CI/CD pipelines and cloud platforms.",

        "Testing":
        "Include Selenium, PyTest, automation frameworks and testing methodologies.",

        "Database":
        "Highlight SQL optimization, indexing and database design experience."
    }

    if predicted_role in role_tips:
        suggestions.append(role_tips[predicted_role])
    unique = []
    for suggestion in suggestions:
        if suggestion not in unique:
            unique.append(suggestion)
    return unique[:8]