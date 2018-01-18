import analysis
data = open('test_data.txt','r').read()
lines = data.split('\n')

sentiment_one = 0;
sentiment_two = 0;
sentiment_three = 0;

for line in lines:
	end = line.find(":")
	tweet = line[:end]
	score = line[len(line)-1:]
	
	is_pos1, num1 = analysis.sentiment_one(str(tweet))
	if(is_pos1 == score):
		sentiment_one += 1
	
	is_pos2, num2 = analysis.sentiment_two(str(tweet))
	if(is_pos2 == score):
		sentiment_two += 1
	"""	
	is_pos3, num3 = analysis.sentiment_three(tweet)
	if(is_pos3 == score):
		sentiment_three += 1"""

size = len(lines)

score1 = sentiment_one/size
score2 = sentiment_two/size
score3 = sentiment_three/size

print(score1)
print(score2)
print(score3)