# test_visionlens.py
"""
Tests for VisionLens module.
"""

import unittest
from visionlens import VisionLens

class TestVisionLens(unittest.TestCase):
    """Test cases for VisionLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VisionLens()
        self.assertIsInstance(instance, VisionLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VisionLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
