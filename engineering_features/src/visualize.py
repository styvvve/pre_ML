import matplotlib.pyplot as plt
from typing import Dict, List
import pandas as pd
import numpy as np

def visualize(df_year: pd.DataFrame):
    #1- evolution of metascore's mean
    plt.figure()
    plt.plot(df_year["release_year"].values, df_year["metascore_mean"].values)
    plt.title("Evolution of metascore's mean")
    plt.xlabel("Year")
    plt.ylabel("Metascore's means")
    plt.savefig("/Users/steve/Documents/pre-ML/engineering_features/output/evolution-of-metascore-means.png", dpi=300)
    plt.close()

    #2 - comparison decade between decade
    df_decade = df_year.groupby("decade").agg({
        'metascore_mean': 'mean', 
        'userscore_mean': 'mean', 
        'metascore_median': 'median', 
        'userscore_median': 'median', 
        'number_of_games': 'sum'
    }).reset_index()
    
    plt.figure()
    plt.bar(df_decade["decade"].values, df_decade["metascore_mean"].values)
    plt.title("Comparison decade between decade")
    plt.xlabel("Decade")
    plt.ylabel("Metascore's means")
    plt.savefig("/Users/steve/Documents/pre-ML/engineering_features/output/comparison-decade-between-decade.png", dpi=300)
    plt.close()

    #3- Frequency of metascore's mean
    plt.figure()
    plt.hist(df_year["metascore_mean"].values, bins=10, range=(40, 100), rwidth=0.9)
    plt.title("Frequency of metascore's mean")
    plt.xlabel("Metascore's mean")
    plt.ylabel("Frequency")
    plt.savefig("/Users/steve/Documents/pre-ML/engineering_features/output/frequency-of-metascore-mean.png", dpi=300)
    plt.close()
    