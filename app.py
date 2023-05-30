import streamlit as st
import pandas as pd

# Load the IMDb dataset
imdb_data = pd.read_csv('imdb_dataset.csv')

# Set page title and layout
st.set_page_config(page_title='IMDb Movie Viewer', layout='wide')

# Set sidebar options
st.sidebar.title('Filters')
years = st.sidebar.slider('Release Year', min_value=1900, max_value=2023, value=(2000, 2023))
selected_genres = st.sidebar.multiselect('Genres', imdb_data['Genre'].unique())

# Filter the dataset based on user selections
filtered_data = imdb_data[
    (imdb_data['Year'].between(years[0], years[1])) & 
    (imdb_data['Genre'].isin(selected_genres))
]

# Display the filtered data
st.title('IMDb Movie Viewer')
st.write(f"Displaying {len(filtered_data)} movies")

st.dataframe(filtered_data)
