import sentiment
import time
import graph_runtime_results as graph

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

sizes = [10,20,30,40,50,60,70,80,90,100]
accuracy_score = []
computation_time = []

for i in range(0,10):
	size = (i+1)*10
	print(str(size)+" kb")
	
	start_time = time.time()
	
	pos = "data_sets/positive-"+str(size)+"kb.txt"
	neg = "data_sets/negative-"+str(size)+"kb.txt"
	
	score = calculate_accuracy(pos,neg)
	end_time = time.time()
	
	computation_time.append(end_time - start_time)
	accuracy_score.append(score)
	
	print("time - "+str(computation_time[i])+" seconds : accuracy - "+str(accuracy_score[i]))
	print(" ")
	

	
	


