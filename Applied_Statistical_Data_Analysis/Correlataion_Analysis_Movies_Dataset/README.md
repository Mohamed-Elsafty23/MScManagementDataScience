# Movie Dataset Correlation Analysis 🎬

## Overview
This project performs a comprehensive correlation analysis on a movies dataset, focusing on understanding relationships between various movie features using point-biserial correlation analysis. The analysis explores connections between binary variables (like movie color and country) and numeric variables (such as budget, IMDB score, and Facebook likes).

## Dataset
The analysis uses the IMDB movies dataset (`movie_metadata.csv`) containing various features:

- Movie attributes (color, duration, title year)
- Social media metrics (Facebook likes for actors, directors, and movies)
- Performance indicators (IMDB score, gross earnings)
- Production details (budget, country, language)
- Audience engagement (user reviews, critic reviews)

## Analysis Methodology
The project employs point-biserial correlation analysis to examine relationships between binary and continuous variables. Key steps include:

1. Data preprocessing and cleaning
2. Binary variable creation
3. Correlation coefficient calculation
4. Statistical significance testing (p-value analysis)

## Key Findings

Some notable correlations discovered:

1. **Color vs Year**: Strong negative correlation (-0.31), indicating older movies tend to be black and white
2. **Color vs IMDB Score**: Positive correlation (0.15), suggesting color movies tend to have slightly higher ratings
3. **Country vs Gross**: Negative correlation (-0.18), showing some regional variations in box office performance
4. **Release Year vs IMDB Score**: Negative correlation (-0.15), indicating older movies tend to have slightly higher ratings

## Project Structure
```
├── main.ipynb                              # Main analysis notebook
├── movie_metadata.csv                      # Raw dataset
├── movie_metadata_cleaned.csv              # Preprocessed dataset
├── point_biserial_correlation_results.csv  # Analysis results
└── README.md                               # Project documentation
```

## Requirements
The project requires Python with the following packages:
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- jupyter

## Usage
1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the Jupyter notebook:
```bash
jupyter notebook main.ipynb
```

## Results
The analysis results are stored in `point_biserial_correlation_results.csv`, containing:
- Binary and numeric variable pairs
- Correlation coefficients
- P-values for statistical significance

## Contributing
Feel free to fork the project and submit pull requests with improvements or additional analyses.

## License
This project is open source and available under the MIT License.