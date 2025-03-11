# Diamond Price Prediction 💎

## Overview
This project implements a machine learning model to predict diamond prices based on various features such as carat weight, cut, color, clarity, and dimensions. The model helps in understanding the key factors that influence diamond prices in the market.

## Dataset
The project uses the `diamonds.csv` dataset, which contains the following features:
- carat: Weight of the diamond
- cut: Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- color: Diamond color, from J (worst) to D (best)
- clarity: A measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
- depth: Total depth percentage
- table: Width of top of diamond relative to widest point
- price: Price in US dollars
- x: Length in mm
- y: Width in mm
- z: Depth in mm

## Project Structure
```
├── main.ipynb          # Main analysis notebook
├── diamonds.csv        # Dataset
├── README.md          # Project documentation
└── requirements.txt   # Required Python packages
```

## Methodology
1. **Data Exploration**
   - Load and inspect the dataset
   - Visualize correlations and distributions
   - Handle missing values and outliers

2. **Model Building**
   - Preprocess data and encode categorical variables
   - Train a Linear Regression model
   - Feature engineering and selection

3. **Model Evaluation**
   - Evaluate using MSE and R2 metrics
   - Visualize actual vs. predicted prices
   - Analyze residuals

## Requirements
- Python 3.7+
- Required packages are listed in `requirements.txt`

## Usage
1. Clone the repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Run the Jupyter notebook:
```bash
jupyter notebook main.ipynb
```

## Results
The project demonstrates the relationship between various diamond characteristics and their prices, helping in:
- Understanding key price determinants
- Making price predictions for new diamonds
- Analyzing market trends and patterns

## Contributing
Feel free to fork the project and submit pull requests with improvements.

## License
This project is open source and available under the MIT License.