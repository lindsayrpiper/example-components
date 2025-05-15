import unittest
from smiles import smiles

class TestSmiles(unittest.TestCase):
    def test_cry(self):
        self.assertEqual(smiles.cry(), ":'(")
        
    def test_tongue(self):
        self.assertEqual(smiles.tongue(), ":P")
        
    def test_glasses(self):
        self.assertEqual(smiles.glasses(), "8^)")
        
if __name__ == "__main__":
    unittest.main()