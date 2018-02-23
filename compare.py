import analysis
data = open('data_sets/test_data.txt','r').read()
lines = data.split('\n')

sentiment_one = 0;
sentiment_two = 0;
sentiment_three = 0;

for line in lines:
	if(line == ""):
		print("")
	else:
		end = line.find(":")
		tweet = line[:end]
		score = line[len(line)-1:]
		
		is_pos1, num1 = analysis.sentiment_one(str(tweet))
		if(is_pos1 == score):
			sentiment_one += 1
		
		
		is_pos2, num2 = analysis.sentiment_two(str(tweet))
		if(is_pos2 == score):
			sentiment_two += 1

		
		is_pos3, num3 = analysis.sentiment_three(str(tweet))
		if(is_pos3 == "positive"):
			is_pos3 = "Y"
		else:
			is_pos3 = "N"
		if(is_pos3 == score):
			sentiment_three += 1
		

size = len(lines)-1

score1 = sentiment_one/size
score2 = sentiment_two/size
score3 = sentiment_three/size

print("sentiment one score: "+ str(score1))
print("sentiment two score: "+ str(score2))
print("sentiment three score: "+ str(score3))