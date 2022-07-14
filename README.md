# Twitter Sentiment Analysis

## Project Overview: 
This project utilizes the Twitter API to search tweets based on user-provided criteria and provide a summary of text sentiment. The search query is limited to tweets from the past seven days, based on developer account permitted use. 

## Getting Started:
1. create a '.env' file in the main directory
    1. create a BEARER_TOKEN variable with your associated bearer token from twitter dev account
    2. Template: BEARER_TOKEN=''
        1. Note - .env requires line 2 to be a whitespace line
2. In a bash terminal run 'source ./setup.sh' to install all dependencies

# Running the Script with a Custom Query: 
1. edit the parameters in config.ini to specify the tweet parameters for one or two queries
    1. The 'keyword' for QUERY 1 is required - this value can be a word, a hashtag or a longer phrase
        1. Values should not include quotes (single or double)
    2. The 'keyword' for QUERY 2 is optional - if not specified, the script will only run the first keyword query
    3. the 'language' for PARAMETERS only supports english at this time (lang:en) and will be used for all queries
    4. the 'num_tweets' for PARAMETERS is the number of tweets you would like to retrieve for each query, this is used for all queries
    5. Be sure to save config.ini (see below for example configuration)
2. in a bash terminal run: python main.py

# Example config.ini Inputs:
[QUERY 1]

keyword = #LIVTour

[QUERY 2]

keyword = #PGATour

[PARAMETERS]

language = lang:en

num_tweets = 1000