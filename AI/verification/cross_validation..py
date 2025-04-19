from sklearn.model_selection import cross_val_score
import pandas as pd
import joblib

train_data = pd.read_parquet("dataset/training/data_no_inbound.parquet")
X_train = train_data.iloc[:, :-1]  # All columns except the last one
y_train = train_data.iloc[:, -1]   # Last column (label)

model_loaded = joblib.load("AI/v3/random_forest_model.pkl")

scores = cross_val_score(model_loaded, X_train, y_train, cv=5)  # 5-fold CV
print(f"Pontuações da Cross-validation: {scores}")
print(f"Média de Acurácia: {scores.mean():.2f}")
