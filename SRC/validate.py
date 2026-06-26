import pandas as pd


def validate(df):

    report = {}

    report["Total Records"] = len(df)

    report["Null Values"] = df.isnull().sum().to_dict()

    report["Duplicate Rows"] = df.duplicated().sum()

    dates = pd.to_datetime(df["claim_date"], errors="coerce")
    report["Invalid Dates"] = dates.isnull().sum()

    amounts = pd.to_numeric(df["claim_amount"], errors="coerce")
    report["Negative Claim Amounts"] = (amounts < 0).sum()

    # Data Quality Score
    issues = (
        report["Duplicate Rows"]
        + report["Invalid Dates"]
        + report["Negative Claim Amounts"]
        + sum(report["Null Values"].values())
    )

    total_possible = len(df) * len(df.columns)

    score = round((1 - issues / total_possible) * 100, 2)

    report["DQ Score"] = score

    if score >= 95:
        report["Status"] = "PASS"
    else:
        report["Status"] = "FAIL"

    return report