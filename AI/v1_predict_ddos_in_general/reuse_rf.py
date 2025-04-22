import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

# ============================
# 1. Carrega os componentes
# ============================
model = joblib.load("AI/v2_predict_ddos_in_general/modelo_ddos_binary.pkl")
le = joblib.load("AI/v2_predict_ddos_in_general/label_encoder_binary.pkl")
scaler = joblib.load("AI/v2_predict_ddos_in_general/scaler_binary.pkl")

# ============================
# 2. Carrega os novos dados COM LABEL ORIGINAL
# ============================
df = pd.read_parquet("dataset/test.parquet")
# df = pd.read_parquet("dataset/all_data_with_all_benign_no_duplicates_shuffled.parquet")
# df = pd.read_parquet("dataset/03.11_UDP_test.parquet")

# Agrupa todas as conexões que não são BENIGN como DDOS
def simplify_label(label):
    return 'BENIGN' if label.upper() == 'BENIGN' else 'DDOS'

df['Label'] = df['Label'].apply(simplify_label)

# Separa os dados e os rótulos verdadeiros
X = df.drop(columns=['Label'])
y_true = df['Label']

# ============================
# 3. Pré-processamento
# ============================
X_scaled = scaler.transform(X)
y_true_encoded = le.transform(y_true)

# ============================
# 4. Fazendo as previsões
# ============================
y_pred_encoded = model.predict(X_scaled)
y_pred_legivel = le.inverse_transform(y_pred_encoded)

# ============================
# 5. Avaliação do modelo
# ============================
print("======= MATRIZ DE CONFUSÃO =======")
print(confusion_matrix(y_true_encoded, y_pred_encoded))

# ============================
# 6. Relatório de Classificação com Percentual
# ============================
report = classification_report(y_true_encoded, y_pred_encoded, target_names=le.classes_, output_dict=True)

print("\n======= RELATÓRIO DE CLASSIFICAÇÃO =======")
for class_name, metrics in report.items():
    if class_name != 'accuracy':
        print(f"\n{class_name}:")
        for metric, value in metrics.items():
            if isinstance(value, float):
                print(f"  {metric.capitalize()}: {value * 100:.6f}%")

# ============================
# 7. Exemplo de saída
# ============================
print("\nExemplos de previsões:")
print(y_pred_legivel[:10])
