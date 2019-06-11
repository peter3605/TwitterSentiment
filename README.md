# TwitterSentiment

This project reads in live data from Twitter using it's python API called Tweepy. The file twitter_streams.py handles all of the Tweep API calls and stores the data that it reads into either .txt files in the data_sets folder or a SQL local database. 

What I was most interested in doing with this data was creating an algorithm that could analyze the sentiment of each tweet. I used a modified version of the Naive Bayes Classifier and created two sets of words: a list of positive ones, and a list of negative ones(found in the words folder). Using these two lists, I compared the words in the tweet to these two lists to calculate whether or not the overall feeling of the tweet text was positive or negative. The code I used to do these calculations can be found in the sentiment.py file.

I also created a couple of tools to analyze this data. graph_live_results.py can create a graph of real time results of the sentiment analysis and show how positive or negative tweets are currently being. Additionally, I created three different algorithms all of which were slightly different, and analyzied their results while factoring in runtime, data_set size, and accuracy, the results of which can be found in graph_runtime_results.py
