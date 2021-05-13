import PySimpleGUI as sg
import threading
import tweepy
from time import sleep

consumer_key = "9ccnYG7eb6iwILKRctdqC5Lma"
consumer_secret = "lG0uIovSGaVyblaVrB2XrcsWXBWyOJ74aii5VlYF5YLdwx6G5u"
access_token = "1344057502502150145-bujfPnvQaSQD4hO2PZfKydMznenzSY"
access_token_secret = "YWwv9YjTsYRYjwIBKRUwbZhkyWYk0gzcuTru2gOSpoVHG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def retweet(word):
	numberOfTweets = 10000
	for tweet in tweepy.Cursor(api.search, word).items(numberOfTweets):
		try:
			tweet.retweet()
			tweet.favorite()
			print('Retweeted and liked this tweet')
			sleep(5)
		except tweepy.TweepError as ex:
			print(ex.reason)
		except StopIteration:
		 	break

def home():
	sg.theme('DarkGrey13')
	layout = [
		[sg.Text('Twitter Bot', size=(10, 1))],
		[sg.Text('Word to search:')],
		[sg.Input(key='word')],
		[sg.Button("Confirm")],
		[sg.Output(size=(30, 5))],
		[sg.Button('Help'), sg.Exit()]
		]
	return sg.Window('Control', layout, element_justification='c', finalize=True)

def help():
	sg.theme('DarkGrey13')
	layout = [
		[sg.Text('If you see any issue, you can report at:')],
		[sg.Text('https://github.com/felipe2102/twitter-bot/issues/new')],
		[sg.Button('Return')]
	]
	return sg.Window('Help', layout, element_justification='c', finalize=True)

index, ajuda = home(), None

if __name__ == '__main__':
	while True:
		window, event, values = sg.read_all_windows()
		if window == index and event == sg.WIN_CLOSED or event == 'Exit':
			break
		if window == index and event == 'Help':
			ajuda = help()
			index.hide()
		if window == ajuda and event == 'Return':
			index.un_hide()
			ajuda.hide()
		if window == index and event == 'Confirm':
			search = values['word']
			threading.Thread(target=retweet, args=(search,), daemon=True).start()