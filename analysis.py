import math
import re
 
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
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
	return tokens_re.findall(s)
 
def process_tweet_text(s):
	t = tokenize(s)
	tokens = []
	for token in t:
		tokens.append(token.lower())
	string = " "
	for word in tokens:
		if(word!="rt"):
			if(word.isalpha()):
				string += (word + " ")
	return string
	
	
	
def calculate_sentiment(text):
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
	score = basic_sentiment(pos_words, neg_words)
	if(num>0):
		return ('Y',score)
	if(num==0):
		return ('0',score)
	else:
		return ('N',score)
		
def basic_sentiment(p,n):
	score = math.log10(p+ 0.5)- math.log10(n+0.5)
	return score
	