"""PROJECT1:- Use Case:Sales Prediction
Create a model which will predict the sales based on campaigning expenses.

Dataset Advertising.csv
The dataset can be downloaded from https://www.kaggle.com/datasets

Perform the following task.
1)Load the data in the DataFrame.
2)Perform Data Preprocessing
3)Handle Categorical Data
4)Perform Exploratory Data Analysis
5)Build the model using Multiple Linear Regression
6)Use the appropriate evaluation metrics"""

# === Step 1: Load Libraries ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# === Step 2: Load the Dataset ===
df = pd.read_csv("Advertising.csv", index_col=0)  # Ensure the dataset is in the same folder or provide full path
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# === Step 3: Data Preprocessing ===
print("\nChecking for missing values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# === Step 4: Handle Categorical Data ===
# No categorical data in this dataset — all numerical.

# === Step 5: Exploratory Data Analysis (EDA) ===
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.pairplot(df)
plt.show()

# === Step 6: Build the Model ===
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Intercept:", model.intercept_)
print("Model Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: {coef:.4f}")

# === Step 7: Make Predictions ===
y_pred = model.predict(X_test)

# === Step 8: Evaluate the Model ===
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation Metrics:")
print(f"  MAE : {mae:.2f}")
print(f"  MSE : {mse:.2f}")
print(f"  RMSE: {rmse:.2f}")
print(f"  R²   : {r2:.2f}")

# === Step 9: Visualize Predictions vs Actual ===
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, edgecolors='k', color='skyblue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.grid(True)
plt.show()


"""PROJECT2:- Use Case: Diabetes Prediction
Consider the PIMA Indians diabetes dataset. Create a Model for diabetes prediction based on the
features mentioned in the dataset.

Dataset: PIMA Indians diabetes dataset.
The dataset can be downloaded from https://www.kaggle.com/datasets

Perform the following tasks.
1)Load the data in the DataFrame.
2)Perform Data Preprocessing
3)Perform Exploratory Data Analysis
4)Build the model using Logistic Regression and K-Nearest Neighbour
5)Use the appropriate evaluation metrics"""

import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score,
    confusion_matrix, classification_report, RocCurveDisplay
)

# ---------------- Config ----------------
CSV_PATH = "DIABETES.csv"
FEATURE_COLS = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin",
                "BMI","DiabetesPedigreeFunction","Age"]
TARGET_COL = "Outcome"
PLOTS_DIR = "plots"
ZERO_AS_MISSING = ["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]
os.makedirs(PLOTS_DIR, exist_ok=True)

# ---------------- Load data ----------------
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Could not find '{CSV_PATH}'. Please put the PIMA csv in this folder with the usual columns.")

df = pd.read_csv(CSV_PATH)
missing_cols = [c for c in ([*FEATURE_COLS, TARGET_COL]) if c not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns in CSV: {missing_cols}")
df = df[[*FEATURE_COLS, TARGET_COL]].copy()
print("Loaded dataset shape:", df.shape)

# --------------- Preprocessing ----------------
df[ZERO_AS_MISSING] = df[ZERO_AS_MISSING].replace(0, np.nan)

print("\nNaN counts after converting zeros to NaN:")
print(df.isna().sum())

X = df[FEATURE_COLS]
y = df[TARGET_COL].astype(int)

numeric_transform = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
preprocess = ColumnTransformer([("num", numeric_transform, FEATURE_COLS)], remainder="drop")

# --------------- EDA (save plots) ----------------
def save_histograms(df, outdir):
    for col in FEATURE_COLS:
        plt.figure()
        vals = df[col].fillna(df[col].median())
        plt.hist(vals, bins=30)
        plt.title(f"Histogram: {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, f"hist_{col}.png"))
        plt.close()

def save_class_balance(y, outdir):
    plt.figure()
    y.value_counts().sort_index().plot(kind="bar")
    plt.title("Class balance (0 = non-diabetic, 1 = diabetic)")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "class_balance.png"))
    plt.close()

def save_correlation_heatmap(df, outdir):
    imp = SimpleImputer(strategy="median")
    X_imp = pd.DataFrame(imp.fit_transform(df[FEATURE_COLS]), columns=FEATURE_COLS)
    corr = X_imp.corr()
    plt.figure(figsize=(8,6))
    plt.imshow(corr, interpolation='nearest', cmap=plt.cm.RdYlBu)
    plt.colorbar()
    plt.title("Feature Correlation (Pearson)")
    plt.xticks(range(len(FEATURE_COLS)), FEATURE_COLS, rotation=45, ha='right')
    plt.yticks(range(len(FEATURE_COLS)), FEATURE_COLS)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "correlation_heatmap.png"))
    plt.close()

print("\nSaving EDA plots to", PLOTS_DIR)
save_histograms(df, PLOTS_DIR)
save_class_balance(y, PLOTS_DIR)
save_correlation_heatmap(df, PLOTS_DIR)
print("EDA saved.")

# --------------- Train-Test split ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42
)
print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

# --------------- Model definitions & GridSearch ----------------
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

log_pipeline = Pipeline([
    ("preprocess", preprocess),
    ("clf", LogisticRegression(max_iter=5000, solver="saga"))
])
log_param_grid = {
    "clf__penalty": ["l1", "l2"],
    "clf__C": [0.01, 0.1, 1, 10],
    "clf__class_weight": [None, "balanced"]
}
log_gs = GridSearchCV(log_pipeline, log_param_grid, cv=cv, scoring="roc_auc", n_jobs=-1)

knn_pipeline = Pipeline([
    ("preprocess", preprocess),
    ("clf", KNeighborsClassifier())
])
knn_param_grid = {
    "clf__n_neighbors": [3,5,7,9],
    "clf__weights": ["uniform", "distance"],
    "clf__p": [1,2]
}
knn_gs = GridSearchCV(knn_pipeline, knn_param_grid, cv=cv, scoring="roc_auc", n_jobs=-1)

print("\nFitting Logistic Regression (GridSearch)...")
log_gs.fit(X_train, y_train)
print("Best LogReg params:", log_gs.best_params_)
print("Best LogReg CV ROC-AUC:", round(log_gs.best_score_,4))

print("\nFitting KNN (GridSearch)...")
knn_gs.fit(X_train, y_train)
print("Best KNN params:", knn_gs.best_params_)
print("Best KNN CV ROC-AUC:", round(knn_gs.best_score_,4))

# --------------- Evaluation ----------------
def eval_and_save(model, X_tr, y_tr, X_te, y_te, name, outdir):
    # predict
    y_tr_pred = model.predict(X_tr)
    y_te_pred = model.predict(X_te)

    if hasattr(model, "predict_proba"):
        y_te_proba = model.predict_proba(X_te)[:,1]
    elif hasattr(model, "decision_function"):
        scores = model.decision_function(X_te)
        smin, smax = scores.min(), scores.max()
        y_te_proba = (scores - smin) / (smax - smin + 1e-12)
    else:
        y_te_proba = y_te_pred.astype(float)

    metrics = {
        "train_accuracy": accuracy_score(y_tr, y_tr_pred),
        "test_accuracy": accuracy_score(y_te, y_te_pred),
        "precision": precision_score(y_te, y_te_pred, zero_division=0),
        "recall": recall_score(y_te, y_te_pred, zero_division=0),
        "f1": f1_score(y_te, y_te_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_te, y_te_proba)
    }

    print(f"\n=== {name} Evaluation ===")
    for k,v in metrics.items():
        print(f"{k:>15}: {v:.4f}")
    print("\nClassification report (test):\n", classification_report(y_te, y_te_pred, digits=4))

    cm = confusion_matrix(y_te, y_te_pred)
    plt.figure()
    plt.imshow(cm, interpolation="nearest")
    plt.title(f"Confusion Matrix — {name}")
    plt.xticks([0,1], ["Pred 0","Pred 1"])
    plt.yticks([0,1], ["True 0","True 1"])
    for (i,j), v in np.ndenumerate(cm):
        plt.text(j, i, str(v), ha='center', va='center')
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"cm_{name.lower().replace(' ', '_')}.png"))
    plt.close()

    plt.figure()
    RocCurveDisplay.from_predictions(y_te, y_te_proba)
    plt.title(f"ROC Curve — {name}")
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"roc_{name.lower().replace(' ', '_')}.png"))
    plt.close()

    return metrics

best_log = log_gs.best_estimator_
best_knn = knn_gs.best_estimator_

log_metrics = eval_and_save(best_log, X_train, y_train, X_test, y_test, "Logistic Regression", PLOTS_DIR)
knn_metrics = eval_and_save(best_knn, X_train, y_train, X_test, y_test, "KNN", PLOTS_DIR)

# --------------- Compare & save summary ----------------
def better_model(m1, m2, key="roc_auc"):
    if m1.get(key,0) >= m2.get(key,0):
        return "Logistic Regression"
    else:
        return "KNN"

winner = better_model(log_metrics, knn_metrics, key="roc_auc")
summary_path = os.path.join(PLOTS_DIR, "model_summary.txt")
with open(summary_path, "w") as f:
    f.write("Pima Diabetes - Model Summary\n")
    f.write("=============================\n\n")
    f.write("Best Logistic Regression params:\n")
    f.write(str(log_gs.best_params_) + "\n\n")
    f.write("Best KNN params:\n")
    f.write(str(knn_gs.best_params_) + "\n\n")
    f.write("Test Metrics (LogReg):\n")
    for k,v in log_metrics.items():
        f.write(f"  {k}: {v:.4f}\n")
    f.write("\nTest Metrics (KNN):\n")
    for k,v in knn_metrics.items():
        f.write(f"  {k}: {v:.4f}\n")
    f.write(f"\nWinner (by ROC-AUC): {winner}\n")

print(f"\nArtifacts saved in folder: ./{PLOTS_DIR}")
print(" - histograms, class balance, correlation heatmap")
print(" - confusion matrices, ROC curves")
print(" - model_summary.txt (with best params & metrics)")

sample = X_test.iloc[:8].copy()
sample["true"] = y_test.iloc[:8].values
sample["pred_logreg"] = best_log.predict(sample[FEATURE_COLS])
sample["pred_knn"] = best_knn.predict(sample[FEATURE_COLS])
print("\nSample predictions (first 8 test rows):")
print(sample.head(8))