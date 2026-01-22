from typing import List, Dict
import pandas as pd

def features(list: List[Dict], csv_path: str) -> pd.DataFrame: 
    dataframe = pd.DataFrame(list)

    dataframe.to_csv(csv_path, index=False)

    return dataframe