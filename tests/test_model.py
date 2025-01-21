"""Basic tests for model operations."""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src.app.model import get_recommendations


def test_get_recommendations_invalid_user():
    """Test recommendation for invalid user."""
    recommendations = get_recommendations(999, [], [], [], {}, {}, 0)
    assert not recommendations
