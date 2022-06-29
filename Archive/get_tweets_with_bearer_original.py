'''Updated in more recent release - this script submits a url request instead or utilizing built in tweepy functions with pagination'''

import requests 
import os
from pathlib import Path
import json
from dotenv import load_dotenv

def retrive_bearer_token():
    # Get the base directory
    basepath = Path()
    basedir = str(basepath.cwd())

    # Load the environment variables
    envars = basepath.cwd() / '.env'
    load_dotenv(envars)

    # Read environment variables
    BEARER_TOKEN = os.getenv('bearer_token')
    print(BEARER_TOKEN)
    return BEARER_TOKEN

def create_header(bearer_token):
    header = {"Authorization": f'Bearer {bearer_token}'}
    return header

def create_url(keyword, max_results=10):
    # api for retrieving tweets in the past seven days 
    search_url = "https://api.twitter.com/2/tweets/search/recent"

    # set query parameters
    query_params = {'query': keyword,
                    'tweet.fields': 'text',
                    'max_results': max_results,
                    'next_token': {}
    }
    return (search_url, query_params)

def send_response(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    bearer_token = retrive_bearer_token()
    header = create_header(bearer_token)
    keyword =  '#LIVTour lang:en'
    max_results = 1000
    url = create_url(keyword, max_results)
    json_response = send_response(url[0], header, url[1])
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    # print(json_response['data'][0]['created_at'])
    # print(json_response['meta']['result_count'])

    # if 'next_token' in   n_response['meta']['next_token']

    with open('output/data.json', 'w') as f:
        json.dump(json_response, f)

if __name__ == "__main__":
    main()
