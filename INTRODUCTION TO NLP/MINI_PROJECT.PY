"""Use Case: Rating Prediction
Create a model that will predict the rating based on the feedback of the customer.

Feature: Text
Label: Stars
Dataset: yelp.csv
The dataset can be downloaded from https://www.kaggle.com/datasets"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix
)

# 1) Load dataset
df = pd.read_csv("yelp.csv")

print("Shape:", df.shape)
print(df.head())

X = df['text']
y = df['stars']

# 2) Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3) Text Vectorization (TF-IDF)
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# 4) Train Models
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train_tfidf, y_train)
y_pred_lr = log_reg.predict(X_test_tfidf)

nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)
y_pred_nb = nb.predict(X_test_tfidf)

rf = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
rf.fit(X_train_tfidf, y_train)
y_pred_rf = rf.predict(X_test_tfidf)

# 5) Evaluation Function
def evaluate_model(y_true, y_pred, model_name):
    acc = accuracy_score(y_true, y_pred)
    print(f"\n--- {model_name} ---")
    print(f"Accuracy: {acc:.3f}")
    print("Classification Report:\n", classification_report(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"{model_name} - Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

evaluate_model(y_test, y_pred_lr, "Logistic Regression")
evaluate_model(y_test, y_pred_nb, "Naive Bayes")
evaluate_model(y_test, y_pred_rf, "Random Forest")

# 6) Feature Importance (for Logistic Regression)
feature_names = np.array(tfidf.get_feature_names_out())
coefs = log_reg.coef_[0]
top_words = feature_names[np.argsort(coefs)[-20:]]
print("\nTop Positive Words (LR):", top_words)
