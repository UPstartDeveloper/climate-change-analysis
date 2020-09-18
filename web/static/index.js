// Creating a chart
const chart = new Chartist.Line('.ct-chart', {});

const lines = [  // each is for a different energy source
    'srcOne',
    'srcTwo',
    'srcThree',
    'srcFour',
    'srcFive',
    'srcSix',
    'srcSeven',
    'srcEight',
    'srcNine'
];

// Grab all the categories
const categoryList = document.querySelector('.control-category ul');
const columns = categoryList.children;

for (let i = 0, length = columns.length; i < length; i += 1) {
    columns[i].children[0].addEventListener("input", function () {
        updateLines(columns);
    });
}

// Update the lists to be checked - toggler
categoryList.addEventListener("click", evt => {
    if (evt.target.tagName == "LI") {
        evt.target.classList.toggle("checked");
    }
});

function getChartData(queryString = "?years=1973&years=2016&sources=Total Energy Electric Power Sector CO2 Emissions") {
    // sending the request and grabbing data
    axios
        .get("/time_series" + queryString)
        .then(res => {
            let timeSeries = res.data;
            // list all categories of emissions
            const series = [
                'Coal Electric Power Sector CO2 Emissions',
                'Natural Gas Electric Power Sector CO2 Emissions',
                'Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector CO2 Emissions',
                'Petroleum Coke Electric Power Sector CO2 Emissions',
                'Residual Fuel Oil Electric Power Sector CO2 Emissions',
                'Petroleum Electric Power Sector CO2 Emissions',
                'Geothermal Energy Electric Power Sector CO2 Emissions',
                'Non-Biomass Waste Electric Power Sector CO2 Emissions',
                'Total Energy Electric Power Sector CO2 Emissions',
            ];
            const seriesData = [];
            for (let i = 0, length = series.length; i < length; i += 1) {
                const currentSeries = series[i];

                // Ensure that the current series is within the time series.
                if (typeof timeSeries[currentSeries] !== "undefined") {
                    const data = Object.values(timeSeries[currentSeries]);
                    seriesData.push(data);
                }
            }
            console.log(timeSeries);
            const chartData = {
                labels: Object.values(timeSeries[0]).map(datetime => {
                    const date = new Date(datetime);
                    return `${date.getFullYear()}-${date.getMonth()}`;
                }),
                series: seriesData
            };

            // Update the chart and line colors.
            chart.update(chartData);
            updateLines(categoryList.children);
        })
        .catch(err => console.error(err));
}

// updating the chart data
function updateChart() {
    let queryString;

    // Get both input fields from the time frame section
    const timeFrames = document.querySelectorAll(".control-date > input");

    // Grab all time ranges
    for (let i = 0, length = timeFrames.length; i < length; i += 1) {
        time = timeFrames[i].value;

        // Start or add to the query string
        if (typeof queryString === "undefined") {
            queryString = "?years=" + time;
        } else {
            queryString += "&years=" + time;
        }
    }

    // Grab all the checked columns
    for (let i = 0, length = sources.length; i < length; i += 1) {
        if (sources[i].classList.contains("checked")) {
            queryString += "&sources=" + sources[i].innerText.toLowerCase();
        }
    }

    getChartData(queryString);
}

// Update the lines drawn with the correct colors
function updateLines(items) {
    let lineNumber = 0;
    // Grab all the checked columns
    for (let i = 0, length = items.length; i < length; i += 1) {
        // Only color the checked off lines
        if (items[i].classList.contains("checked")) {
            currentLine =
                document.querySelector(`.ct-series-${lines[lineNumber]} .ct-line`);
            currentPoints =
                document.querySelectorAll(`.ct-series-${lines[lineNumber]} .ct-point`);
            currentLine.style.cssText =
                `stroke: ${items[i].children[0].value} !important;`;

            // Color every point
            for (let j = 0, length = currentPoints.length; j < length; j += 1) {
                currentPoints[j].style.cssText =
                    `stroke: ${items[i].children[0].value} !important;`;
            }
            lineNumber += 1;
        }
    }
}
console.log('calling getChart')
getChartData();