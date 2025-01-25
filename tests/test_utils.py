"""Basic tests for utility functions."""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.app.display import display_recommendations


def test_empty_recommendations():
    """Test display of empty recommendations."""
    assert display_recommendations([]) is None
