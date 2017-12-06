import pickle
import nltk

pos_tweets = []
with open("words/positive_tweets.txt", "rb") as myFile:
    pos_tweets = pickle.load(myFile)
neg_tweets = []
with open("words/negative_tweets.txt", "rb") as myFile:
    neg_tweets = pickle.load(myFile)
			  
			  
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words	
word_features = get_word_features(get_words_in_tweets(tweets))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
	
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'Your song is annoying'
print (classifier.classify(extract_features(tweet.split())))


