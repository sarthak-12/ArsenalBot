import tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_key_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
search_key = 'Arsenal' #keywords to be searched
num = 5  #number of tweets to be searched
for tweet in tweepy.Cursor(api.search , search_key).items(num):
	try:
		tweet.favorite()
		print('Liked that tweet.')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
