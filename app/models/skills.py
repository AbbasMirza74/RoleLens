import re
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "sqlite",
    "flask",
    "django",
    "fastapi",
    "streamlit",
    "rest api",
    "api",
    "html",
    "css",
    "javascript",
    "react",
    "bootstrap",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "linux",
    "opencv",
    "computer vision",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "pytorch",
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "nlp",
    "llm",
    "gemini",
    "langchain",
    "mongodb",
    "postgresql",
    "oracle",
    "data structures",
    "algorithms",
    "oop",
    "mvc",
    "authentication",
    "session management"
]
ROLE_SKILLS = {

    "Python Developer": [
        "python",
        "flask",
        "sql",
        "git",
        "github",
        "rest api",
        "docker",
        "oop",
        "data structures",
        "algorithms"
    ],

    "Java Developer": [
        "java",
        "sql",
        "git",
        "github",
        "oop",
        "data structures",
        "algorithms",
        "rest api"
    ],

    "Data Science": [
        "python",
        "numpy",
        "pandas",
        "matplotlib",
        "machine learning",
        "scikit-learn",
        "tensorflow",
        "deep learning"
    ],

    "DevOps Engineer": [
        "docker",
        "kubernetes",
        "linux",
        "aws",
        "git",
        "github"
    ],

    "Database": [
        "sql",
        "mysql",
        "sqlite",
        "postgresql",
        "oracle"
    ],

    "Testing": [
        "java",
        "python",
        "selenium",
        "automation",
        "testing"
    ],

    "Web Designing": [
        "html",
        "css",
        "javascript",
        "bootstrap",
        "react"
    ],

    "HR": [
        "communication",
        "leadership",
        "management"
    ]
}


def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found.append(skill.title())
    return sorted(list(set(found)))

def get_missing_skills(role, detected_skills):
    expected = ROLE_SKILLS.get(role, [])
    detected = [skill.lower() for skill in detected_skills]
    missing = []
    for skill in expected:
        if skill.lower() not in detected:
            missing.append(skill.title())
    return missing

def calculate_skill_match(role, detected_skills):
    expected = ROLE_SKILLS.get(role)
    if not expected:
        return 0
    detected = [s.lower() for s in detected_skills]
    matched = 0
    for skill in expected:
        if skill.lower() in detected:
            matched += 1
    return round((matched / len(expected)) * 100)