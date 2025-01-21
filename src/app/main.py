"""Main application module for the Smart Buyer Assistant."""

import streamlit as st

from src.app.model import load_model, get_recommendations
from src.app.utils import show_sample_users, display_recommendations


def main():
    """Initialize and run the main application."""
    st.set_page_config(page_title="Smart Buyer Assistant", layout="wide")
    st.title("Smart Buyer Assistant 🛍️")
    st.write("Product Recommendation System")

    try:
        U, sigma, Vt, user_mapper, item_mapper, ratings_mean = load_model()

        user_id = st.number_input("Enter the user ID:", value=391642)

        if st.button("Get Recommendations", type="primary"):
            with st.spinner("Generating recommendations..."):
                recommendations = get_recommendations(
                    int(user_id), U, sigma, Vt, user_mapper, item_mapper, ratings_mean
                )
                display_recommendations(recommendations)

        show_sample_users(user_mapper)

    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        st.write("Error details for debugging:", str(e))


if __name__ == "__main__":
    main()
