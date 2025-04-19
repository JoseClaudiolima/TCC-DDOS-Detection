import pandas as pd
train_data = pd.read_parquet("dataset/training/data_no_inbound.parquet")
X_train = train_data.iloc[:, :-1]  # All columns except the last one
y_train = train_data.iloc[:, -1]   # Last column (label)

print("Colunas usadas para treinamento:")
print(X_train.columns)

print("Coluna do label:")
print(y_train.name)
