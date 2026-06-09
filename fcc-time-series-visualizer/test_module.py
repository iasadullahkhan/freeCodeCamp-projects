import unittest
import time_series_visualizer
import matplotlib as mpl

class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.line_fig = time_series_visualizer.draw_line_plot()
        self.bar_fig = time_series_visualizer.draw_bar_plot()
        self.box_fig = time_series_visualizer.draw_box_plot()

    def test_line_plot_properties(self):
        ax = self.line_fig.axes[0]
        self.assertEqual(ax.get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel(), "Page Views")

    def test_bar_plot_properties(self):
        ax = self.bar_fig.axes[0]
        self.assertEqual(ax.get_xlabel(), "Years")
        self.assertEqual(ax.get_ylabel(), "Average Page Views")

    def test_box_plot_properties(self):
        ax1 = self.box_fig.axes[0]
        ax2 = self.box_fig.axes[1]
        self.assertEqual(ax1.get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(ax2.get_title(), "Month-wise Box Plot (Seasonality)")

if __name__ == "__main__":
    unittest.main()