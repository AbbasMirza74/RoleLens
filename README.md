# 🎯 RoleLens - AI Resume Analyzer
RoleLens is a Machine Learning powered web application that analyzes resumes and predicts the most suitable job role using Natural Language Processing (NLP). The application also extracts technical skills, identifies missing skills for the predicted role, estimates an ATS score, and provides resume improvement suggestions.
---
## 🚀 Features
- 📄 Upload Resume (PDF/DOCX)
- 🤖 Predict Job Role using Machine Learning
- 🧹 NLP-based Resume Preprocessing
- 🛠 Detect Technical Skills
- 📌 Identify Missing Skills
- 📊 Estimate ATS Score
- 💡 Generate Resume Improvement Suggestions
- 🌐 Flask Web Interface
---
## 🛠 Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Naive Bayes
- Linear SVM
- Random Forest

### NLP
- NLTK
- Regular Expressions

### Libraries
- Joblib
- Pandas
- pdfplumber
- python-docx


## 📂 Project Structure

```
RoleLens/
│
├── run.py
├── requirements.txt
│
└── app/
    ├── __init__.py
    │
    ├── datasets/
    │
    ├── models/
    │   ├── preprocessing.py
    │   ├── train_model.py
    │   ├── predict.py
    │   ├── skills.py
    │   ├── ats.py
    │   ├── suggestions.py
    │   ├── resume_model.pkl
    │   └── tfidf.pkl
    │
    ├── routes/
    │   └── dashboard.py
    │
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   └── dashboard_result.html
    │
    └── static/
```

---

# ⚙️ Workflow
```
Upload Resume
        │
        ▼
Extract Text
        │
        ▼
NLP Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
ML Model Prediction
        │
        ▼
Skill Detection
        │
        ▼
Missing Skill Detection
        │
        ▼
ATS Score Calculation
        │
        ▼
Resume Suggestions
        │
        ▼
Display Results
```
---

# 🧠 Machine Learning Pipeline
Dataset
↓
Resume Cleaning
↓
Train-Test Split
↓
TF-IDF Vectorization
↓
Train Multiple Models
- Logistic Regression
- Naive Bayes
- Linear SVM
- Random Forest
↓

Evaluate Accuracy
↓
Save Best Model (.pkl)
↓
Load Model for Prediction
---
# 📝 Resume Preprocessing
The uploaded resume undergoes several preprocessing steps before prediction.
- Convert to lowercase
- Remove emails
- Remove URLs
- Remove phone numbers
- Remove special characters
- Remove stopwords
- Lemmatization
- Tokenization
Example
```
Input
Python Flask Developer with SQL knowledge.
↓
Output
python flask developer sql knowledge
```
---
# 📊 Prediction Process
```
Resume
↓
clean_text()
↓
TF-IDF Vectorizer
↓
resume_model.pkl
↓
Predicted Role
↓
Skill Extraction
↓
ATS Score
↓
Suggestions
``
---

# 🎯 Supported Job Categories
- Python Developer
- Java Developer
- Data Science
- Testing
- DevOps
- Database
- Web Designing
- HR

---
# 📈 Output

The application displays
- Predicted Job Role
- Top Matching Roles
- Detected Skills
- Missing Skills
- Estimated ATS Score
- Resume Suggestions
- Model Used
- Processing Time

---
# 📦 Installation

```bash
git clone https://github.com/yourusername/RoleLens.git
cd RoleLens
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

---
# 🎓 Learning Outcomes
- Natural Language Processing
- Text Classification
- Machine Learning Model Training
- TF-IDF Vectorization
- Flask Web Development
- Model Serialization using Joblib
- Resume Analysis
---

---

# 👨‍💻 Author

Mirza Mahazeef Abbas
B.Tech Information Technology
Python | Flask | Machine Learning
