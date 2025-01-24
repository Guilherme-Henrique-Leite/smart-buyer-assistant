"""Utility functions for the recommendation system interface."""

import numpy as np
import pandas as pd
import streamlit as st


def display_recommendations(recommendations):
    """Display product recommendations in the Streamlit interface.

    :recommendations: List of tuples (product_id, rating) to display
    """
    if recommendations:
        st.subheader("Personalized Recommendations")
        cols = st.columns(5)
        for idx, (prod_id, rating) in enumerate(recommendations):
            with cols[idx]:
                st.metric(label=f"Product {prod_id}", value=f"⭐ {rating:.2f}")
    else:
        st.warning("No recommendations found for this user.")


def show_sample_users(user_mapper):
    """Display sample user IDs for testing the system.

    :user_mapper(dict): Dictionary containing valid user IDs
    """
    with st.expander("See examples of valid user IDs"):
        st.write("### Available User IDs")
        sample_users = sorted(list(user_mapper.keys()))
        sample_users = np.random.choice(sample_users, size=5, replace=False)

        user_data = [
            {
                "User ID": int(user_id),
                "Example of Use": f"Enter {int(user_id)} and click on 'Get Recommendations'",
            }
            for user_id in sample_users
        ]

        df_examples = pd.DataFrame(user_data)
        st.table(df_examples)
        st.info("💡 Tip: Use any of these IDs to test the recommendation system!")
