import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.land import Land
from src.player import Player
import unittest
from main import Display

print("one")

class test_main(unittest.TestCase):
    def test_display(self):
        print("test_display running")
        pass

    def test_moving(self):
        print("test_moving running")
        pass

    def test_purchase(self):
        print("test_purchase running")
        pass

    def test_selling(self):
        print("test_selling running")
        pass

    def test_money(self):
        print("test_money running")
        pass

    def test_take_turn(self):
        print("test_take_turn running")
        pass

    def test_end_game(self):
        print("test_end_game running")
        pass

if __name__ == "__main__":
    unittest.main()
