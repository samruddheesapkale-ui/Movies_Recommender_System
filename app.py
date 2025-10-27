import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3426ddd59ebafd441882fbab9a28318e&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Define recommendation function
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters  # 👈 moved outside the loop!


# Upload pickle files manually
movies_file = st.file_uploader("Upload movies_dict.pkl", type="pkl")
similarity_file = st.file_uploader("Upload similarity.pkl", type="pkl")

if movies_file is not None and similarity_file is not None:
    movies_dict = pickle.load(movies_file)
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(similarity_file)
    st.success("✅ Files loaded successfully! Now you can use the recommender system.")

    # ⬇️ Keep the rest of your code (like recommend() function etc.) here ⬇️

else:
    st.warning("⚠️ Please upload both .pkl files to start.")

# Streamlit UI
st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


