# Sea Level Predictor

A predictive analytics project that analyzes historical global sea level measurements and forecasts future sea level rise through the year 2050. The project applies linear regression techniques to identify long-term environmental trends and visualize potential future scenarios.

This project was completed as part of the freeCodeCamp Data Analysis with Python Certification.

## Project Objectives

* Analyze historical sea level data
* Visualize long-term environmental trends
* Apply linear regression models
* Generate future sea level predictions
* Compare historical and modern growth rates

## Forecasting Approach

### Model 1: Historical Trend

Uses all available records from 1880 onward to estimate long-term sea level growth.

### Model 2: Modern Trend

Uses data from the year 2000 onward to estimate recent acceleration in sea level rise.

Both models project sea level estimates through 2050.

## Generated Visualization

### Sea Level Prediction Plot

`sea_level_plot.png`

Includes:

* Historical sea level observations
* Long-term regression line
* Modern-trend regression line
* Forecasted values through 2050

## Project Structure

```
├── sea_level_predictor.py
├── main.py
├── test_module.py
├── epa-sea-level.csv
└── sea_level_plot.png
```

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* SciPy

## Installation

```bash
pip install pandas matplotlib scipy
```

## Usage

```bash
python main.py
```

## Skills Demonstrated

* Predictive analytics
* Linear regression
* Data visualization
* Environmental data analysis
* Statistical modeling

## Learning Outcomes

This project strengthened my understanding of regression analysis, forecasting techniques, and data-driven decision-making while working with real-world climate datasets.
