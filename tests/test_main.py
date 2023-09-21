import unittest
import pandas as pd
from Pandas_package import main
from Pandas_package.main import load_data, descriptive_statistics

class TestMain(unittest.TestCase):

    def test_load_data(self):
        data = load_data("data/data_sample.csv")
        self.assertIsInstance(data, pd.DataFrame)

    def test_descriptive_statistics(self):
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 6, 7, 8, 9]
        }
        df = pd.DataFrame(data)
        stats = descriptive_statistics(df)
        self.assertAlmostEqual(stats['A']['mean'], 3.0)
        self.assertAlmostEqual(stats['B']['mean'], 7.0)

if __name__ == "__main__":
    unittest.main()
