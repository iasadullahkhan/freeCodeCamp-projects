import medical_data_visualizer
from unittest import main

print("--- Generating Visual Analytics Plots ---")
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()
print("Plots saved successfully as 'catplot.png' and 'heatmap.png'!")

print("\n--- Running Automated Tests ---")
main(module='test_module', exit=False)