import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.land import Land
from src.player import Player
import unittest
from main import Display
from unittest.mock import patch, mock_open
import json

task_number = 0
class test_main(unittest.TestCase):
    def test_display(self):
        print("test_display running")
        try:
            d = Display()
            print("test passed, display initialized")
            task_number + 1
        except Exception as e:
            self.fail("Dsiplay not initialized")

    #Reference: https://stackoverflow.com/questions/45163906/how-to-unit-test-function-opening-a-json-file
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
    "Name": "Mediterranean Avenue",
    "Type": "Property",
    "Price": 60,
    "Color": "Purple",
    "HousePrice": 50,
    "Rent": [2000, 4, 10, 30, 90, 160, 250]
    }))    
    def test_load_file(self, mock_file):
        print("test_load_file running")
        with open("Json\monopoly_space_info.json") as f:
            data = json.load(f)
        try:
            mock_file.assert_called_with("Json\monopoly_space_info.json")
            assert data["Name"] == "Mediterranean Avenue"
            assert data["Price"] == 60
            print("Load file test passed")
        except Exception as e:
            self.fail("Load file test failed")
      

    def test_moving(self):
        print("test_moving running")
        pass


    def test_money(self):
        print("test_money running")
        pass  

    def test_jail(self):
        pass
    
    def test_end_game(self):
        print("test_end_game running")
        pass

if __name__ == "__main__":
    unittest.main()
