"""Q1) Predict the price of the car based on its features. Use appropriate evaluation metrics.
Dataset : cars.csv"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline

# 1) Load data
df = pd.read_csv("cars.csv")

print("Dataset shape:", df.shape)
print(df.head())

# 2) Data Preprocessing
for col in ["debt", "income"]:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].median())

X = df.drop("sales", axis=1)
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3) Exploratory Data Analysis
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

sns.histplot(df["sales"], kde=True)
plt.title("Car Price Distribution")
plt.show()

# 4) Build models inside Pipelines
models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(),
    "Lasso": Lasso(),
    "Random Forest": RandomForestRegressor(random_state=42)
}

results = {}

for name, model in models.items():
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("model", model)
    ])
    
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results[name] = {"MSE": mse, "MAE": mae, "R2": r2}
    print(f"\n{name} Performance:")
    print(f"  MSE: {mse:.2f}")
    print(f"  MAE: {mae:.2f}")
    print(f"  R2 : {r2:.3f}")

# 5) Compare model performance
results_df = pd.DataFrame(results).T
print("\nModel Comparison:")
print(results_df)

results_df[["MSE", "MAE"]].plot(kind="bar", figsize=(8,5))
plt.title("Model Error Comparison")
plt.ylabel("Error")
plt.show()

results_df["R2"].plot(kind="bar", figsize=(8,5), color="green")
plt.title("R2 Score Comparison")
plt.ylabel("R2 Score")
plt.show()


"""Q2)Create a model that can predict the profit based on its features metrics. Use appropriate
evaluation metrics.The Dataset can be downloaded from kaggle.com  Dataset: 50_startups.csv"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1) Load Data
df = pd.read_csv("50_startups.csv")
print("Shape:", df.shape)
print(df.head())

X = df.drop("Profit", axis=1)
y = df["Profit"]

cat_cols = ["State"]
num_cols = [col for col in X.columns if col not in cat_cols]

# 2) Preprocessing
numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])
categorical_transformer = Pipeline(steps=[
    ("encoder", OneHotEncoder(drop="first"))  
])
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_cols),
        ("cat", categorical_transformer, cat_cols)
    ]
)

# 3) EDA
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.histplot(df["Profit"], kde=True, bins=20)
plt.title("Profit Distribution")
plt.show()

# 4) Models
linreg = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

rf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linreg.fit(X_train, y_train)
y_pred_lr = linreg.predict(X_test)

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 5, 10]
}
grid = GridSearchCV(rf, param_grid, cv=5, scoring="r2", n_jobs=-1)
grid.fit(X_train, y_train)
best_rf = grid.best_estimator_
y_pred_rf = best_rf.predict(X_test)

# 5) Evaluation
def evaluate(y_true, y_pred, name):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"\n{name} Performance:")
    print(f"  MAE : {mae:.2f}")
    print(f"  MSE : {mse:.2f}")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  R²  : {r2:.3f}")
    return {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}

metrics_lr = evaluate(y_test, y_pred_lr, "Linear Regression")
metrics_rf = evaluate(y_test, y_pred_rf, "Random Forest")

results = pd.DataFrame([metrics_lr, metrics_rf],
                       index=["Linear Regression", "Random Forest"])
print("\nModel Comparison:\n", results)

results["R2"].plot(kind="bar", color=["blue", "green"],
                   title="R² Comparison", ylabel="R² Score")
plt.show()


"""Q3)Create a model that can predict the profit based on its features. Use appropriate evaluation
metrics. The Dataset can be downloaded from kaggle.com  Dataset:Salary_Data"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1) Load data
df = pd.read_csv("salary_data.csv")
print("Shape:", df.shape)
print(df.head())

# 2) EDA
plt.scatter(df["YearsExperience"], df["Salary"], color="blue")
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 3) Features and Target
X = df[["YearsExperience"]]   
y = df["Salary"]             
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4) Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 5) Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"  MAE : {mae:.2f}")
print(f"  MSE : {mse:.2f}")
print(f"  RMSE: {rmse:.2f}")
print(f"  R²  : {r2:.3f}")

# 6) Visualize Regression Line
plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted Line")
plt.title("Linear Regression: Salary Prediction")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

# 7) Example Prediction
years = np.array([[7.5]])   
predicted_salary = model.predict(years)
print(f"\nPredicted Salary for {years[0][0]} years of experience = {predicted_salary[0]:.2f}")
