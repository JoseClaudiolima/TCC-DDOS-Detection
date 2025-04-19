# Change completely this file in future, when use real conections

import pandas as pd

def read_data_with_sample_of_conections():
    # Load the data
    df = pd.read_parquet("dataset/all_data_with_15_features_and_label.parquet")

    return df
