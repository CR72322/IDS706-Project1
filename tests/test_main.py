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
            'Year': [2017, 2018],
            'Cost of a healthy diet': [3.952, 4.069]
        }
        df = pd.DataFrame(data)
        stats = descriptive_statistics(df, 'Cost of a healthy diet')
        self.assertAlmostEqual(stats['mean'], 4.0105)

if __name__ == "__main__":
    unittest.main()
