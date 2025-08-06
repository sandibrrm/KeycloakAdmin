# test_keycloakadmin.py
"""
Tests for KeycloakAdmin module.
"""

import unittest
from keycloakadmin import KeycloakAdmin

class TestKeycloakAdmin(unittest.TestCase):
    """Test cases for KeycloakAdmin class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeycloakAdmin()
        self.assertIsInstance(instance, KeycloakAdmin)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeycloakAdmin()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
