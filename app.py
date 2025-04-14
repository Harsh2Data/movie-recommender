import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1a9fcecb7b50e9dd700f1901762baf79'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


with open('movies_dic.pkl', 'rb') as f:
    movie_list = pickle.load(f)
movie = pd.DataFrame(movie_list)
st.title("Movie Recommender")
selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movie['title'].values
)
with open('similarity.pkl','rb') as f:
    similarity = pickle.load(f)
def recommand(selected_movie):
    recommended = []
    recommended_movie_poster   = []
    movie_index = movie[movie['title'] == selected_movie].index[0]
    dis = similarity[movie_index]
    movie_list = sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_list:
        recommended_movie_poster.append(fetch_poster(movie.iloc[i[0]].id))

        recommended.append(movie.iloc[i[0]].title)
    return recommended,recommended_movie_poster

if st.button("Recommend"):
    name, poster = recommand(selected_movie)

    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text (name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])

