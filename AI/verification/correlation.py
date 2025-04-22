
from sklearn.preprocessing import LabelEncoder
import pandas as pd

train_data = pd.read_parquet("dataset/train.parquet")
X_train = train_data.iloc[:, :-1]  # All columns except the last one
y_train = train_data.iloc[:, -1]   # Last column (label)

# Converte o label em números
encoder = LabelEncoder()
y_train_numeric = encoder.fit_transform(y_train)

# Calcula a correlação
correlation = X_train.corrwith(pd.Series(y_train_numeric))
print(correlation)
