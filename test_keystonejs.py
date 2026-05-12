# test_keystonejs.py
"""
Tests for KeystoneJS module.
"""

import unittest
from keystonejs import KeystoneJS

class TestKeystoneJS(unittest.TestCase):
    """Test cases for KeystoneJS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeystoneJS()
        self.assertIsInstance(instance, KeystoneJS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeystoneJS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
