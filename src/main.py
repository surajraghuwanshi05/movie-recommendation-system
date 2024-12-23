import pickle
import streamlit as st
import requests
from config.config import KEY



# Function to fetch movie poster from TMDB API

API_KEY = KEY  # use your api key 
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data['Response'] == 'True':
        return data['Poster']  # Return poster URL
    else:
        return None  # Return None if movie not found or error

# Function to recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    # Fetch top 5 recommended movies
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movies.iloc[i[0]].title))  # Fetch movie poster

    return recommended_movie_names, recommended_movie_posters

# Streamlit app
st.header('Movie Recommender System')

# Load the movie list and similarity matrix from the pickle files
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Movie select box
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Show recommendation when button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display recommended movies and their posters
    cols = st.columns(5)  # Create 5 columns
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])  # Display the movie poster




