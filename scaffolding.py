import pandas as pd
import os
from typing import Dict


def load_data(file_path) -> pd.DataFrame:
    with open(file_path, 'r') as f:
        df = pd.read_csv('path/Users/dawitdagnaw/Documents/2025/project1/stock_daily_returns.csv')
    return df


def explore(df: pd.DataFrame):
    """
    Optional
    """
    pass


def trade(df: pd.DataFrame) -> pd.DataFrame:
    """
    Args:
        df: a pd.DataFrame with columns "Date" and stocks "A" through "J".

    Returns:
        A pd.DataFrame with additional columns "Signal_A" through "Signal_J",
        which contain -1 (sell), 0 (hold), or 1 (buy).
    """
    # TODO: implement trading strategy
    for stock in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        df[f"Signal_{stock}"] = 0  # Default to hold

    return df


def backtest(df: pd.DataFrame) -> Dict[str, float]:
    """
    Args:
        df: a pd.DataFrame with columns "Signal_A" through "Signal_J".

    Returns:
        A Dict[str, float] with keys:
        - "Annualized Average Return"
        - "Standard Deviation of Returns"
        - "Annualized Sharpe Ratio"
        - "Maximum Drawdown"
        - "Annualized Sortino Ratio"
    """
    for stock in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        assert f"Signal_{stock}" in df.columns, f"Strategy function must return a DataFrame with 'Signal_{stock}' column."
        assert df[f"Signal_{stock}"].isin([-1, 0, 1]).all(), f"Signal_{stock} column must only contain -1, 0, or 1."

    # TODO: Implement backtesting logic
    performance_metrics = {}
    return performance_metrics


def main():
    file_path = 'stock_daily_returns.csv'
    # Load data
    df = load_data(file_path)

    # TODO: Explore data
    explore(df)

    # TODO: Define trading strategy
    df = trade(df)

    # TODO: Backtest strategy
    metrics = backtest(df)


if __name__ == '__main__':
    main()
