import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# ============================
# 1. Load the dataset
# ============================
train_df = pd.read_parquet("dataset/train.parquet")
test_df = pd.read_parquet("dataset/test.parquet")

# ============================
# 2. Map all attack types to 'DDOS'
# ============================
def simplify_label(label):
    return 'BENIGN' if label.upper() == 'BENIGN' else 'DDOS'

train_df['Label'] = train_df['Label'].apply(simplify_label)
test_df['Label'] = test_df['Label'].apply(simplify_label)

# ============================
# 3. Split features and labels
# ============================
X_train = train_df.drop(columns=['Label'])
y_train = train_df['Label']

X_test = test_df.drop(columns=['Label'])
y_test = test_df['Label']

# ============================
# 4. Preprocessing
# ============================
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================
# 5. Train the model
# ============================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train_encoded)

# ============================
# 6. Evaluation
# ============================
y_pred = model.predict(X_test_scaled)

print("======= CONFUSION MATRIX =======")
print(confusion_matrix(y_test_encoded, y_pred))
print("\n======= CLASSIFICATION REPORT =======")
print(classification_report(y_test_encoded, y_pred, target_names=le.classes_))

# ============================
# 7. Save the model and encoders
# ============================
joblib.dump(model, "modelo_ddos_binary.pkl")
joblib.dump(le, "label_encoder_binary.pkl")
joblib.dump(scaler, "scaler_binary.pkl")

print("\nBinary model (BENIGN vs DDOS) saved successfully!")
