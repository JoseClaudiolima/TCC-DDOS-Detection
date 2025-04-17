# Change completely this file in future, when use real conections

import pandas as pd

def read_data_with_sample_of_conections():
    # Carregar o parquet
    df = pd.read_parquet("dataset/data_with_500k_samples.parquet") # There are 3 samples in /dataset

    return df
