# Twitter Sentiment Analysis

## Project Overview: 
This project utilizes the Twitter API to search tweets based on user-provided criteria and provide a summary of text sentiment. The search query is limited to tweets from the past seven days, based on developer account permitted use. 

## Getting Started
1. create a '.env' file in the main directory
  1. create a BEARER_TOKEN variable with your associated bearer token from twitter dev account
  2. Template: BEARER_TOKEN=''
    1. Note - .env requires line 2 to be a whitespace line
2. In a bash terminal run 'source ./setup.sh' to install all dependencies

# Running the script with a custom query 
1. in a bash terminal run: python main.py <'search_query'> <num_tweets>
  1. see https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query for further information on building a search query