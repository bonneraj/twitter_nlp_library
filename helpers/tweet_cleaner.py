import re
from helpers.json_utils import list_to_json, list_from_json
from typing import List

class TweetCleaner:

    def run_clean_tweets_workflow(self, raw_output_path: str, cleaned_output_path: str):
        '''Runs clean tweets workflow'''
        # read tweets json
        raw_tweets_list = list_from_json(raw_output_path)
        # clean tweets
        cleaned_tweets_list = self._clean_tweets(raw_tweets_list)
        unique_cleaned_tweets = self._remove_duplicate_tweets(cleaned_tweets_list)
        # save list as json
        list_to_json(cleaned_output_path, unique_cleaned_tweets)
    
    def _clean_tweets(self, tweet_list: List) -> List:
        '''Cleans tweets by stripping extraneous characters'''
        # remove non alpha-numeric characters
        cleaned_tweets = []
        for tweet in tweet_list:
            tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet)
            tweet = re.sub(' +', ' ', tweet)
            cleaned_tweets.append(tweet)
        return cleaned_tweets

    def _remove_duplicate_tweets(self, tweet_list: List) -> List:
        '''Get a list of unique tweets'''
        unique_tweets = set(tweet_list)
        unique_tweet_list = list(unique_tweets)
        return unique_tweet_list