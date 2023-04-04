import os
import re
from pathlib import Path
from dotenv import load_dotenv
from helpers.get_tweets_with_bearer import GetTweets
from helpers.tweet_cleaner import TweetCleaner
from helpers.word_cloud_generator import WordCloudGenerator
from helpers.word_cloud_visualizer import WordCloudVisualizer
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

def generate_word_cloud(cleaned_file_path: str):
    word_cloud_generator = WordCloudGenerator()
    word_cloud_object = word_cloud_generator.run_generate_word_cloud_workflow(cleaned_file_path)
    return word_cloud_object

def visualize_word_cloud(word_cloud_object, world_cloud_file_path: str):
    word_cloud_visualizer = WordCloudVisualizer()
    word_cloud_visualizer.plot_standalone_bar_graph(word_cloud_object, world_cloud_file_path)

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
        world_cloud_file_path = (f'output/word_cloud_{keyword}.json')

        collect_tweets(tweet_output_file_path, keyword, max_results)
        clean_tweets(tweet_output_file_path, cleaned_tweet_output_file_path)
        word_cloud_object = generate_word_cloud(cleaned_tweet_output_file_path)
        visualize_word_cloud(word_cloud_object, world_cloud_file_path)

    LOGGER.info('********** Exiting main() ******END******\n')


if __name__ == "__main__":
    main()
