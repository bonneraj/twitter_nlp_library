import requests 
import os
from pathlib import Path
import json
import tweepy as tw
from helpers.json_utils import list_to_json,api_response_to_list
from typing import List

class GetTweets:
    def __init__(self, BEARER_TOKEN):
        self.BEARER_TOKEN = BEARER_TOKEN

    def run_get_tweets_workflow(self, query, num_tweets, file_path):
        '''Runs associated get tweets workflow'''
        client = self._create_client()
        api_response = self._get_tweets_list(client, query, num_tweets)
        tweet_list = api_response_to_list(api_response)
        list_to_json(file_path, tweet_list)
            
    def _create_client(self) -> str:
        '''Returns client session for API call'''
        client = tw.Client(self.BEARER_TOKEN)
        return client

    def _get_tweets_list(self, client: str, query: str, num_tweets: int) -> List:
        '''Submits specified headers to Twitter API'''
        tweets = tw.Paginator(client.search_recent_tweets, query=query, tweet_fields='text', max_results=100).flatten(limit=int(num_tweets))
        return tweets
