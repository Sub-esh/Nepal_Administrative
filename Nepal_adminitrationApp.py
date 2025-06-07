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

# extract district names for filtering
features = Nepal_admin.getInfo()['features']
district_names = sorted(set([f['properties']['ADM2_NAME'] for f in features]))

# sidebar for filtering
selected_district = st.sidebar.selectbox("Filter by Disctrict Name",['ALL']) + district_names

# show full or filtered map
if selected_district == "ALL":
    st.subheader("All Districts")
else:
     st.subheader(f"Selected District: {selected_district}")

create_map(Nepal_admin, selected_district if selected_district != "ALL" else None)


