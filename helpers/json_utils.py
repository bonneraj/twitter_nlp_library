import json

def list_from_json(file_path):
    with open(file_path, 'r') as f:
        list = json.load(f)
    return list
    
def list_to_json(file_path, list):
    with open(file_path, 'w') as f:
        json.dump(list, f)

def api_response_to_list(paginator_object):
    tweet_list = []
    for tweet in paginator_object:
        tweet_list.append(tweet.text)
    return tweet_list