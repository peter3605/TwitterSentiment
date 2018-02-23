import math
import re
import requests
import ast
import json
from string import ascii_letters
import sentiment
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
 
def tokenize(text):
	tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
	return tokens_re.findall(text)
	
 
def process_tweet_text(text):
	t = tokenize(text)
	tokens = []
	for token in t:
		tokens.append(token.lower())

	words = []
	for word in tokens:
		if(word!="rt"):
			if(word.isalpha()):
				words.append(word)
	allowed = set(ascii_letters)
	output = [word for word in words if any(letter in allowed for letter in word)]
	string = ''
	for word in output:
		string += (word + " ")
	return string
	
def sentiment_one(text):
	num = 0
	pos_words = 0;
	neg_words = 0
	for word in text.split():
		poslines = open('words/positive.txt').read().splitlines()
		for line in poslines:
			if(word == line):
				num += 1
				pos_words+=1
		neglines = open('words/negative.txt.').read().splitlines()
		for line in neglines:
			if(word == line):
				num -= 1
				neg_words+=1
	score = math.log10(pos_words+ 0.5)- math.log10(neg_words+0.5)

	is_pos = ""
	if(score>0):
		is_pos = "Y"
	elif(score==0):
		is_pos = "O"
	elif(score<0):
		is_pos = "N"
	return is_pos,score
	
def sentiment_two(text):
	url = ' http://text-processing.com/api/sentiment/'
	dataLoad = {'text':text}
	response = requests.post(url,data = dataLoad)
	result = ast.literal_eval(response.content.decode("utf-8"))
	label = result['label']
	score = result['probability'][label]
	is_pos = 'O'
	if(label == 'neg'):
		score = score * -1
		is_pos = 'N'
	elif(label == 'pos'):
		is_pos = 'Y'
	return is_pos,score
	
def sentiment_three(text):
	num = 0
	pos_words = 0;
	neg_words = 0
	for word in text.split():
		poslines = open('words/positive.txt').read().splitlines()
		for line in poslines:
			if(word == line):
				num += 1
				pos_words+=1
		neglines = open('words/negative.txt.').read().splitlines()
		for line in neglines:
			if(word == line):
				num -= 1
				neg_words+=1
	score = math.log10(pos_words+ 0.5)- math.log10(neg_words+0.5)
	is_pos = sentiment.sentiment(text,'data_sets/positive-50kb.txt','data_sets/negative-50kb.txt')

	if(is_pos == False and score > 0):
		score = score * -1
	elif(is_pos == True and score < 0):
		score = score * -1
	return is_pos,score
