import mean_var_std
from unittest import main

# Test your function visually in the console
print("--- Visual Test Result ---")
try:
    print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
except ValueError as e:
    print(e)

print("\n--- Running Automated Unit Tests ---")
# This runs the automated tests from test_module.py automatically
main(module='test_module', exit=False)