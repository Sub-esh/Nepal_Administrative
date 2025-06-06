# Nepal Administrative Boundaries Visualizer

This app visualizes administrative boundaries of Nepal

## How the code is organized
Main:-Nepal_administrationApp.py #main app, imports, utility
     -Readme.md 
     -requirements.txt 
Utils:-data_loader.py # load and/or cache data
      -model_loader.py # load and cache models
data:-data.csv #store data files/source

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`