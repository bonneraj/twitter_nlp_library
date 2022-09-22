import json
from typing import List

def list_from_json(file_path: str) -> List:
    '''Reads JSON records and returns a list'''
    with open(file_path, 'r') as f:
        list = json.load(f)
    return list
    
def list_to_json(file_path: str, list: List):
    '''Dumps items from a list into JSON'''
    with open(file_path, 'w') as f:
        json.dump(list, f)

def api_response_to_list(paginator_object) -> List:
    '''Gets tweet text returned from API response and puts into a list'''
    tweet_list = []
    for tweet in paginator_object:
        tweet_list.append(tweet.text)
    return tweet_list