import pandas as pd
import numpy as np


def load_train_data() -> pd.DataFrame:
    with open("data/train.csv", "r+") as f:
        return pd.read_csv(f)

def clean_data(input_df: pd.DataFrame) -> pd.DataFrame:
    clean_df = input_df[['PassengerId', 'Survived', 'Age', 'Pclass', 'SibSp', 'Parch', 'Fare']]
    clean_df.dropna(how="any")
    return clean_df


if __name__ == "__main__":
    data = load_train_data()
    data = clean_data(data)     
    print(data.describe())
