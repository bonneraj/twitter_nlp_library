import pandas as pd
from helpers.json_utils import list_from_json

def get_df_from_json(json_path: str) -> pd.DataFrame:
    '''Reads collected tweets from .json and returns a Pandas DataFrame'''
    
    json_list = list_from_json(json_path)
    df = pd.DataFrame.from_records(data=json_list)
    return df