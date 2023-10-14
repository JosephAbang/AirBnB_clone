#!/ussr/bin/python3

import unittest
from models.base_model import BaseModel as BM
from datetime import datetime as dt


class TestBaseModel(unittest.TestCase):
    def test_Updated_at_type(self):
        assertEqual(type(BM.updated_at), type(dt.now()))
    def test_created_at_type(self):
        assertEqual(type(BM.created_at), type(dt.now()))
    def test_id_type(self):
        assertEqual(type(BM.id, str))

    



if __name__ == "__main__":
    unittest.main()
