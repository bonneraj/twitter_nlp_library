import re
from helpers.json_utils import list_to_json, list_from_json

class TweetCleaner:

    def run_clean_tweets_workflow(self, raw_output_path, cleaned_output_path):
        # read tweets json
        raw_tweets_list = list_from_json(raw_output_path)
        # clean tweets
        cleaned_tweets_list = self._clean_tweets(raw_tweets_list)
        # save list as json
        list_to_json(cleaned_output_path, cleaned_tweets_list)
    
    def _clean_tweets(self, tweet_list):
        # remove non alpha-numeric characters
        cleaned_tweets = []
        for tweet in tweet_list:
            tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet)
            tweet = re.sub(' +', ' ', tweet)
            cleaned_tweets.append(tweet)
        return cleaned_tweets