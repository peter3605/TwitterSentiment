import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime

style.use('ggplot')

fig = plt.figure()
fig.canvas.set_window_title('Graph')
fig.set_size_inches(7, 8, forward=True)
graph_data = open('data.txt','r').read()
lines = graph_data.split('\n')
title = "start time: "+str(datetime.now())+"\n"+"search term: "
fig.suptitle(title)
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
		if(x!=0):
			try:
				total += int(line)
			except:
				continue
			fig.suptitle(title+lines[0]+"\n"+"number of tweets: "+str(x)+"\n"+"average sentiment score: "+str(total/x))
			xs.append(x)
			ys.append(line)
		x+=1
	ax.clear()
	ax.plot(xs, ys)
	
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
