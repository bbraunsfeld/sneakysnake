"""
Unit and regression test for the sneakysnake package.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest

import sneakysnake
#from sneakysnake import Button


def test_sneakysnake_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "sneakysnake" in sys.modules

def test_simple_math():
    """example test"""
    assert 2+2 == 2*2

def test_simple_math2():
    """example test 2"""
    assert 3+3 == 3*3
#def test_button_hover():
#    """tests if class Buttom has a method hover"""
#    assert hasattr(Button, 'hover') == True

#def test_button_invis():
#    """test if class Button has method invisible"""
#    assert hasattr(game_loop.Button, 'invisible') == True