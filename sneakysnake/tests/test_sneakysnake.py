"""
Unit and regression test for the sneakysnake package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import sneakysnake


def test_sneakysnake_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "sneakysnake" in sys.modules
