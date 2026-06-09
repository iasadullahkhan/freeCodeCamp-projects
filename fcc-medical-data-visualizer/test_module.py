import unittest
import medical_data_visualizer
import matplotlib as mpl

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.char_plot = medical_data_visualizer.draw_cat_plot()
        self.heat_map = medical_data_visualizer.draw_heat_map()

    def test_categorical_plot_images(self):
        self.assertTrue(isinstance(self.char_plot, mpl.figure.Figure), "Catplot output should be a matplotlib figure.")

    def test_heat_map_images(self):
        self.assertTrue(isinstance(self.heat_map, mpl.figure.Figure), "Heatmap output should be a matplotlib figure.")

    def test_cat_plot_data_lines(self):
        ax = self.char_plot.axes[0]
        actual = len(ax.patches)
        expected = 12  # 6 features * 2 values (0 and 1)
        self.assertEqual(actual, expected, f"Expected 12 bars on the plot, got {actual}.")

if __name__ == "__main__":
    unittest.main()