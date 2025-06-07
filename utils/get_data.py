import ee

def get_Nepal_adm():
    # Load the admin boundaries of Nepal
    Nepal_admin = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level2")\
                    .filter(ee.Filter.eq('ADM2_NAME','Bagmati'))
