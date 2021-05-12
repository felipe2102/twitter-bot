import tweepy
from time import sleep

consumer_key = "9ccnYG7eb6iwILKRctdqC5Lma"
consumer_secret = "lG0uIovSGaVyblaVrB2XrcsWXBWyOJ74aii5VlYF5YLdwx6G5u"
access_token = "1344057502502150145-bujfPnvQaSQD4hO2PZfKydMznenzSY"
access_token_secret = "YWwv9YjTsYRYjwIBKRUwbZhkyWYk0gzcuTru2gOSpoVHG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def re():
	search = "#goza"
	search2 = "#goza"
	numberOfTweets = 10000
	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
		try:
			tweet.retweet()
			tweet.favorite()
			print('Retweeted and liked this tweet')
			sleep(5)
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
		 	break
	for tweet in tweepy.Cursor(api.search, search2).items(numberOfTweets):
		try:
			tweet.retweet()
			tweet.favorite()
			print('Retweeted and liked this tweet')
			sleep(5)
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
		 	break

re()
