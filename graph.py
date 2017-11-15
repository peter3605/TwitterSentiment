import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
fig.suptitle('location: "119.1796875,5.3972734077,127.1337890625,18.9374644296" size:337')
ax = fig.add_subplot(1,1,1)
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

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()