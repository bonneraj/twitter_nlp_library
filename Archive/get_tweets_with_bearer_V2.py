import requests 
import os
from pathlib import Path
import json
from dotenv import load_dotenv
import tweepy as tw

class GetTweets:
    def __init__(self, BEARER_TOKEN):
        self.BEARER_TOKEN = BEARER_TOKEN

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

    def create_client(bearer_token):
        client = tw.Client(bearer_token)
        return client

    def get_tweets_list(client, query, num_tweets):
        tweets = tw.Paginator(client.search_recent_tweets, query=query, tweet_fields='text', max_results=100).flatten(limit=num_tweets)
        results = []

        for tweet in tweets:
            results.append(tweet.text)
        return results

    def save_tweets_as_json(file_path, tweet_list):
        with open(file_path, 'w') as f:
            json.dump(tweet_list, f)

    def main():
        bearer_token = retrive_bearer_token()
        client = create_client(bearer_token)
        query =  '#LIVTour lang:en'
        max_results = 100
        tweets_list = get_tweets_list(client, query, num_tweets=200)
        
        save_tweets_as_json('output/data.json', tweets_list)