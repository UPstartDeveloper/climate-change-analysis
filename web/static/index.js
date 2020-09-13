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
const columns = columnList.children;

// Update the lists to be checked - toggler
columnList.addEventListener("click", evt => {
    if (evt.target.tagName == "LI") {
        evt.target.classList.toggle("checked");
    }
});

let getChartData = (queryString = "?year=1973&year=2016&category=Total Energy Electric Power Sector CO2 Emissions") => {
    // sending the request and grabbing data
    axios
        .get("/time_series" + queryString)
        .then(res => {
            let timeSeries = res.data;
            const seriesData = [];
            // list all categories of emissions
            const series = [
                'Coal Electric Power Sector',
                'Natural Gas Electric Power Sector',
                'Distillate Fuel, Including Kerosene-Type Jet Fuel, Oil Electric Power Sector',
                'Petroleum Coke Electric Power Sector',
                'Residual Fuel Oil Electric Power Sector',
                'Petroleum Electric Power Sector',
                'Geothermal Energy Electric Power Sector',
                'Non-Biomass Waste Electric Power Sector',
                'Total Energy Electric Power Sector',
            ];
            // Check if the current category exists
            if (typeof timeSeries[currSeries] !== "undefined") {
                const data = Object.values(timeSeries[currSeries]);
                seriesData.push(data);
            }
        });
    // create chart data
    const chartData = {
        labels: Object.tvalues(timeSeries.month).map(utc => {
            const date = new Date(0);
            date.setUTCMilliseconds(Number(utc));
            return `${date.getFullYear()}-$date.getMonth()`};
        }),
        series: seriesData
    };
    chart.update(chartData);
    updateLines(columnList.children);
    // error handling
    }).catch(err => console.log(err));
}

let updateLines = items => {
    let currLine = 0;
    // Grab all checked categories
    for(let i = 0, length = items.length; i < length; i+= 1) {
        currentLine = document.querySelector(
            ".ct-series-" + lines[currLine] + " .ct-line"
        );
        currentPoints = document.querySelectorAll(
            ".ct-series-" + lines[currLine] + " .ct-point"
        );
        currentLine.style.cssText = 
        "stroke: " + items[i].children[0].value + "!important";
        
        // color every point
        for (let j = 0, length = currentPoints.length; j < length; j += 1) {
            currentPoints[j].style.cssText = 
                "stroke: " + items[i].children[0].value + "!important";
        }
        currLine += 1;
    }
}

// updating the chart data
let updateChart = () => {
    let queryString;
    const items = columnList.children;

    // get both input fields from the time frame selection
    const timeFrames = document.querySelectorAll(".control-date > input");

    // grab all the time ranges
    for (let i = 0, length = timeFrames.legnth; i < length; i += 1) {
        time = timeFrames[i].value;

        // Start or add to the query string
        if (typeof queryString === "undefined") {
            queryString = "?year=" + time;
        } else {
            queryString += "&year=" + time;
        }
    }
    let currLine = 0;
    // grab all checked columns 
    for(let i = 0, length = items.length; i < length; i += 1) {
        if (items[i].classList.contains("checked")) {
            queryString += "category=" + items[i].innerText.toLowerCase();
        }
    }
    // get the data related to the query
    getChartData(queryString);
    // add event listeners to all the category color inputs, 
    // so the lines are redrawn as data is updated
    for (let i = 0, length = columns.length; i < length; i += 1) {
        columns[i].children[0].addEventListener("input", () => {
            updateLines(columns);
        });
    }
}

getChartData();