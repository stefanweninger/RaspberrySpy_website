import tweepy

consumer_key="ykQSj0nnBrDp260MqSTWT1w6J"
consumer_secret="QNd8CMxrPumYuAqTMwrNkYOZUL5A5Ey7IbWklNZHNXpDLVmfm6"
access_token="59456756-HcBJFxen8u3CuNqUQ1PzQs0BaIBKI495FDXDHrXs7"
access_token_secret="ozHyxTh23Oq1LOz95Y7H7jhiFncYFW54MZ7pt1SQV4otW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.mentions_timeline()
for tweet in public_tweets:
    print(tweet.text)

#api.update_status(status="hey Im a bot")

def create_tweet(tweet):
    global api
    api.update_status(status=tweet)
