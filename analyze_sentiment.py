import os
import re
from pathlib import Path
from dotenv import load_dotenv
from helpers.get_tweets_with_bearer import GetTweets
from helpers.sentiment_analyzer import SentimentAnalyzer
from helpers.tweet_cleaner import TweetCleaner
from helpers.sentiment_visualizer import SentimentVisualizer
from helpers.config_parser import ConfigParser
from helpers.logger import logger

def get_tweet_params(config_file_path: str):
    parser = ConfigParser()
    query_list, max_results = parser.run_get_tweet_params_workflow(config_file_path)
    
    return query_list, max_results
    
def collect_tweets(tweet_output_file_path: str, query: str, max_results: int):
    '''This function collects user-specified arguments from config.ini and collects specified number of tweets based on keyword'''
    # Get the base directory
    basepath = Path()

    # create parent directory for .json output if it doesn't already exist
    output_parent_dir = tweet_output_file_path.split('/')[0]
    output_parent_dir = output_parent_dir + '/'
    if not os.path.exists(output_parent_dir):
        os.makedirs(output_parent_dir)

    # Load the environment variables
    envars = basepath.cwd() / '.env'
    load_dotenv(envars)

    # Read environment variables
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    client = GetTweets(BEARER_TOKEN)
    client.run_get_tweets_workflow(query, max_results, tweet_output_file_path)

def clean_tweets(raw_file_path: str, cleaned_file_path: str):
    cleaner = TweetCleaner()
    cleaner.run_clean_tweets_workflow(raw_file_path, cleaned_file_path)

def get_tweet_sentiment(cleaned_file_path: str, sentiment_summary_file_path: str, keyword: str):
    analyzer = SentimentAnalyzer()
    analyzer.run_analyze_sentiment_workflow(cleaned_file_path, sentiment_summary_file_path, keyword)

def visualize_tweet_sentiment(sentiment_summary_file_path: str, keyword: str):
    visualizer = SentimentVisualizer()
    visualizer.plot_standalone_bar_graph(sentiment_summary_file_path, keyword)
    
def main():
    # for loop to run all workflows for one or more search queries
    LOGGER = logger()
    LOGGER.info('********** Entering main() ******BEGIN******\n')
    config_file_path = 'config.ini'
    query_list, max_results = get_tweet_params(config_file_path)
    
    for query in query_list:
        # clean keyword to be used in file names
        keyword = query[1]
        keyword = str(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", keyword))
        keyword = keyword.replace(" ", "_")

        # specify query-specific file paths
        tweet_output_file_path = (f'output/raw_tweets_{keyword}.json')
        cleaned_tweet_output_file_path = (f'output/clean_tweets_{keyword}.json')
        sentiment_summary_file_path = (f'output/sentiment_summary_{keyword}.json')

        collect_tweets(tweet_output_file_path, keyword, max_results)
        clean_tweets(tweet_output_file_path, cleaned_tweet_output_file_path)
        get_tweet_sentiment(cleaned_tweet_output_file_path, sentiment_summary_file_path, keyword)
        visualize_tweet_sentiment(sentiment_summary_file_path, keyword)

    LOGGER.info('********** Exiting main() ******END******\n')


if __name__ == "__main__":
    main()
