import streamlit as st
from utils.gee_auth import initialize_ee
from utils.get_data import get_Nepal_adm
from components.map_display import create_map

# page config
st.set_page_config(page_title = "Nepal Administrative Map", layout = "wide" )

# title
st.title ("Administrative Boundary of Nepal using Google Earth Engine")

#Initialize GEE
initialize_ee()

# get data from gee
Nepal_admin = get_Nepal_adm()

# Create and display map
m = create_map(Nepal_admin)

# render the folium map
st_folium(m, width=1200, height=600)


