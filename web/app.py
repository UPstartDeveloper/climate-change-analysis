from flask import Flask, render_template
import pandas as pd

# Instaniate global app variable
app = Flask(__name__)

# make a list of DataFrames, for each CSV we use
dfs = [
    pd.read_csv('../Data/carbon-emissions.csv'),  # carbon emissions
]
# attach a DataFrame of emissions data to the app variable
app.emissions_df = dfs[0]
# add a property for the different sources of the emissions
app.carbon_categories = dfs[0]['Description'].unique()
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
    return render_template("index.html"), 200  # template and response code


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


if __name__ == "__main__":
    # Run the app locally 
   app.run(host="0.0.0.0", port=5000, debug=True)
