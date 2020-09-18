import datetime
from functools import reduce

from flask import Flask, render_template, request
import pandas as pd

import web.util as util

# Instaniate global app variable
app = Flask(__name__)

# make a list of DataFrames, for each CSV we use
climate_change_data = [
    # using convert_emission_times(), the dates will already by converted
    util.clean_emission_data('../Data/carbon-emissions.csv'),  # carbon emissions
]
# attach properties for DataFrame of emissions and energy sources to app
app.emissions_df, app.carbon_categories  = climate_change_data[0]
# add a propert for different colors, each for an emission category
app.colors = [
    '#F00064',  # hot pink
    '#4BBCFE',  # light blue
    '#F06400',  # orange
    '#FF8DEF',  # pink
    '#50296A',  # purple
    '#810D0D',  # brown
    '#545273',  # dark indigo
    '#D8AA61',  # light brown
    '#FFFDC7',  # yellow
]


# Route to Get the Home Page
@app.route("/", methods=['GET'])
def get_index():
    '''Return the view of the home page.'''
    return render_template("index.html"), 200  # template and response


# Route to Get Emission Page
@app.route("/emissions", methods=['GET'])
def get_emissions_chart():
    '''Return the view of the emissions chart page.'''
    return (
        render_template(
        "emissions.html",  # template name
        categories=app.carbon_categories,
        # colors=app.colors,  # context of template
        ), 200  # response code
    )


@app.route("/time_series", methods=["GET"])
def get_time_series_data():
    '''Return the necessary data to create a time series'''
    # Grab the requested years and sources from the query arguments
    # default ranges and sources
    range_of_years = [int(year) for year in request.args.getlist("years")]
    sources = request.args.getlist("sources")

    # Generate a list of all the months we need to get
    min_year = min(range_of_years)
    max_year = max(range_of_years)

    # Grab all of the data specified from start to stop range.
    selected_date_range = app.emissions_df[
        (app.emissions_df.index >= datetime.datetime(min_year, 1, 1)) &
        (app.emissions_df.index <= datetime.datetime(max_year, 12, 31))
    ]

    # Slice the DF to include only the sources we want 
    requested_trend_data = selected_date_range[sources]
    # sort our dataframe by those sources.
    # requested_trend_data = requested_trend_data.sort_values(by=["month"])

    # Return the dataframe as json
    print(f"JSON: {requested_trend_data}")
    return requested_trend_data.to_json(), 200


if __name__ == "__main__":
    # Run the app locally 
   app.run(host="0.0.0.0", port=5000, debug=True)
