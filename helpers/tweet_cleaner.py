import re

class TweetCleaner:
    def __init__(self, tweet_list):
        self.tweet_list = tweet_list

    def clean_tweets(self, tweet_list):
        cleaned_tweets = []
        # remove non alpha-numeric characters
        for tweet in tweet_list:
            tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet)
            tweet = re.sub(' +', ' ', tweet)
            cleaned_tweets.append(tweet)
        
        return cleaned_tweets
