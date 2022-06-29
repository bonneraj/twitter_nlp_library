import pandas as pd
from helpers.json_utils import list_from_json
import tabulate

def get_df_from_json(json_path):
    json_list = list_from_json(json_path)
    df = pd.DataFrame.from_records(data=json_list)
    return df

# DOESN'T WORK
def print_dataframe(df):
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
