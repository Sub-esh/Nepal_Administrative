import geemap.foliumap as geemap

def create_map(Nepal_admin, selected_district = None):
    # Create a geemap map object
    m = geemap.Map(center=(28.3949,84.124),zoom = 9)

    # filter by district
    if selected_district:
        district = Nepal_admin.filter(ee.Filter.eq("ADM2_NAME", selected_district))
    else:
        district = Nepal_admin
    
    # Add the the layer to the map
    m.addLayer(district, {}, "Nepal Districts")

    # Set map to bounds of the districts
    m.centerObject(Nepal_admin, zoom = 9)

    # Add layer control
    m.add_control(geemap.LayersControl())

    # Display the map in Streamlit
    return m.to_streamlit(width=1200, height=600)
