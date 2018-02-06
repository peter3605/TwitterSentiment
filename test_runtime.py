import sentiment
import time

def calculate_accuracy(pos_data_set,neg_data_set):
	data = open('data_sets/test_data.txt','r').read()
	lines = data.split('\n')

	sentiment_score = 0;

	for line in lines:
		if(line == ""):
			print("")
		else:
			end = line.find(":")
			tweet = line[:end]
			score = line[len(line)-1:]

			is_pos = sentiment.sentiment(tweet,pos_data_set,neg_data_set)
			if(is_pos == "positive"):
				is_pos = "Y"
			else:
				is_pos = "N"
			if(is_pos == score):
				sentiment_score += 1
			

	size = len(lines)-1

	final_score = sentiment_score/size
	return final_score


accuracy_score = []
computation_time = []
positive_data_sets = ["data_sets/positive-10kb.txt","data_sets/positive-20kb.txt","data_sets/positive-30kb.txt","data_sets/positive-40kb.txt","data_sets/positive-50kb.txt"]
negative_data_sets = ["data_sets/negative-10kb.txt","data_sets/negative-20kb.txt","data_sets/negative-30kb.txt","data_sets/negative-40kb.txt","data_sets/negative-50kb.txt"]

for i in range(0,len(positive_data_sets)-1):
	print(i)
	start_time = time.time()
	score = calculate_accuracy(positive_data_sets[i],negative_data_sets[i])
	end_time = time.time()
	
	computation_time.append(end_time - start_time)
	accuracy_score.append(score)
	
	print("time - "+str(computation_time[i])+" seconds : score - "+str(accuracy_score[i]))
	print("")
	
	


