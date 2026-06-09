import time_series_visualizer
from unittest import main

print("--- Generating Time Series Visualizations ---")
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()
print("Plots generated: line_plot.png, bar_plot.png, box_plot.png")

print("\n--- Running Test Framework ---")
main(module='test_module', exit=False)