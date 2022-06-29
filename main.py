from sys import argv
import os
from pathlib import Path
from dotenv import load_dotenv
from helpers.get_tweets_with_bearer import GetTweets
from helpers.tweets_json_functions import list_from_json, list_to_json
from helpers.sentiment_analyzer import SentimentAnalyzer
from helpers.tweet_cleaner import TweetCleaner

def collect_tweets(tweet_output_file_path):
    """ This function collects user-specified arguments from the command line and runs\n
    """
    # assign arguments passed through the command line (bash)
    query = argv[1]
    max_results = argv[2]

    # Get the base directory
    basepath = Path()

    # Load the environment variables
    envars = basepath.cwd() / '.env'
    load_dotenv(envars)

    # Read environment variables
    BEARER_TOKEN = os.getenv('bearer_token')

    client = GetTweets(BEARER_TOKEN)
    client.run_get_tweets_workflow(query, max_results, tweet_output_file_path)

def clean_tweets(raw_file_path, cleaned_file_path):
    cleaner = TweetCleaner()
    cleaner.run_clean_tweets_workflow(raw_file_path, cleaned_file_path)

def get_tweet_sentiment(cleaned_file_path, sentiment_summary_file_path):
    analyzer = SentimentAnalyzer()
    analyzer.run_analyze_sentiment_workflow(cleaned_file_path, sentiment_summary_file_path)
    
def main():
    tweet_output_file_path = 'output/raw_tweets.json'
    cleaned_tweet_output_file_path = 'output/clean_tweets.json'
    sentiment_summary_file_path = 'output/sentiment_summary.json'
    collect_tweets(tweet_output_file_path)
    clean_tweets(tweet_output_file_path, cleaned_tweet_output_file_path)
    get_tweet_sentiment(cleaned_tweet_output_file_path, sentiment_summary_file_path)

if __name__ == "__main__":
    main()