import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Historical Data')

    # 3. Create first line of best fit (entire dataset: 1880 to 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate an extended series of years up to 2050
    years_all = pd.Series([i for i in range(1880, 2051)])
    sea_levels_all = res_all.slope * years_all + res_all.intercept
    plt.plot(years_all, sea_levels_all, color='red', label='Fit: 1880-2050')

    # 4. Create second line of best fit (recent data: 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate an extended series of years from 2000 to 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    sea_levels_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, sea_levels_recent, color='green', label='Fit: 2000-2050')

    # 5. Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # 6. Save image and return current axes (don't modify)
    plt.savefig('sea_level_plot.png')
    return plt.gca()