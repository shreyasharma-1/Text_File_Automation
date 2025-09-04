"""Q4) Create a model that can predict the disease of cancer based on features given in the
 dataset. Use appropriate evaluation metrics. Dataset:cancer.csv"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix, classification_report
)
import seaborn as sns

# 1) Load dataset
df = pd.read_csv("cancer.csv")
print("Shape:", df.shape)
print(df.head())

# 2) Preprocessing
if df["diagnosis"].dtype == "object":
    le = LabelEncoder()
    df["diagnosis"] = le.fit_transform(df["diagnosis"])  

if "id" in df.columns:
    df = df.drop("id", axis=1)

X = df.drop("diagnosis", axis=1)
y = df["diagnosis"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3) EDA (optional, quick insight)
plt.figure(figsize=(6,5))
sns.countplot(x=y)
plt.title("Class Distribution (0=Benign, 1=Malignant)")
plt.show()

# 4) Train Models
logreg = LogisticRegression(max_iter=1000, random_state=42)
logreg.fit(X_train, y_train)
y_pred_lr = logreg.predict(X_test)
y_prob_lr = logreg.predict_proba(X_test)[:,1]

rf = RandomForestClassifier(random_state=42)
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 5, 10]
}
grid = GridSearchCV(rf, param_grid, cv=5, scoring="accuracy")
grid.fit(X_train, y_train)
best_rf = grid.best_estimator_
y_pred_rf = best_rf.predict(X_test)
y_prob_rf = best_rf.predict_proba(X_test)[:,1]

# 5) Evaluation function
def evaluate(y_true, y_pred, y_prob, name):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_prob)
    print(f"\n{name} Performance:")
    print(f"  Accuracy : {acc:.3f}")
    print(f"  Precision: {prec:.3f}")
    print(f"  Recall   : {rec:.3f}")
    print(f"  F1 Score : {f1:.3f}")
    print(f"  ROC-AUC  : {auc:.3f}")
    print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("\nClassification Report:\n", classification_report(y_true, y_pred))
    return {"Accuracy": acc, "Precision": prec, "Recall": rec, "F1": f1, "AUC": auc}

metrics_lr = evaluate(y_test, y_pred_lr, y_prob_lr, "Logistic Regression")
metrics_rf = evaluate(y_test, y_pred_rf, y_prob_rf, "Random Forest")

# 6) Compare Models
results = pd.DataFrame([metrics_lr, metrics_rf], index=["Logistic Regression", "Random Forest"])
print("\nModel Comparison:\n", results)

results[["Accuracy","F1","AUC"]].plot(kind="bar", figsize=(8,5))
plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.show()


"""Q5)Create a model that can predict that the customer has purchased item or not based on
features given in the dataset. Use appropriate evaluation metrics. 
Dataset: Social_Ntetwork_Ads.csv"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report, roc_curve
)

# 1) Load dataset
df = pd.read_csv("social_network_ads.csv")
print("Shape:", df.shape)
print(df.head())

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# 2) Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3) Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4) Train Models
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)
y_pred_lr = log_reg.predict(X_test)
y_prob_lr = log_reg.predict_proba(X_test)[:,1]

rf = RandomForestClassifier(random_state=42, n_estimators=200, max_depth=5)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_prob_rf = rf.predict_proba(X_test)[:,1]

svm = SVC(probability=True, random_state=42)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
y_prob_svm = svm.predict_proba(X_test)[:,1]

# 5) Evaluation Function
def evaluate(y_true, y_pred, y_prob, name):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_prob)
    print(f"\n{name} Performance:")
    print(f"  Accuracy : {acc:.3f}")
    print(f"  Precision: {prec:.3f}")
    print(f"  Recall   : {rec:.3f}")
    print(f"  F1 Score : {f1:.3f}")
    print(f"  ROC-AUC  : {auc:.3f}")
    print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("\nClassification Report:\n", classification_report(y_true, y_pred))
    return {"Accuracy": acc, "Precision": prec, "Recall": rec, "F1": f1, "AUC": auc}

metrics_lr = evaluate(y_test, y_pred_lr, y_prob_lr, "Logistic Regression")
metrics_rf = evaluate(y_test, y_pred_rf, y_prob_rf, "Random Forest")
metrics_svm = evaluate(y_test, y_pred_svm, y_prob_svm, "SVM")

# 6) Model Comparison
results = pd.DataFrame([metrics_lr, metrics_rf, metrics_svm],
                       index=["Logistic Regression", "Random Forest", "SVM"])
print("\nModel Comparison:\n", results)

results[["Accuracy", "F1", "AUC"]].plot(kind="bar", figsize=(8,5))
plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.show()

# 7) ROC Curve
plt.figure(figsize=(6,5))
for model_name, y_prob in [("LR", y_prob_lr), ("RF", y_prob_rf), ("SVM", y_prob_svm)]:
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f"{model_name}")
plt.plot([0,1],[0,1],"k--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate (Recall)")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()
