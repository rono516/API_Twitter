from textblob import TextBlob
import tweepy
import sys

api_key = "1INSA5zlzR1mBpEwwaGNICHPI"
api_key_secret = "tnbv7zw0LvLL2qiV1IHdztQIsdm80Z3HI6vmuLOomPZTJBrrte"
access_token = "1175064453743828992-hoTX48Iy5vsjsUqu6wYbTiJQ4qjJfD"
access_token_secret = "dytyZ2wdrGYuqbhWxpTLI6mkvFyptoAYhCRxBM41S2Bpv"

auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret= api_key_secret)

auth_handler.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler)

search_term = 'sad'
tweet_amount = 10

tweets = tweepy.Cursor(api.search, q=search_term, lang= 'en').items(tweet_amount)
polarity = 0

positive = 0
neutral = 0
negative = 0

for tweet in tweets:
    #print(tweet.text) #this gives us tweets including hashtags and
    # irrelevant content we do not need and so we need to clean tweets
    #we receive from twitter
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
        #print(final_text) #prints our cleaned texts

        #We are ready to do sentiment analysis of our tweets
        analysis = TextBlob(final_text)
        tweet_polarity = analysis.polarity
        if tweet_polarity > 0:
            positive +=1
        elif tweet_polarity < 0:
            negative +=1
        else:
            neutral +=1
        polarity += tweet_polarity
        print(final_text)
print(polarity)
print(f'amount of positive tweets: {positive}')
print(f'amount of negative tweets: {negative}')
print(f'amount of neutral tweets: {neutral}')



