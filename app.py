import streamlit as st
import pickle
import gzip
import pandas as pd
import requests

PAGE_TITLE = "Movie Recomendation | bisat19"
PAGE_ICON = "🎬"
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


dict_film = pickle.load(open('artefak/film_dict.pkl','rb'))
list_film = pd.DataFrame(dict_film)
list_judul = list_film['title'].values
with gzip.open('artefak/kesamaan.pkl.gz', 'rb') as f:
    kesamaan = pickle.load(f)

def fetch_poster(film_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(film_id))
    data = response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def rekomen(film):
    film_index = list_film[list_film['title'] == film].index[0]
    distances = kesamaan[film_index]
    film_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    rekomendasi_film = []
    rekomendasi_film_poster = []
    for i in film_list:
        film_id = list_film.iloc[i[0]].movie_id
        rekomendasi_film.append(list_film.iloc[i[0]].title)
        rekomendasi_film_poster.append(fetch_poster(film_id))
    return rekomendasi_film,rekomendasi_film_poster

st.title('Sistem Rekomendasi Film')

selected_film = st.selectbox(
    'Coba',
    (list_judul))

if st.button('Recommend'):
    judul,poster = rekomen(selected_film)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(judul[0])
        st.image(poster[0])
    with col2:
        st.text(judul[1])
        st.image(poster[1])
    with col3:
        st.text(judul[2])
        st.image(poster[2])
    with col4:
        st.text(judul[3])
        st.image(poster[3])
    with col5:
        st.text(judul[4])
        st.image(poster[4])

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(judul[5])
        st.image(poster[5])
    with col2:
        st.text(judul[6])
        st.image(poster[6])
    with col3:
        st.text(judul[7])
        st.image(poster[7])
    with col4:
        st.text(judul[8])
        st.image(poster[8])
    with col5:
        st.text(judul[9])
        st.image(poster[9])