# Titanic Survival Prediction using GLM and Machine Learning

This project analyzes the famous Titanic dataset to predict passenger survival using various machine learning models, including Generalized Linear Models (GLM) and other classifiers.

## Project Overview

The project aims to predict whether a passenger survived the Titanic disaster based on features such as passenger class, age, sex, and embarkation point. Multiple machine learning models are implemented and compared to find the best performing model.

## Dataset

The dataset (`titanic.txt`) contains information about Titanic passengers including:
- Passenger ID
- Survival status (target variable)
- Passenger class (Pclass)
- Name
- Sex
- Age
- Number of siblings/spouses aboard (SibSp)
- Number of parents/children aboard (Parch)
- Ticket number
- Fare
- Cabin
- Port of Embarkation

## Models Implemented

- Logistic Regression
- Ridge Classifier
- Stochastic Gradient Descent (SGD) Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- K-Nearest Neighbors Classifier

## Features

- Data preprocessing and cleaning
- Handling missing values
- Feature engineering
- Model training and evaluation
- Confusion matrix visualization for model comparison

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

The analysis is contained in Jupyter notebooks:
- `main.ipynb`: Primary analysis with multiple machine learning models
- `main_2.ipynb`: Additional analysis using statsmodels for GLM implementation

To run the notebooks:
1. Start Jupyter Notebook or JupyterLab
2. Open either `main.ipynb` or `main_2.ipynb`
3. Run the cells sequentially

## Project Structure

```
├── README.md
├── requirements.txt
├── titanic.txt          # Dataset
├── main.ipynb           # Main analysis notebook
└── main_2.ipynb        # Additional GLM analysis
```

## Methodology

1. Data Preprocessing:
   - Handling missing values in Age and Embarked columns
   - Encoding categorical variables (Sex, Embarked)
   - Feature selection

2. Model Training:
   - Split data into training and test sets
   - Train multiple classifier models
   - Evaluate model performance using confusion matrices

## Results

The project includes visualizations of confusion matrices for each model, allowing for easy comparison of model performance in predicting passenger survival.

## Contributing

Feel free to fork this repository and submit pull requests with improvements.

## License

This project is open source and available for educational purposes.