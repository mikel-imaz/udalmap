import unittest
import sys
import pandas as pd
sys.path.append("../src")
from udalmap.utils import UdmDf

class TestUdalmapUtils(unittest.TestCase):

    def setUp(self):
        """Fixture"""
        self.udmdf = UdmDf()
        self.indicatorid = "7"
        self.body = "entities"
        
    def test_response_find(self):
        """Test response to find()"""
        df = self.udmdf.find()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.shape[0] > 0)

    def test_response_get(self):
        """Test response to get(indicatorId, body)"""
        df = self.udmdf.get(self.indicatorid, self.body)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.shape[0] > 0)

    def tearDown(self):
        """Clean the environment"""
        del self.udmdf
        del self.indicatorid
        del self.body


# Make this module executable in unittest
if __name__ == "__main__":
    unittest.main(verbosity=2)