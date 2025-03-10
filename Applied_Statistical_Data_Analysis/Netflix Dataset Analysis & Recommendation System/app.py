import gradio as gr
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go
from joblib import load

# Load the data and models
df = pd.read_csv('netflix_titles.csv')
node_embeddings = load('node_embeddings.pkl')

# Create TF-IDF matrix
def create_soup(x):
    features = []
    if isinstance(x['description'], str):
        features.append(x['description'])
    if isinstance(x['cast'], str):
        features.append(x['cast'])
    if isinstance(x['director'], str):
        features.append(x['director'])
    if isinstance(x['listed_in'], str):
        features.append(x['listed_in'])
    if isinstance(x['title'], str):
        features.append(x['title'])
    return ' '.join(features)
df['combined_features'] = df.apply(create_soup, axis=1)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_hybrid_recommendations(query, n_recommendations=10):
    # Convert query to TF-IDF vector
    query_vec = tfidf.transform([query])
    
    # Get content-based similarity scores
    content_scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    
    # Combine scores with weights
    weights = {'content': 0.7, 'node_embeddings': 0.3}
    final_scores = content_scores * weights['content']
    
    # Get top recommendations
    sim_scores_with_index = list(enumerate(final_scores))
    sim_scores_with_index = sorted(sim_scores_with_index, key=lambda x: x[1], reverse=True)
    sim_scores_with_index = sim_scores_with_index[:n_recommendations]
    
    # Create recommendations DataFrame
    recommendations = []
    for i, score in sim_scores_with_index:
        recommendations.append({
            'title': df['title'].iloc[i],
            'type': df['type'].iloc[i],
            'similarity_score': score,
            'description': df['description'].iloc[i],
            'genres': df['listed_in'].iloc[i]
        })
    
    return pd.DataFrame(recommendations)

def create_bar_chart(recommendations_df):
    fig = go.Figure(data=[
        go.Bar(
            x=recommendations_df['title'],
            y=recommendations_df['similarity_score'],
            marker_color=recommendations_df['similarity_score'],
            text=recommendations_df['similarity_score'].round(3),
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title='Top 10 Recommendations',
        xaxis_title='Title',
        yaxis_title='Similarity Score',
        xaxis_tickangle=-45,
        height=500
    )
    
    return fig

def create_network_graph(recommendations_df):
    G = nx.Graph()
    plt.figure(figsize=(12, 8))
    
    # Add nodes
    for _, row in recommendations_df.iterrows():
        G.add_node(row['title'], type=row['type'], score=row['similarity_score'])
    
    # Add edges
    titles = recommendations_df['title'].tolist()
    for i, title1 in enumerate(titles):
        idx1 = df[df['title'] == title1].index[0]
        for j, title2 in enumerate(titles[i+1:], i+1):
            idx2 = df[df['title'] == title2].index[0]
            similarity = cosine_similarity(tfidf_matrix[idx1:idx1+1], 
                                         tfidf_matrix[idx2:idx2+1])[0][0]
            G.add_edge(title1, title2, weight=similarity)
    
    # Visualization
    pos = nx.spring_layout(G, k=1)
    node_colors = ['#FF9999' if G.nodes[node]['type'] == 'Movie' else '#9999FF' 
                  for node in G.nodes()]
    node_sizes = [G.nodes[node]['score'] * 3000 for node in G.nodes()]
    
    nx.draw(G, pos,
           node_color=node_colors,
           node_size=node_sizes,
           with_labels=True,
           font_size=8,
           width=[G[u][v]['weight'] * 2 for u,v in G.edges()],
           alpha=0.7)
    
    plt.title('Recommendation Network')
    return plt.gcf()

def get_recommendations(description):
    recommendations_df = get_hybrid_recommendations(description)
    bar_chart = create_bar_chart(recommendations_df)
    network_graph = create_network_graph(recommendations_df)
    return bar_chart, network_graph

# Create Gradio interface
iface = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(label="Enter movie/series description", lines=3),
    outputs=[
        gr.Plot(label="Top 10 Recommendations"),
        gr.Plot(label="Recommendation Network")
    ],
    title="Netflix Recommendation System",
    description="Enter a description of the content you're interested in to get personalized recommendations.",
    theme="huggingface",
    examples=[
        ["A thrilling action movie with car chases and explosions"],
        ["A romantic comedy about finding love in the city"],
        ["A documentary about nature and wildlife"]
    ]
)

if __name__ == "__main__":
    iface.launch()