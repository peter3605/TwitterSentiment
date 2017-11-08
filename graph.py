import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class Graph():
	style.use('ggplot')

	fig, ax = plt.subplots()
	ax.set_yticks([-20,0,20])
	ax.set_xticks([])

	def animate(i):
		graph_data = open('data.txt','r').read()
		lines = graph_data.split('\n')
		xs = []
		ys = []
		x=0
		for line in lines:
			x+=1
			xs.append(x)
			ys.append(line)
		ax.clear()
		ax.plot(xs, ys)
	ax.set_yticks([-20,0,20])
	ax.tick_params(labelbottom='off')  
	ax.tick_params(labelleft='off')  
	ani = animation.FuncAnimation(fig, animate, interval=10)
	plt.show()