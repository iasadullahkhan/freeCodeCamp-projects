# Page View Time Series Visualizer

A time-series analysis project that examines historical page view data from the freeCodeCamp forum. The project focuses on identifying long-term growth patterns, seasonal fluctuations, and yearly traffic trends through data visualization techniques.

This project was completed as part of the freeCodeCamp Data Analysis with Python Certification.

## Project Objectives

* Clean noisy traffic data
* Remove statistical outliers
* Analyze long-term trends
* Investigate seasonal behavior
* Visualize data using multiple chart types

## Data Cleaning

To improve accuracy, page view values outside the:

* Bottom 2.5%
* Top 2.5%

were removed from the dataset before analysis.

## Generated Visualizations

### Line Chart

`line_plot.png`

Displays daily page views over time, highlighting overall growth and traffic trends.

### Bar Chart

`bar_plot.png`

Shows average monthly page views grouped by year, making it easier to compare annual performance.

### Box Plots

`box_plot.png`

Includes:

* Trend Analysis (Year-wise distribution)
* Seasonality Analysis (Month-wise distribution)

These plots help identify data spread, outliers, and recurring seasonal patterns.

## Project Structure

```
├── time_series_visualizer.py
├── main.py
├── test_module.py
├── fcc-forum-pageviews.csv
├── line_plot.png
├── bar_plot.png
└── box_plot.png
```

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* Seaborn

## Installation

```bash
pip install pandas matplotlib seaborn
```

## Usage

```bash
python main.py
```

## Skills Demonstrated

* Time-series analysis
* Data visualization
* Data cleaning
* Statistical interpretation
* Trend analysis
* Seasonality detection
