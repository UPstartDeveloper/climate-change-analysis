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


# Route to Get the Home Page
@app.route("/", methods=['GET'])
def get_index():
    '''Return the view of the home page.'''
    return render_template("index.html"), 200


# Route to Get Emission Page
@app.route("/emissions", methods=['GET'])
def get_emissions_chart():
    '''Return the view of the emissions chart page.'''
    return render_template("emissions.html"), 200


if __name__ == "__main__":
    # Run the app locally 
   app.run(host="0.0.0.0", port=5000, debug=True)
