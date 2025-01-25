"""Model operations for recommendation system."""

import numpy as np
import streamlit as st


@st.cache_data
def load_model():
    try:
        model_path = "notebooks/models/recommendation_model.npz"
        model_data = np.load(model_path, allow_pickle=True)
        return (
            model_data["U"],
            model_data["sigma"],
            model_data["Vt"],
            dict(model_data["user_mapper"]),
            dict(model_data["item_mapper"]),
            model_data["ratings_mean"],
        )
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model is properly uploaded.")
        return None


def get_recommendations(
    user_id, U, sigma, Vt, user_mapper, item_mapper, ratings_mean, n_recommendations=5
):
    try:
        if user_id not in user_mapper:
            st.error(f"User {user_id} not found!")
            return []

        user_idx = user_mapper[user_id]
        sigma_diag = np.diag(sigma)

        user_pred = np.dot(np.dot(U[user_idx : user_idx + 1], sigma_diag), Vt).flatten()
        user_pred = user_pred + ratings_mean
        pred_ratings = np.clip(user_pred, 1, 5)

        top_indices = np.argsort(-pred_ratings)[:n_recommendations]
        top_ratings = pred_ratings[top_indices]

        reverse_item_mapper = {v: k for k, v in item_mapper.items()}
        recommendations = []

        for idx, rating in zip(top_indices, top_ratings):
            if idx in reverse_item_mapper:
                recommendations.append((reverse_item_mapper[idx], rating))

        return recommendations

    except Exception as e:
        st.error(f"Error generating recommendations: {str(e)}")
        return []
