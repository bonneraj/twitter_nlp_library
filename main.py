from sys import argv
import os
from pathlib import Path
from dotenv import load_dotenv
from helpers.get_tweets import GetTweets
from helpers.sentiment_analyzer import SentimentAnalyzer
from helpers.tweet_cleaner import TweetCleaner

def collect_tweets():
    """ This function calls the twitter api and returns the specified query"""
    # assign arguments passed through the command line (bash)
    query = argv[1]
    max_results = argv[2]

    # Get the base directory
    basepath = Path()
    basedir = str(basepath.cwd())

    # Load the environment variables
    envars = basepath.cwd() / '.env'
    load_dotenv(envars)

    # Read environment variables
    BEARER_TOKEN = os.getenv('bearer_token')

    connector = GetTweets(BEARER_TOKEN)
    tweet_list = connector.search_tweets(query, max_results)
    
    return tweet_list

tweet_list = collect_tweets()


cleaner = TweetCleaner(tweet_list)
cleaned_tweets = cleaner.clean_tweets(tweet_list)

analyzer = SentimentAnalyzer(cleaned_tweets)
analysis_output = analyzer.analyze_sentiment(cleaned_tweets)
compound_score_summary = analyzer.summarize_sentiment(analysis_output, 'compound')
negative_score_summary = analyzer.summarize_sentiment(analysis_output, 'neg')
neutral_score_summary = analyzer.summarize_sentiment(analysis_output, 'neu')
positive_score_summary = analyzer.summarize_sentiment(analysis_output, 'pos')

print(f'COMPOUND: {compound_score_summary}\nNEGATIVE: {negative_score_summary}\nNEUTRAL: {neutral_score_summary}\nPOSITIVE: {positive_score_summary}')


