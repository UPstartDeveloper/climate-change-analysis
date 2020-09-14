import pandas as pd


def convert_emission_times(path):
    """Converts all times in the emissions DataFrame into DateTime values."""
    # make a DF of the emissions CSV, wherever it's located
    carbon_df = pd.read_csv(path)
    # convert to strings
    carbon_df['YYYYMM'] = [str(date)[:-2] + "-" + str(date)[-2:] for date in carbon_df['YYYYMM']]
    # remove all dates in the 13th month
    new_df = carbon_df[~carbon_df["YYYYMM"].str.contains('-13')]
    new_df["YYYYMM"] = pd.to_datetime(new_df['YYYYMM'], format="%Y-%m")
    # convert to datetime
    return new_df
