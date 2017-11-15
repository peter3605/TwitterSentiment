import tweepy 
import time
import json
import nltk
import re
import sys
from nltk.corpus import stopwords
from database import Database
import analysis as sa



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
				is_pos,score = sa.import_score(text)
				#mydb.insert_tweet_info(tweet['id'],tweet['user']['id'],tweet['created_at'],text,is_pos,score)
				file = open('data.txt','a')
				file.write(str(score)+'\n')
				file.close()
			


	def on_error(self, status):
		print ('ERROR - '+str(status))


		
#log into twitter api and set up the twitter stream		
def get_twitter_data():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

	streamListener = myListener()
	myStream = tweepy.Stream(auth=api.auth, listener=streamListener)
	myStream.filter(locations = [119.1796875,5.3972734077,127.1337890625,18.9374644296])
		
		
		
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
		
		
		
def main():
	global mydb
	#mydb = Database()
	open("data.txt","w").close()
	#exec(open('graph.py').read())
	get_twitter_data()
	
	
	
if __name__ == '__main__':
	main()
	