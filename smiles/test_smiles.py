import unittest
from smiles import smiles

class TestSmiles(unittest.TestCase):
    def test_smile(self):
        """Test that smile function returns the correct emoticon"""
        self.assertEqual(smiles.smile(), ":)")

    def test_laugh(self):
        """Test that laugh function returns the correct emoticon"""
        self.assertEqual(smiles.laugh(), ":D")

    def test_cry(self):
        """Test that cry function returns the correct emoticon"""
        self.assertEqual(smiles.cry(), ":'(")

    def test_tongue(self):
        """Test that tongue function returns the correct emoticon"""
        self.assertEqual(smiles.tongue(), ":P")

    def test_glasses(self):
        """Test that glasses function returns the correct emoticon"""
        self.assertEqual(smiles.glasses(), "8)")

if __name__ == "__main__":
    unittest.main()