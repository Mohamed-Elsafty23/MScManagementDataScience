# Lego Inventory Analysis

This project analyzes a Lego brick inventory dataset to understand the distribution of colors, product types, and variety across different Lego pieces.

## Project Overview

The analysis includes:
- Color distribution analysis across all products
- Product type analysis (Standard bricks vs Special bricks vs Special Tools)
- Color variety analysis for different products
- Comparison of dark vs light shade distributions

## Dataset Description

The dataset (`ASDA Week 2 Lego Inventory - Sheet1.csv`) contains information about:
- Product/Color: Unique identifier for each Lego piece
- Product type: Classification (Standard bricks, Special bricks, Special Tools)
- Color columns: Various color variations including different shades

## Analysis Features

1. **Color Distribution**
   - Visualization of total count for each color
   - Analysis of most common colors in the inventory

2. **Product Analysis**
   - Average number of colors per product type
   - Identification of products with highest color variety

3. **Shade Analysis**
   - Comparison between dark and light shades
   - Distribution visualization of color variations

## Files in the Project

- `ASDA Week 2 Lego Inventory - Sheet1.csv`: Raw data file containing the Lego inventory
- `lego_data.ipynb`: Jupyter notebook containing the analysis code
- `Report Lego Inventory.pdf`: Detailed report of the analysis
- `requirements.txt`: Required Python packages

## Getting Started

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Open and run the Jupyter notebook `lego_data.ipynb`

## Technologies Used

- Python
- Pandas for data manipulation
- Matplotlib for data visualization
- Jupyter Notebook for interactive analysis