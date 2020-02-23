# Is Climate Change Real? How Do You Know?

## Overview
This project uses common statistical analysis techniques to explore the relationships between carbon emissions, and the cost and amount of natural disasters globally over time!
The time period observed ranges from 1900 to 2018.

## Links to Datasets (on [Kaggle](https://www.kaggle.com/))
1. [Natural Disasters Dataset](https://www.kaggle.com/dataenergy/natural-disaster-data)
This dataset was posted by Aravind Sivalingam, and is a subset of what's available on [Our World in Data](https://ourworldindata.org/natural-disasters).
It includes the annual counts of reported natural disasters from 1900-2018, as well as their economic costs in USD.
It goes further as well to break down disasters by type of event, such as any of the following:
    - "All natural disasters"
    - "Drought"
    - "Earthquake"
    - "Extreme temperature"
    - "Extreme weather"
    - "Flood"
    - "Impact"
    - "Landslide"
    - "Mass movement (dry)"
    - "Volcanic activity"
    - "Wildfire"
2. [Carbon Emissions Dataset by EIA](https://www.kaggle.com/txtrouble/carbon-emissions)
This dataset was posted by Jason McNeil, and comes from the Energy Information Administration.
It provides records of the carbon dioxide emissions produced by the United States monthly, for every year from January  of 1973 to July of 2016.
Data is broken down by the type of energy produced in the process, as either being:
    - "Coal Electric Power Sector CO2 Emissions"
    - "Total Energy Electric Power Sector CO2 Emissions"


## Analysis Summary
At the end of [the analysis in my Jupyter Notebook](analysis.ipynb), I hope to present the following to you:

1. **Rising Above (and Below) the Mean**:
By the decade, the mean and median count of natural disasters rises throughout the 20th century, and have dropped (so far) during the 21st century.
Reason why? Possibly due to regression to the mean.
2. **Disasters in the 21st Century**:
The population subset of years 2000-2018 make up:
37.5% of those years that have above average number of total natural disasters, compared to the annual mean of the 20th century (1900-2000).
and nearly 43% of all years that have above average number of total natural disasters (1900-2018)
3. **Distribution Across Centuries**:
The relative frequency of natural disasters within the first 18 years of this century, is nearly half to that of the entirety of the previous century.
4. **Skewing Our Data?**:
None of the natural disaster counts in our dataset constitute as outliers, suggesting some correlation is possible between how the counts have changed over time, with other variables.
5. **Correlation to Carbon Emissions**:
According to the data provided by the EIA, over the turn of the century the number of carbon emissions due to electricity generation in the U.S. has decreased.
6. **Correlation to Economic Damages**:
Because the p-value of t-test is less than 0.05, we can accept that as disasters go up, so will their costliness!
Perhaps we would already have expected this?¶

## Presentation Tools
The slideshow included in this repository are available for anyone to use!

Click here for the [slideshow](analysis.slides.html).

Take a closer look at [LICENSE.md](LICENSE.md) for more details.
