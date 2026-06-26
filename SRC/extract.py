import pandas as pd

def extract():
    df = pd.read_csv(
        "../Data/claims.csv",
        sep=",",
        engine="python"
    )

    return df