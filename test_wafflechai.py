# test_wafflechai.py
"""
Tests for WaffleChai module.
"""

import unittest
from wafflechai import WaffleChai

class TestWaffleChai(unittest.TestCase):
    """Test cases for WaffleChai class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WaffleChai()
        self.assertIsInstance(instance, WaffleChai)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WaffleChai()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
