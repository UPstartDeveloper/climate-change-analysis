import pandas as pd


def clean_emission_data(path):
    """Converts all times in the emissions DataFrame into DateTime values."""
    # make a DF of the emissions CSV, wherever it's located
    carbon_df = pd.read_csv(path)
    # convert dates to strings
    carbon_df['YYYYMM'] = [str(date)[:-2] + "-" + str(date)[-2:] for date in carbon_df['YYYYMM']]
    # remove all dates in the 13th month
    new_df = carbon_df[~carbon_df["YYYYMM"].str.contains('-13')]
    # convert to datetime
    new_df["YYYYMM"] = pd.to_datetime(new_df['YYYYMM'], format="%Y-%m")
    # give each energy source it's own column
    new_df = new_df.pivot(index='YYYYMM', columns='Description', values='Value')
    # TODO: remove NaN values
    # store a list of the different sources
    carbon_categories = dfs[0]['Description'].unique()
    return new_df, carbon_categories
