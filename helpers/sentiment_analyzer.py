import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from statistics import mean, median
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self, cleaned_tweet_list):
        self.cleaned_tweet_list = cleaned_tweet_list
        
    def analyze_sentiment(self, cleaned_tweet_list):
        sia = SentimentIntensityAnalyzer()
        sentiment_output_list = []
        for tweet in cleaned_tweet_list:
            sentiment_output_list.append(sia.polarity_scores(tweet))

        return sentiment_output_list

    def summarize_sentiment(self, sentiment_output_list, metric):
        compound_score_list = []
        for output in sentiment_output_list:
            compound_score_list.append(output[metric])
        
        summary_output = []
        mean_score = mean(compound_score_list)
        median_score = median(compound_score_list)
        summary_output.append({'average': mean_score}) 
        summary_output.append({'median': median_score})
        
        return summary_output
