import ee

def initialize_ee():
    try:
        ee.Initialize(project = "ee-subsonic")
    except Exception as e:
        ee.Authenticate()