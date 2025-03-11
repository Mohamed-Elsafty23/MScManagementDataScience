# Spotify Dataset Clustering Analysis 🎵

## Overview
This project performs cluster analysis on Spotify's dataset of 5000 songs to identify patterns and groupings based on audio features. The analysis helps understand music similarities and can be used for music recommendations and playlist generation.

## Dataset
The project uses the "spotify_5000_songs.csv" dataset containing 5000 songs with their audio features including:
- Acousticness
- Danceability
- Energy
- Instrumentalness
- Valence
- Tempo
- And more...

## Features
- Data preprocessing and exploration of Spotify audio features
- Implementation of clustering algorithms
- Analysis of song clusters and their characteristics
- Generation of playlists based on cluster analysis
- Visualization of clustering results

## Project Structure
```
├── 6.3.3_spotify_5000_songs.csv    # Original dataset
├── audio_features_spotify.docx      # Documentation of audio features
├── clustered_spotify_data.csv       # Dataset with cluster assignments
├── clustered_spotify_data_with_playlists.csv  # Final dataset with playlists
└── main.ipynb                      # Main analysis notebook
```

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Open `main.ipynb` in Jupyter Notebook or JupyterLab
2. Follow the notebook cells for:
   - Data loading and preprocessing
   - Feature analysis
   - Cluster analysis
   - Results visualization

## Technologies Used
- Python 3.x
- Pandas for data manipulation
- Scikit-learn for clustering algorithms
- Matplotlib and Seaborn for visualization
- Jupyter Notebook for interactive analysis

## Results
The analysis identifies distinct clusters of songs based on their audio features, which can be used for:
- Music recommendation systems
- Playlist generation
- Understanding musical patterns and trends
- Genre classification

## License
This project is available under the MIT License.

## Acknowledgments
- Spotify for providing the audio features data
- The original dataset creators and contributors