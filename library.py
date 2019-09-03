#tweepy needs to be installed on the Swisscom Cloud too
import tweepy
#twitter developer account needed for the following access data:
consumer_key="ykQSj0nnBrDp260MqSTWT1w6J"
consumer_secret="QNd8CMxrPumYuAqTMwrNkYOZUL5A5Ey7IbWklNZHNXpDLVmfm6"
access_token="59456756-HcBJFxen8u3CuNqUQ1PzQs0BaIBKI495FDXDHrXs7"
access_token_secret="ozHyxTh23Oq1LOz95Y7H7jhiFncYFW54MZ7pt1SQV4otW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #logs into Bryan's twitter developer account @gigerbytes
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def create_tweet(tweet):
    global api
    api.update_status(status=tweet) #sends the latest logged 50 characters as a tweet