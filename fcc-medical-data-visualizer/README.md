# Medical Data Visualizer

A healthcare-focused data visualization project that examines relationships between cardiovascular disease and various health indicators. Using Pandas, NumPy, Matplotlib, and Seaborn, the project transforms raw medical data into meaningful visual insights.

This project was completed as part of the freeCodeCamp Data Analysis with Python Certification.

## Project Objectives

* Perform feature engineering using BMI calculations
* Normalize medical indicator variables
* Clean inaccurate and extreme observations
* Visualize health trends through statistical charts
* Explore correlations between medical attributes

## Data Processing

### Feature Engineering

Created an `overweight` column based on Body Mass Index (BMI):

```
BMI = Weight (kg) / Height² (m²)
```

### Data Normalization

The following columns were transformed into binary values:

* Cholesterol
* Glucose

Values indicate:

* 0 = Normal
* 1 = Above Normal

### Data Cleaning

Removed:

* Records where diastolic pressure exceeded systolic pressure
* Extreme height outliers
* Extreme weight outliers

## Generated Visualizations

### Categorical Plot

`catplot.png`

Visualizes distributions of:

* Active lifestyle
* Smoking habits
* Alcohol consumption
* Cholesterol levels
* Glucose levels
* Overweight status

Grouped by cardiovascular disease diagnosis.

### Correlation Heatmap

`heatmap.png`

Displays relationships among medical variables using a correlation matrix.

## Project Structure

```
├── medical_data_visualizer.py
├── main.py
├── test_module.py
├── medical_examination.csv
├── catplot.png
└── heatmap.png
```

## Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Installation

```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

```bash
python main.py
```

## Skills Demonstrated

* Data cleaning
* Feature engineering
* Exploratory data analysis
* Data visualization
* Correlation analysis
* Medical dataset interpretation
