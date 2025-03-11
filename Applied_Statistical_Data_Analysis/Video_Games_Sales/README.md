# Video Game Sales Analysis 🎮

## Overview
This project analyzes a comprehensive dataset of video game sales across different regions, platforms, and genres. The dataset includes games with sales greater than 100,000 copies, providing insights into the global gaming market trends and patterns.

## Dataset Description
The dataset contains the following information for each video game:
- Rank - Ranking of overall sales
- Name - The game's name
- Platform - Platform of the game's release (i.e. PC, PS4, etc.)
- Year - Year of the game's release
- Genre - Genre of the game
- Publisher - Publisher of the game
- Sales data (in millions) for different regions:
  - NA_Sales - North America
  - EU_Sales - Europe
  - JP_Sales - Japan
  - Other_Sales - Rest of the world
  - Global_Sales - Total worldwide sales

## Analysis Features
The project includes various analyses and visualizations:
1. Distribution analysis of global sales
2. Temporal analysis of game releases per year
3. Genre-wise sales analysis
4. Platform-based sales comparison
5. Year vs Global Sales correlation analysis
6. Sales prediction modeling using machine learning

## Visualizations
- Global sales distribution histogram
- Number of games released per year
- Total global sales by genre
- Sales trends across different platforms
- Correlation analysis between variables

## Technologies Used
- Python 3.x
- Data Analysis: Pandas, NumPy
- Visualization: Matplotlib, Seaborn, Plotly
- Machine Learning: Scikit-learn
- Statistical Analysis: SciPy

## Setup and Installation
1. Clone the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook:
   ```bash
   jupyter notebook main.ipynb
   ```

## Project Structure
```
├── main.ipynb              # Main analysis notebook
├── vgsales.csv            # Dataset file
├── requirements.txt       # Required Python packages
├── README.md             # Project documentation
├── scaler.pkl            # Saved scaler model
├── trained_model.pkl     # Saved trained model
└── output.json           # Model output and metrics
```

## Key Findings
- Analysis of sales trends across different gaming platforms
- Identification of most successful game genres
- Temporal analysis of gaming industry growth
- Regional sales pattern analysis
- Predictive modeling for game sales

## License
This project is available under the MIT License.

## Acknowledgments
The dataset used in this project contains video game sales information from various sources, compiled for analytical purposes.