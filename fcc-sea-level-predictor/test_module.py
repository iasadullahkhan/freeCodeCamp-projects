import unittest
import sea_level_predictor
import matplotlib as mpl

class SeaLevelPredictorTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Plot title is incorrect.")

    def test_plot_labels(self):
        actual_x = self.ax.get_xlabel()
        actual_y = self.ax.get_ylabel()
        self.assertEqual(actual_x, "Year", "X-axis label is incorrect.")
        self.assertEqual(actual_y, "Sea Level (inches)", "Y-axis label is incorrect.")

    def test_plot_data_lines(self):
        actual_lines = len(self.ax.get_lines())
        expected_lines = 2
        self.assertEqual(actual_lines, expected_lines, "The plot should contain two trend lines.")

if __name__ == "__main__":
    unittest.main()