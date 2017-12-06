import tweepy 
import time
import json
import nltk
import re
import sys
import analysis as sa
import pickle
from nltk.corpus import stopwords
from database import Database
from http.client import IncompleteRead
from datetime import datetime



#consumer key, consumer secret, access token, access secret.
consumer_key="LNQrdS2U0HLL5J0y6MPEVCOkl"
consumer_secret="47B9ZiHXgPWCg2nyGjWQXbLULHIqEJVOVcAGK59ahLdtXm2N05"
access_token="2827582612-YqwOL4w56tc4DApnvqbviiMTMGP1hKHoU3wgWTo"
access_token_secret="HOHTtdWQqBhMAXfzGT12ci23YtX1uwjr4U0PKbjqgyumK"

#on_data is called for every data set that comes through the twitter stream
class myListener(tweepy.StreamListener):
	def on_data(self, data):
		tweet = json.loads(data)
		if 'text' in tweet:
			text = sa.process_tweet_text(tweet['text'])
			language = calculate_languages_ratios(text)
			#add tweet to database
			if(language):
				#get sentiment score
				is_pos,score = sa.import_score(text)
				
				add_tweet_to_list(text,is_pos)
				
				#insert tweet info into database
				mydb.insert_tweet_info(tweet['id'],tweet['user']['id'],tweet['created_at'],text,is_pos,score,key)
				
				#insert sentiment score into data.txt
				file = open('data.txt','a')
				file.write(str(score)+'\n')
				file.close()
			


	def on_error(self, status):
		print ('ERROR - '+str(status))

def add_tweet_to_list(text,is_pos):
	if(is_pos == 'Y'):
		pos_tweets = []
		with open("words/positive_tweets.txt", "rb") as myFile:
			pos_tweets = pickle.load(myFile)
		pos_tweets.append((text,'positive'))	
		with open("words/positive_tweets.txt", "wb") as myFile:
			pickle.dump(pos_tweets, myFile)
	elif(is_pos == 'N'):
		neg_tweets = []
		with open("words/negative_tweets.txt", "rb") as myFile:
			neg_tweets = pickle.load(myFile)
		neg_tweets.append((text,'negative'))
		with open("words/negative_tweets.txt", "wb") as myFile:
			pickle.dump(neg_tweets, myFile)
		
#log into twitter api and set up the twitter stream		
def get_twitter_data(keyword):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

	streamListener = myListener()
	myStream = tweepy.Stream(auth=api.auth, listener=streamListener)
	myStream.filter(track = keyword)
		
		
#returns which ever language makes up the largest ratio of the text parameter
def calculate_languages_ratios(text):
	languages_ratios = {}
	
	tokens = nltk.wordpunct_tokenize(text)
	words = [word.lower() for word in tokens]

	for language in stopwords.fileids():
		stopwords_set = set(stopwords.words(language))
		words_set = set(words)
		common_elements = words_set.intersection(stopwords_set)

		languages_ratios[language] = len(common_elements) # language "score"
	isEnglish = False
	if(max(languages_ratios, key=languages_ratios.get)=='english'):
		for lang in languages_ratios:
			if(lang!='english'):
				if(languages_ratios[lang]==languages_ratios['english']):
					isEnglish = False
				else:
					if((languages_ratios['english']-languages_ratios[lang])>1):
						isEnglish = False
		isEnglish = True
	else:
		isEnglish = False
	return isEnglish
		
		
		
def main(keyword):
	#create a string of all the search terms
	global key 
	key = ""
	for k in keyword:
		key += (k+", ")
	key = key[:len(key)-2]
	
	#add the search terms to the first line of data.txt
	open("data.txt","w").close()
	file = open('data.txt','a')
	file.write(str(datetime.now())+"\n")
	file.write(key+'\n')
	file.close()
	
	#connect to database
	global mydb
	mydb = Database()
	
	#stream tweets
	get_twitter_data(keyword)
	
	
if __name__ == '__main__':
	#get all of the arguments as search terms
	args = []
	for arg in sys.argv:
		if(arg.isalnum()):
			args.append(arg)
	main(args)
	