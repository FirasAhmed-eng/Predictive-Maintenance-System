import pandas as pd


def create_rolling_features(new_column_name, df: pd.DataFrame, column, window=60):
    """
        Creates a rolling feature for a sensor grouped by machine.

        Parameters:
        -----------
        df : DataFrame
        column : str
        new_column : str
        window : int
    """
    df = df.sort_values(["machine_id", "timestamp"])
    df[new_column_name] = (df.groupby("machine_id")[column].transform(  # This will group by machine_id to calculate rolling mean for each machine
        lambda x: x.rolling(window=window, min_periods=1).mean()))
    return df
