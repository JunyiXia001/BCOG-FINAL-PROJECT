import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.land import Land
from src.player import Player
import unittest
from main import Display
from unittest.mock import patch, mock_open
import json
from unittest.mock import MagicMock
class test_main(unittest.TestCase):

    def test_display(self):
        print("test_display running")
        try:
            d = Display()
            print("test passed, display initialized")
        except Exception as e:
            self.fail("Dsiplay not initialized")

    #Reference: https://stackoverflow.com/questions/45163906/how-to-unit-test-function-opening-a-json-file
    #Mock opening file 
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
    "Name": "Mediterranean Avenue",
    "Type": "Property",
    "Price": 60,
    "Color": "Purple",
    "HousePrice": 50,
    "Rent": [2000, 4, 10, 30, 90, 160, 250]
    }))    
    #testing loading file function
    def test_load_file(self, mock_file):
        print("test_load_file running")
        with open("Json\monopoly_space_info.json") as f:
            data = json.load(f)
        try:
            mock_file.assert_called_with(r"Json\monopoly_space_info.json")
            assert data["Name"] == "Mediterranean Avenue"
            assert data["Price"] == 60
            print("Load file test passed")
        except Exception as e:
            self.fail("Load file test failed")
    #testing change in money
    def test_money(self):
        print("test_money running")

        player = Player(1)
        try:

            self.assertEqual(player.money, 1500)

            player.money -= 300
            self.assertEqual(player.money, 1200)

            player.money += 450
            self.assertEqual(player.money, 1650)
            print("test money passed")
        except Exception as e:
            self.fail("test_money failed")
    #testing jail status 
    def test_jail(self):
        print("test_jail running")
        player = Player(1)
        try:
            self.assertEqual(player.jail_status, 0)
            player.jail_status = 1
            self.assertEqual(player.jail_status, 1)
            print("test_jail passed")

        except Exception as e:
            self.fail("test_jail failed")

if __name__ == "__main__":
    unittest.main()
