# Airbnb Data Analysis Project

This project performs Exploratory Data Analysis (EDA) on Airbnb listing data from different cities, analyzing pricing patterns and differences between weekday and weekend rates.

## Project Overview

The analysis focuses on:
- Comparing pricing across different cities
- Analyzing weekday vs weekend price variations
- Visualizing price distributions and patterns
- Statistical analysis of pricing factors

## Data Source

The data is sourced from Google Sheets and includes:
- Listing prices for different cities
- Weekday and weekend pricing information
- Location data
- Other relevant listing attributes

## Features

- Data extraction from Google Sheets using gspread
- Data cleaning and preprocessing
- Statistical analysis using scipy
- Visualization using matplotlib and seaborn
- Geospatial visualization using folium

## Requirements

The project requires Python 3.7+ and the following packages:
```
pandas
gspread
matplotlib
seaborn
scipy
folium
oauth2client
```

You can install the required packages using:
```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repository
2. Install the required packages
3. Set up Google Sheets API credentials:
   - Create a service account in Google Cloud Console
   - Download the JSON credentials file
   - Rename it to `test.json` and place it in the project directory
4. Share your Google Sheet with the service account email

## Usage

1. Open `main.ipynb` in Jupyter Notebook or JupyterLab
2. Make sure all required packages are installed
3. Run the cells sequentially to perform the analysis

## Analysis Results

The analysis provides insights into:
- Price variations across different cities
- Weekend vs weekday pricing patterns
- Geographical price distributions
- Statistical significance of price differences

## Files Description

- `main.ipynb`: Main analysis notebook
- `test.json`: Google Sheets API credentials
- `airbnb_data.csv`: Processed dataset
- `requirements.txt`: Required Python packages

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.