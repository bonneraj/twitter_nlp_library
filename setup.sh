# !/bin/sh


# install dependencies
pip install python-dotenv
pip install tweepy
pip install textblob
python -m textblob.download_corpora
pip install nltk