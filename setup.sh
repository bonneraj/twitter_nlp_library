# !/bin/sh


# install dependencies
pip install requests
pip install requests-oauthlib
pip install python-dotenv
python -m pip install python-dotenv
pip install tweepy
pip install textblob
python -m textblob.download_corpora
pip install nltk
pip install seaborn
pip install pandas
pip install tabulate
python -m pip install pytest
pip install pytest-cov
pip install mypy
pip install wordcloud
pip install matplotlib

# print options
echo ' -RUN TEST QUERY: python main.py'
echo ' - TEST: python -m pytest'
echo ' - COVERAGE: python -m pytest --cov=src'