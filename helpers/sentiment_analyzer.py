import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from statistics import mean, median
nltk.download('vader_lexicon')
from helpers.json_utils import list_from_json, list_to_json
from tabulate import tabulate
from helpers.dataframe_utils import get_df_from_json
import logging
from typing import List, Dict

class SentimentAnalyzer:
        
    def run_analyze_sentiment_workflow(self, cleaned_output_path: str, sentiment_output_path: str, keyword: str):
        '''Runs associated analyze sentiment workflow'''
        LOGGER.info('********** Entering run_analyze_sentiment_workflow() ******BEGIN******\n')
        # read cleaned tweets json
        cleaned_tweets_list = list_from_json(cleaned_output_path)
        # run sentiment workflow
        sentiment_output = self._analyze_sentiment(cleaned_tweets_list)
        sentiment_summary = self._summarize_sentiment(sentiment_output, keyword)
        list_to_json(sentiment_output_path, sentiment_summary)
        # print out results
        sentiment_output_df = get_df_from_json(sentiment_output_path)
        print(f"\n******Tweet Keyword: {keyword}******\n{tabulate(sentiment_output_df, headers='keys', tablefmt='fancy_grid')}\n")
        LOGGER.info('********** Exiting run_analyze_sentiment_workflow() ******END******\n')
    
    def _analyze_sentiment(self, cleaned_tweet_list: List) -> List:
        ''''Score tweets using SentimentIntensityAnalyzer from NLTK'''
        sia = SentimentIntensityAnalyzer()
        sentiment_output_list = []
        for tweet in cleaned_tweet_list:
            sentiment_output_list.append(sia.polarity_scores(tweet))
        return sentiment_output_list

    def _summarize_sentiment(self, sentiment_output_list: str, keyword: str) -> Dict:
        '''Calculate summary of descriptive statistics for scored sentiments across entire query'''
        metric_list = ['compound', 'neg', 'neu', 'pos']
        summary_output = []
        for metric in metric_list:
            metric_scores = []
            for record in sentiment_output_list: 
                metric_scores.append(record[metric])
            mean_score = mean(metric_scores)
            median_score = median(metric_scores)
            summary_output.append({'metric': metric,'mean': mean_score, 'median': median_score, 'keyword': keyword}) 

        return summary_output

LOGGER = logging.getLogger(__name__)