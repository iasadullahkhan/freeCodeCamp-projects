import demographic_data_analyzer
from unittest import main

print("--- Data Analysis Results ---")
demographic_data_analyzer.calculate_demo_data()

print("\n--- Running Automated Tests ---")
main(module='test_module', exit=False)