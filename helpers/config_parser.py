import configparser
import logging
from typing import List, Optional

class ConfigParser():
        
    def run_get_tweet_params_workflow(self, config_file_path: str) -> tuple[List, int]: 
        '''Runs the specified get tweet parameters workflow'''
        config = self._initialize_parser(config_file_path)
        # first query
        first_keyword, first_query, len_query = self._get_query_one(config)
        # second query
        second_keyword, second_query = self._get_query_two(config)

        query_list = []

        # if second_query is None, return write only the first_query to a list obj
        query_list.append([first_query, first_keyword])
        
        if second_query:
            query_list.append([second_query, second_keyword])
        return query_list, len_query

    def _initialize_parser(self, config_file_path: str):
        '''Initializes a ConfigParser object to read config.ini file'''
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config
    
    def _get_query_one(self, config) -> tuple[str, str, int]:
        '''Retrieves the first, mandatory tweet parameters to include: a keyword and the number of tweets to retrieve'''
        keyword = config.get("QUERY 1", "keyword")
        language = config.get("PARAMETERS", "language")
        num_tweets = config.get("PARAMETERS", "num_tweets")

        # validations for config.ini
        if keyword == '':
            raise RuntimeError('Cannot excecute script: config.ini is missing a keyword value for Query 1')
        if language == '':
            raise RuntimeError('Cannot excecute script: config.ini is missing a language value for Query 1')
        if num_tweets == '':
            raise RuntimeError('Cannot excecute script: config.ini is missing a num_tweets value for Query 1')
        
        query = (keyword + ' ' + language)
        return keyword, query, num_tweets
    
    def _get_query_two(self, config) -> Optional[tuple[str, str]]:
        '''Checks for second, optional tweet parameters to include: a keyword and the number of tweets to retrieve'''
        keyword = config.get("QUERY 2", "keyword")
        language = config.get("PARAMETERS", "language") # query 2 will use the same num_tweets parameter as query 1 
        
        # validations for config.ini
        if keyword == '':
            LOGGER.info('WARNING: config.ini is missing a keyword value for Query 2, the script will only be run for Query 1')
            return None, None
        else:
            query = (keyword + ' ' + language)
            return keyword, query

config = ConfigParser()
LOGGER = logging.getLogger(__name__)
config.run_get_tweet_params_workflow('config.ini')