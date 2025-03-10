# Netflix Dataset Analysis & Recommendation System 🎬

[![Gradio](https://img.shields.io/badge/Gradio-Demo-orange)](https://huggingface.co/spaces/Mohamed284/Netflix_Recommendation_System)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Overview

This project implements a sophisticated hybrid recommendation system for Netflix movies and TV shows, combining multiple advanced approaches to provide accurate and diverse content recommendations:

- **Content-Based Filtering** (Text Similarity using TF-IDF)
- **Collaborative Filtering** (User Preferences using SVD)
- **Graph-Based Learning** (Node2Vec for network-based recommendations)

## Features

- **Interactive Demo**: Try the recommendation system on [Gradio](https://huggingface.co/spaces/Mohamed284/Netflix_Recommendation_System)
- **Hybrid Approach**: Combines multiple recommendation techniques
- **Data Visualization**: Comprehensive EDA with informative visualizations
- **Network Analysis**: Graph-based content relationships

## Dataset

The analysis uses the Netflix titles dataset (`netflix_titles.csv`) containing metadata about movies and TV shows, including:

- Show ID, Title, Type (Movie/TV Show)
- Director, Cast, Country
- Release Year, Rating, Duration
- Genre Categories
- Plot Descriptions

## Key Findings

1. **Content Distribution**:
   - ~70% movies, ~30% TV series
   - Significant regional variations in content type distribution

2. **Geographic Insights**:
   - US leads in content volume
   - India, UK, and South Korea follow as major content producers

3. **Content Trends**:
   - Substantial library expansion between 2015-2021
   - Movie durations typically cluster between 90-110 minutes

## Methodology

### 1. Content-Based Filtering
- TF-IDF vectorization for text analysis
- Cosine similarity for content matching

### 2. Collaborative Filtering
- Matrix factorization using SVD
- User-item interaction modeling

### 3. Graph-Based Learning
- Node2Vec for network embeddings
- Content relationship mapping

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository
2. Install dependencies
3. Run the application:
```bash
python app.py
```

## Requirements

- Python 3.7+
- Required packages:
  - gradio
  - pandas
  - numpy
  - networkx
  - matplotlib
  - scikit-learn
  - plotly
  - joblib
  - node2vec

## Project Structure

```plaintext
├── app.py                 # Main application file
├── netflix_titles.csv     # Dataset
├── node_embeddings.pkl    # Pre-trained embeddings
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

## Ethical Considerations

- User privacy and data protection
- Age-appropriate content recommendations
- Cultural sensitivity and diversity
- Regulatory compliance (GDPR, COPPA)

## Authors

Group 1 (March 10, 2025):
- Mohamed Khaled Elsafty
- Seyed Bahram Taghavi Araghi
- Hossein Ojaghi
- Mayurbhai J. Odedra
- Ayesha Jabeen

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Netflix for inspiring the recommendation system architecture
- The open-source community for tools and libraries
- Hugging Face for hosting the demo


## Project Report

You can view our detailed project report in the following ways:

1. **Direct PDF Link**: [View Full Report](Group_1_Netflix%20Dataset%20Analysis%20%26%20Recommendation%20System.pdf)

2. **Online Preview**: 
   <object data="Group_1_Netflix%20Dataset%20Analysis%20%26%20Recommendation%20System.pdf" type="application/pdf" width="100%" height="600px">
      <p>It appears you don't have a PDF plugin for this browser. You can 
      <a href="Group_1_Netflix%20Dataset%20Analysis%20%26%20Recommendation%20System.pdf">click here to download the PDF file.</a></p>
   </object>

> **Note**: If the preview doesn't load, you can download the PDF file directly and view it locally.