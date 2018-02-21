from matplotlib import pyplot as plt
from matplotlib import style

def accuracy_vs_size():
	style.use('ggplot')

	x = [0,1,2,3]
	y = [6,9,3,4]

	plt.plot(x,y,linewidth=5)


	plt.title('Accuracy versus Test Data Size')
	plt.ylabel('Accuracy(percentage)')
	plt.xlabel('Test Data Size(in kilobytes)')

	plt.show()

def time_vs_size():
	style.use('ggplot')

	x = [0,1,2,3]
	y = [8,8,8,8]

	plt.plot(x,y,linewidth=5)


	plt.title('Time versus Test Data Size')
	plt.ylabel('Time(in seconds)')
	plt.xlabel('Test Data Size(in kilobytes)')

	plt.show()

def accuracy_vs_time():
	style.use('ggplot')

	x = [0,1,2,3]
	y = [5,4,3,2]

	plt.plot(x,y,linewidth=5)


	plt.title('Accuracy versus Time')
	plt.ylabel('Accuracy(percentage)')
	plt.xlabel('time(in seconds)')

	plt.show()
	
accuracy_vs_size()
time_vs_size()
accuracy_vs_time()