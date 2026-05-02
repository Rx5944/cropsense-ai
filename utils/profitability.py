import pandas as pd

def load_prices():
    return pd.read_csv("data/prices.csv")

def get_profitability(top_df):
    prices = load_prices()

    merged = top_df.merge(prices, on="crop", how="left")
    merged["price"] = merged["price"].fillna(2000)

    merged["profit_score"] = (
        merged["probability"] * merged["price"]
    )

    return merged.sort_values(
        by="profit_score",
        ascending=False
    )