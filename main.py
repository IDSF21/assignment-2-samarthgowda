import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache
def load_songs():
    df = pd.read_csv("./data.csv")
    df = df.drop_duplicates(["id", "name"], keep="last")

    df = df.dropna(how="any")

    df["year"] = df["year"].astype(int)

    return df

songs = load_songs()

@st.cache
def get_years(songs):
    return list(np.sort(songs["year"].unique()))

years = get_years(songs)

@st.cache
def calculate_songs_agg(songs):

    songs_agg = songs.groupby("year").agg(
        {
            "acousticness": np.mean,
            "danceability": np.mean,
            "duration_ms": np.mean,
            "energy": np.mean,
            "instrumentalness": np.mean,
            "liveness": np.mean,
            "loudness": np.mean,
            "popularity": np.mean,
            "speechiness": np.mean,
            "tempo": np.mean,
            "valence": np.mean
        }
    )

    songs_agg.index = pd.to_datetime(songs_agg.index, format="%Y")

    return songs_agg

songs_agg = calculate_songs_agg(songs)


with st.container():
    """
    # Songs from 1921-2020 

    Information about these songs are from Spotify Web API. Dataset provided from [Kaggle](https://www.kaggle.com/ektanegi/spotifydata-19212020).
    """

    if st.checkbox("Show raw dataframe of Spotify 1921-2020 Songs Dataset"):
        songs


    if st.checkbox("Show dataframe of average values for different columns in Spotify Songs grouped by Year"):
        songs_agg


with st.container():
    """
    ### Understanding how different aspects of songs have changed over time
    """

    overall_variable_select = st.selectbox(
        "Select the variable that you would like to explore.", 
        [
            "acousticness", 
            "danceability", 
            "duration_ms", 
            "energy", 
            "instrumentalness", 
            "liveness",
            "loudness",
            "speechiness",
            "tempo",
            "valence"
        ],
        key="overall_variable",
    )

    songs_agg_data = songs_agg[[overall_variable_select]]

    songs_agg_data["year"] = songs_agg_data.index 

    fig, ax = plt.subplots()
    ax.plot("year", overall_variable_select, data=songs_agg_data)
    ax.set_xlabel("Release Year")
    ax.set_ylabel(overall_variable_select)
    ax.set_title(f"{overall_variable_select} vs Release Year for Spotify Song Data 1921-2021")
    st.pyplot(fig)


with st.container():
    """
    ### Understanding the distribution of aspects of songs for a given release year range
    """

    col1, col2 = st.columns(2)

    with col1:
        start_year, end_year = st.select_slider("Select a range of years to explore", options=years, value=[years[0], years[-1]])
        

    with col2:
        year_variable_select = st.selectbox(
            "Select the variable that you would like to explore", 
            [
                "acousticness", 
                "danceability", 
                "duration_ms", 
                "energy", 
                "instrumentalness", 
                "liveness",
                "loudness",
                "speechiness",
                "tempo",
                "valence"
            ],
            key="year_variable",
        )


    with st.container():
        
        after_start = songs["year"] >= start_year
        before_end = songs["year"] <= end_year
        between_years = after_start & before_end
        songs_data = songs.loc[between_years]

        songs_data = songs_data[["year", year_variable_select]]

        fig, ax = plt.subplots()
        ax.hist(songs_data[year_variable_select])
        ax.set_xlabel(f"Release Year from {start_year} to {end_year}")
        ax.set_ylabel(overall_variable_select)
        ax.set_title(f"Histogram of {overall_variable_select} for Spotify Song Data {start_year} to {end_year}")
        st.pyplot(fig)