import pandas as pd


def clean_emission_data(path):
    def fill_not_available(df, column_name):
        '''Fills in 0 for all values in the column that are populated by "Not Available."'''
        new_values = list()
        for item in df[column_name]:
            # get the value to append
            value = item
            # if value is NaN, change to 0
            if value == "Not Available":
                value = 0
            # add the value
            new_values.append(value)
        # reassign the column in the df
        df[column_name] = new_values
        return df
    def convert_dates(df, date_column):
        '''Converts the date column to datetime values. Will NOT remove NaN.'''
        df[date_column] = [str(date)[:-2] + "-" + str(date)[-2:] for date in df[date_column]]
        # remove all dates in the 13th month
        df = df[~df[date_column].str.contains('-13')]
        # convert to datetime
        df[date_column] = pd.to_datetime(df[date_column], format="%Y-%m")
        return df
    """Converts all times in the emissions DataFrame into DateTime values."""
    # A: make a DF of the emissions CSV, wherever it's located
    carbon_df = pd.read_csv(path)
    # B: store a list of the different sources
    carbon_categories = carbon_df['Description'].unique()
    # C: convert dates to strings
    carbon_df = convert_dates(carbon_df, 'YYYYMM')
    # D: give each energy source it's own column - now the date is the index
    carbon_df = carbon_df.pivot(index='YYYYMM', columns='Description', values='Value')
    # E: remove NaN values
    for category in carbon_categories:
        carbon_df = fill_not_available(carbon_df, category)
    # F: set a new index, so that the dates can have their own column
    dates = carbon_df.index
    carbon_df.index = list(range(len(dates)))
    carbon_df['YYYYMM'] = dates
    return carbon_df, carbon_categories
