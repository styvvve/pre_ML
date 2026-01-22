import pandas as pd
from typing import List, Dict

def stats_df(df: pd.DataFrame) -> pd.DataFrame: 
    #we ll regroup games per year and calculate the mean each year
    games_per_year = df.groupby(["release_year"])

    df_agg = games_per_year.agg({
        'metascore': ['mean', 'median'],
        'userscore': ['mean', 'median'], 
        'metascore_count': ['mean', 'median'], 
        'userscore_count': ['mean', 'median']
    })

    #flatten columns
    df_agg.columns = [
        f"{col}_{stat}" for col, stat in df_agg.columns
    ]

    #add number of games each year
    df_agg["number_of_games"] = games_per_year.size()

    #reset index
    df_agg = df_agg.reset_index()

    #create a decade column
    df_agg["decade"] = (df_agg["release_year"] // 10) * 10

    return df_agg
        