"""Basic tests for utility functions."""

from src.app.display import display_recommendations


def test_empty_recommendations():
    """Test display of empty recommendations."""
    assert display_recommendations([]) is None
