import unittest

from helpers.word_cloud_generator import WordCloudGenerator
from helpers.json_utils import list_from_json

class TestWordCloudGenerator(unittest.TestCase):
    
    def test_get_unique_string(self):     
        list_from_json = TestListToJson()
        word_cloud_generator = WordCloudGenerator()
        unique_string = word_cloud_generator._get_unique_string(list_from_json.clean_tweet_list)

        self.assertTrue(unique_string.startswith('  Any LIV player please win  Congrats on the great work Derek  Guess Who   exactly  You realize the PGA Tour is a US based tour'))
        
class TestListToJson:
    
    def __init__(self):
        self.clean_tweet_list = list_from_json('./tests/test_content/cleaned_tweets.json')
    