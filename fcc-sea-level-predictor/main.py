import sea_level_predictor
from unittest import main

print("--- Generating Sea Level Trend Models ---")
sea_level_predictor.draw_plot()
print("Prediction plot saved successfully as 'sea_level_plot.png'!")

print("\n--- Running Automated Validation ---")
main(module='test_module', exit=False)