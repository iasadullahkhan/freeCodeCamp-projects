import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Import the data and set the index to the date column
df = pd.read_csv(
    "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/main/fcc-forum-pageviews.csv",
    parse_dates=['date'],
    index_col='date'
)

# 2. Clean data by filtering out top 2.5% and bottom 2.5% of page views
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# 3. Draw Line Plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='firebrick', linewidth=1)
    
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't modify)
    fig.savefig('line_plot.png')
    return fig

# 4. Draw Bar Plot
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')

    # Group data by year and month, calculating the average
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Reorder columns to ensure chronological month sequence
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_pivot = df_pivot.reindex(columns=months_order)

    # Draw plot
    fig = df_pivot.plot(kind='bar', figsize=(10, 8)).get_figure()
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=months_order)

    # Save image and return fig (don't modify)
    fig.savefig('bar_plot.png')
    return fig

# 5. Draw Box Plot
def draw_box_plot():
    # Prepare data for box plots (this part is usually given in the boilerplate)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Set up the matplotlib figure with 2 subplots side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot (Seasonality)
    months_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=months_short, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't modify)
    fig.savefig('box_plot.png')
    return fig