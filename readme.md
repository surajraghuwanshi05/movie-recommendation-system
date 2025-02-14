# Movie Recommendation System

This project is a **Movie Recommendation System** designed to suggest movies based on a user's preferences. The system uses various attributes of movies such as genre, title, popularity, and user ratings to provide personalized recommendations. This project aims to improve the movie-watching experience by helping users discover movies that match their interests.

## Features

- **Movie Suggestions**: Recommends movies based on the movie name provided by the user.
- **Movie Poster Display**: Displays movie posters alongside the movie titles for a visual experience.
- **Data Sources**: Utilizes movie data like title, budget, genres, overview, runtime, revenue, and popularity to make recommendations.
- **User-Friendly Interface**: Built using Streamlit for easy interaction and data visualization.

## Technologies Used

- **Python**: The main programming language used for building the recommendation system.
- **Streamlit**: For creating the user interface and interactive visualizations.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: Used for machine learning algorithms .
- **IMDb dataset** (or any other relevant movie dataset): Provides information about movies.

## Setup

To run this project locally, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:
- Python (version 3.7 or higher)
- pip (Python's package installer)

### Install Required Libraries

```bash
pip install -r requirements.txt
```

# Movie Recommendation System

## Overview
This project implements a movie recommendation system using machine learning techniques. The system leverages a combination of data preprocessing, feature extraction, and similarity metrics to recommend movies based on user preferences. The recommendation system is built on the [TMDB 5000 Movies dataset](https://www.kaggle.com/datasets/tmdb/tmdb-5000-movie-dataset).

## Datasets
The project utilizes two primary datasets:
1. **Movies Dataset (`tmdb_5000_movies.csv`)**: Contains information about the movies, including their titles, genres, budget, revenue, popularity, and more.
2. **Credits Dataset (`tmdb_5000_credits.csv`)**: Contains information about the cast and crew of the movies.

### Dataset Details:
- **Movies Dataset**: 
  - Columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `release_date`, `budget`, `revenue`, `popularity`, `vote_average`, etc.
- **Credits Dataset**:
  - Columns: `movie_id`, `cast`, `crew`.

## Libraries Used
- **pandas**: For data manipulation and preprocessing.
- **matplotlib & seaborn**: For data visualization.
- **sklearn**: For machine learning algorithms and feature extraction (CountVectorizer and TfidfVectorizer).
- **pickle**: For saving and loading the model and data.

## Steps

### 1. Data Preprocessing
- Merged the movies dataset with the credits dataset on the `title` column.
- Dropped irrelevant columns such as `budget`, `homepage`, `original_language`, `spoken_languages`, `production_companies`, `production_countries`, `tagline`, `vote_average`, and `vote_count`.
- Extracted the `year` and `decade` of movie release from the `release_date`.
- Cleaned the `genres`, `keywords`, `cast`, and `crew` columns by converting them into lists and removing unnecessary spaces.
- Combined all relevant features (overview, genres, keywords, cast, crew, year, and decade) into a single `tags` column for the recommendation system.

### 2. Feature Extraction
- Used **CountVectorizer** and **TfidfVectorizer** for converting the text data in the `tags` column into numerical vectors.
- Both vectorizers have been used to compute the similarity matrix between movies.

### 3. Similarity Calculation
- Calculated cosine similarity between the movies based on their feature vectors using both **CountVectorizer** and **TfidfVectorizer**.

### 4. Movie Recommendation
- Created a function to recommend similar movies based on a given movie title. The function calculates the cosine similarity and returns the top 5 most similar movies.

### 5. Model Saving
- Saved the processed movie data (`movie_list.pkl`) and the similarity matrix (`similarity.pkl`) using `pickle` for later use in the recommendation system.

