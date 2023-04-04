from helpers.json_utils import list_from_json
import logging
from typing import List, Dict
from wordcloud import WordCloud
from collections import Counter

class WordCloudGenerator:
        
    def run_generate_word_cloud_workflow(self, cleaned_output_path: str):
        '''Runs associated analyze sentiment workflow'''
        LOGGER.info('********** run_generate_word_cloud_workflow ******BEGIN******\n')
        # read cleaned tweets json
        cleaned_tweets_list = list_from_json(cleaned_output_path)
        # convert list of tweets to string
        cleaned_tweets_string = self._get_unique_string(cleaned_tweets_list)
        # run word cloud workflow
        word_cloud_object = self._generate_word_cloud(cleaned_tweets_string)
        
        LOGGER.info('********** Exiting run_generate_word_cloud_workflow ******END******\n')
        return word_cloud_object
    
    def _get_unique_string(self, tweet_list):
        unique_string = (" ").join(tweet_list)
        return unique_string
    
    def _get_word_frequencies(self, cleaned_tweet_list: List):
        '''An alternative method to get word cloud (vs. creating a unique string of all tweets)'''
        word_frequency_dict = Counter(cleaned_tweet_list)
        return word_frequency_dict

    def _generate_word_cloud(self, unique_string: dict):
        word_cloud = WordCloud(width = 1000, height = 500).generate(unique_string)
        return word_cloud

LOGGER = logging.getLogger(__name__)