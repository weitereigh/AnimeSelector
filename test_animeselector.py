# test_animeselector.py
"""
Tests for AnimeSelector module.
"""

import unittest
from animeselector import AnimeSelector

class TestAnimeSelector(unittest.TestCase):
    """Test cases for AnimeSelector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeSelector()
        self.assertIsInstance(instance, AnimeSelector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeSelector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
