import pandas as pd
import logging

NARROW_THRESHOLD = 0.5  # 0.5% CPR width

def compute_cpr(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Computing CPR values...")
    df = df.copy()
    df["Pivot"] = (df["High"] + df["Low"] + df["Close"]) / 3
    df["BC"] = (df["High"] + df["Low"]) / 2
    df["TC"] = 2 * df["Pivot"] - df["BC"]
    df["CPR_Width"] = (df["TC"] - df["BC"]).abs()
    df["CPR_Width_pct"] = (df["CPR_Width"] / df["Pivot"]) * 100
    df["CPR_Type"] = df["CPR_Width_pct"].apply(
        lambda x: "Narrow" if x <= NARROW_THRESHOLD else "Wide"
    )
    logging.info("CPR computation complete.")
    return df
