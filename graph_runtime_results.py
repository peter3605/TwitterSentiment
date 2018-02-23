from matplotlib import pyplot as plt
from matplotlib import style

def accuracy_vs_size(x,y):
	style.use('ggplot')

	plt.plot(x,y,linewidth=3)


	plt.title('Accuracy versus Test Data Size')
	plt.ylabel('Accuracy(percentage)')
	plt.xlabel('Test Data Size(in kilobytes)')

	plt.show()

def time_vs_size(x,y):
	style.use('ggplot')

	plt.plot(x,y,linewidth=3)


	plt.title('Time versus Test Data Size')
	plt.ylabel('Time(in seconds)')
	plt.xlabel('Test Data Size(in kilobytes)')

	plt.show()

	
accuracy = [0.5294,0.5714,0.6471,0.6303,0.6218,0.5882]
time = [93.27,260.37,516.11,872.47,1245.8372,1723.1116]
size = [10,20,30,40,50,60]
accuracy_vs_size(size,accuracy)
time_vs_size(size,time)
