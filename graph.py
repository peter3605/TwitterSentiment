import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

if __name__ == '__main__':
	style.use('ggplot')

	fig = plt.figure()
	fig.canvas.set_window_title('Graph')
	fig.set_size_inches(9, 8, forward=True)
	graph_data = open('data.txt','r').read()
	fig.suptitle(" ")
	ax = fig.add_subplot(1,1,1)
	ax.set_yticks([-20,0,20])
	ax.set_xticks([])
			
	def animate(i):
		graph_data = open('data.txt','r').read()
		lines = graph_data.split('\n')
		xs = []
		ys = []
		x=0
		total = 0
		for line in lines:
			if(x>=2):
				try:
					total += int(line)
				except:
					continue
				fig.suptitle("start time: "+lines[0]+"\n"+"search terms: "+lines[1]+"\n"+"number of tweets: "+str(x-1)+"\n"+"average sentiment score: "+str(format((total/x),".4f")))
				xs.append(x)
				ys.append(line)
			x+=1
		ax.clear()
		ax.plot(xs, ys)

	ani = animation.FuncAnimation(fig, animate, interval=10)
	try:
		plt.show()
	except:
		print(" ")
