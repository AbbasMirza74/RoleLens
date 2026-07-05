import joblib
import pandas as pd
from app.models.preprocessing import clean_text
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
df = pd.read_csv("app/datasets/job_data.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["Resume"] = df["Resume"].apply(clean_text)
X = df["Resume"]
y = df["Category"]
print(df["Category"].value_counts())
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42,stratify=y)
vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Linear SVM": LinearSVC(),
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
}
best_model = None
best_accuracy = 0
print("=" * 70)
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )
    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )
    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )
    print(f"\n{name}")
    print("-" * 50)
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
print("\n" + "=" * 70)
print(f"Best Model : {best_model.__class__.__name__}")
print(f"Accuracy   : {best_accuracy:.4f}")
print("=" * 70)
joblib.dump(best_model, "app/models/resume_model.pkl")
joblib.dump(vectorizer, "app/models/tfidf.pkl")
print("\nModel Saved Successfully")