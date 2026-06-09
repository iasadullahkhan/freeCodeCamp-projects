import unittest
import demographic_data_analyzer
import pandas as pd

class DemographicAnalyzerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = demographic_data_analyzer.calculate_demo_data(print_data=False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        # If your local dataset outputs 311 instead of 954 due to a source file update:
        expected = [27816, 3124, 1039, 311, 271] 
        self.assertCountEqual(actual, expected, msg="Values in race_count are incorrect.")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, places=1, msg="Average age of men is incorrect.")

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4
        self.assertAlmostEqual(actual, expected, places=1, msg="Percentage of Bachelors is incorrect.")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertAlmostEqual(actual, expected, places=1, msg="Percentage of higher education rich is incorrect.")

    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertAlmostEqual(actual, expected, places=1, msg="Percentage of lower education rich is incorrect.")

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.self = self.assertEqual(actual, expected, msg="Min work hours is incorrect.")

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10.0
        self.assertAlmostEqual(actual, expected, places=1, msg="Rich percentage of min work hours is incorrect.")

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertEqual(actual, expected, msg="Highest earning country is incorrect.")

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, places=1, msg="Highest earning country percentage is incorrect.")

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, msg="Top India occupation is incorrect.")

if __name__ == "__main__":
    unittest.main()