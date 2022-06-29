import tweepy as tw

class GetTweets:
    def __init__(self, BEARER_TOKEN):
        self.BEARER_TOKEN = BEARER_TOKEN

    def search_tweets(self, query, max_results):
        client = self._get_client()
        
        try:
            tweets = client.search_recent_tweets(query=query, max_results=max_results)
            
            tweet_data = tweets.data
            results = []
            
            if tweet_data:
                for tweet in tweet_data:
                    obj = {}
                    results.append(tweet.text)
            if results:
                return results
            else: 
                return [f'Could not retrieve tweets with the given query: {query}']
        except:
            raise RuntimeError(f'"{query}" is not a valid query, refer to the README for example queries and further resources')

    def _get_client(self):
        client = tw.Client(bearer_token = self.BEARER_TOKEN)
        return client