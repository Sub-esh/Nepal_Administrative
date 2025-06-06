import folium
from streamlit_folium import st_folium

def create_map(Nepal_admin):
    # Convert GEE FeatureCollection to GeoJSON
    geoj = Nepal_admin.geometry().coordinates().get(0).getInfo

    # Create Folium map centered on the Kathmandu
    m = folium.Map(location = [84.259,28.06], zoom_start = 7)

    # Add the administrative boundaries
    folium.GeoJson(
        geoj,
        name = "Nepal Adminstrative",
        style_function = lambda feature: {
            'fillColor' : '#4466cc',
            'color' : 'black',
            'weight': 1,
            'fillOpacity' : 0.4
        }
    ).add_to(m)
    return m