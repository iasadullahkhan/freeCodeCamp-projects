# Mean-Variance-Standard Deviation Calculator

A Python-based statistical analysis tool that utilizes NumPy to compute key descriptive statistics from a 3×3 matrix. The application calculates measures of central tendency, dispersion, and aggregation across rows, columns, and the entire dataset.

This project was developed as part of the freeCodeCamp Data Analysis with Python Certification.

## Features

* Calculates the mean of each row, column, and the entire matrix
* Computes variance and standard deviation
* Determines maximum and minimum values
* Calculates row-wise, column-wise, and overall sums
* Converts NumPy data types into native Python objects for clean output formatting
* Validates input size to ensure a 3×3 matrix can be formed

## Project Structure

```
├── mean_var_std.py      # Core statistical calculation logic
├── main.py              # Test runner and demonstration script
├── test_module.py       # Automated unit tests
```

## Technologies Used

* Python 3
* NumPy

## Installation

```bash
pip install numpy
```

## Usage

Run the application:

```bash
python main.py
```

Example output format:

```python
{
  'mean': [[...], [...], ...],
  'variance': [[...], [...], ...],
  'standard deviation': [[...], [...], ...],
  'max': [[...], [...], ...],
  'min': [[...], [...], ...],
  'sum': [[...], [...], ...]
}
```

## Learning Outcomes

* NumPy array manipulation
* Statistical analysis using Python
* Data aggregation techniques
* Unit testing fundamentals
