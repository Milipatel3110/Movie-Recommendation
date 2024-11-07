import streamlit as st

# Sample Data
sample_movies = ["The Matrix", "Inception", "Interstellar", "Pulp Fiction", "The Dark Knight"]
sample_user_id = 123  # Example user ID

# Page Title
st.title("Movie Recommendation System")

# Sidebar for Feature Selection
st.sidebar.title("Recommendation Type")
recommendation_type = st.sidebar.selectbox(
    "Select the type of recommendation you want:",
    ["Content-Based", "Collaborative Filtering", "KNN Similar Items", "Hybrid"]
)

# User Input
st.write("## User Input")
selected_movie = st.selectbox("Choose a movie you like:", sample_movies)
user_id = st.text_input("Enter your User ID", value=str(sample_user_id))

# Mock function to simulate recommendations
def get_mock_recommendations(recommendation_type, selected_movie, user_id):
    if recommendation_type == "Content-Based":
        return [
            {"title": "Inception", "similarity": 0.95},
            {"title": "Interstellar", "similarity": 0.90},
            {"title": "The Dark Knight", "similarity": 0.85},
        ]
    elif recommendation_type == "Collaborative Filtering":
        return [
            {"title": "Pulp Fiction", "rating_prediction": 4.7},
            {"title": "Fight Club", "rating_prediction": 4.6},
            {"title": "The Shawshank Redemption", "rating_prediction": 4.5},
        ]
    elif recommendation_type == "KNN Similar Items":
        return [
            {"title": "The Matrix Reloaded", "similarity": 0.98},
            {"title": "The Matrix Revolutions", "similarity": 0.97},
            {"title": "Equilibrium", "similarity": 0.93},
        ]
    elif recommendation_type == "Hybrid":
        return [
            {"title": "The Matrix Reloaded", "similarity": 0.96, "rating_prediction": 4.8},
            {"title": "Inception", "similarity": 0.94, "rating_prediction": 4.7},
            {"title": "Interstellar", "similarity": 0.92, "rating_prediction": 4.6},
        ]

# Display Recommendations Based on Selected Type
st.write("## Recommendations")

recommendations = get_mock_recommendations(recommendation_type, selected_movie, user_id)

if recommendation_type == "Content-Based":
    st.write(f"Top Content-Based Recommendations for '{selected_movie}':")
    for rec in recommendations:
        st.write(f"**{rec['title']}** - Similarity: {rec['similarity']:.2f}")
        
elif recommendation_type == "Collaborative Filtering":
    st.write(f"Top Collaborative Filtering Recommendations for User ID '{user_id}':")
    for rec in recommendations:
        st.write(f"**{rec['title']}** - Predicted Rating: {rec['rating_prediction']:.1f}")
        
elif recommendation_type == "KNN Similar Items":
    st.write(f"Movies similar to '{selected_movie}' based on KNN:")
    for rec in recommendations:
        st.write(f"**{rec['title']}** - Similarity: {rec['similarity']:.2f}")
        
elif recommendation_type == "Hybrid":
    st.write(f"Top Hybrid Recommendations for '{selected_movie}' and User ID '{user_id}':")
    for rec in recommendations:
        st.write(f"**{rec['title']}** - Similarity: {rec['similarity']:.2f}, Predicted Rating: {rec['rating_prediction']:.1f}")
