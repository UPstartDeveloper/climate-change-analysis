import pandas as pd


def clean_emission_data(path):
    def fill_not_available(dataframe, column_name):
        '''Fills in 0 for all values in the column that are populated by "Not Available."'''
        new_values = list()
        for item in dataframe[column_name]:
            # get the value to append
            value = item
            # if value is NaN, change to 0
            if value == "Not Available":
                value = 0
            # add the value
            new_values.append(value)
        # reassign the column in the df
        dataframe[column_name] = new_values
        return dataframe
    """Converts all times in the emissions DataFrame into DateTime values."""
    # make a DF of the emissions CSV, wherever it's located
    carbon_df = pd.read_csv(path)
    # store a list of the different sources
    carbon_categories = carbon_df['Description'].unique()
    # convert dates to strings
    carbon_df['YYYYMM'] = [str(date)[:-2] + "-" + str(date)[-2:] for date in carbon_df['YYYYMM']]
    # remove all dates in the 13th month
    new_df = carbon_df[~carbon_df["YYYYMM"].str.contains('-13')]
    # convert to datetime
    new_df["YYYYMM"] = pd.to_datetime(new_df['YYYYMM'], format="%Y-%m")
    # give each energy source it's own column - now the date is the index
    new_df = new_df.pivot(index='YYYYMM', columns='Description', values='Value')
    # remove NaN values
    for category in carbon_categories:
        new_df = fill_not_available(new_df, category)
    return new_df, carbon_categories
