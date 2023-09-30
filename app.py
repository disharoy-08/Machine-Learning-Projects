import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{movie_id}?api_key=3baa0560421793e28acd0dcea71c4dc4&language=en-US'.format(movie_id))
#     data = response.json()
#     return 'https://image.tmdb.org/t/p/original'+data['poster_path']

def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=3baa0560421793e28acd0dcea71c4dc4&language=en-US')

    if response.status_code == 200:
        data = response.json()
        # Check if the 'id' key is present in the response
        if 'id' in data:
            return 'https://image.tmdb.org/t/p/original' + data['poster_path']
        else:
            return 'No poster available for this movie.'
    else:
        return 'Error fetching movie data from TMDb API.'



def recommend(movie):
    movie_index = movies [movies ['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movies_id = movies .iloc[i[0]].movie_id

        recommended_movies.append(movies .iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movies_id))

    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you to be contacted?',
movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

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


