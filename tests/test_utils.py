"""Basic tests for utility functions."""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src.app.utils import display_recommendations


def test_empty_recommendations():
    """Test display of empty recommendations."""
    assert display_recommendations([]) is None
