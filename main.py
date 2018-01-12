import tkinter
import twitter_stream as ts
import sys
import os
from threading import Thread

class GUI:
	def __init__(self, window):
		self.window = window
		self.window.title("Twitter Sentiment Analysis")
		self.window.geometry("500x300")
		self.window.wm_iconbitmap("logo.ico")

		self.label = tkinter.Label(window, text="Please insert search terms - they need to be separated by spaces")
		self.label.pack(anchor='center')
		
		self.text_field = tkinter.Entry(window, bd =5)
		self.text_field.pack(anchor='center')
		
		self.var = tkinter.IntVar()
		self.var.set(1)
		
		self.radioBtn1 = tkinter.Radiobutton(self.window, text="Algorithm 1", variable=self.var, value=1)
		self.radioBtn1.pack(anchor = 'center')
		self.radioBtn2 = tkinter.Radiobutton(self.window, text="Algorithm 2", variable=self.var, value=2)
		self.radioBtn2.pack(anchor = 'center')
		self.radioBtn3 = tkinter.Radiobutton(self.window, text="Algorithm 3", variable=self.var, value=3)
		self.radioBtn3.pack(anchor = 'center')
		
		self.enter_button = tkinter.Button(window, text="Enter", command = self.enter_button_event)
		self.enter_button.pack(anchor='center')

		
	def run_graph(self):
		os.system('graph.py')
		self.text_field.delete(0, 'end')
		
	def run_stream(self):
		input = self.text_field.get()
		arg = input.split()
		ts.start(arg, self.var.get())
	
	def enter_button_event(self):
		t = Thread(target=self.run_graph, args=())
		t.start()

		t1 = Thread(target = self.run_stream, args = ())
		t1.start()
		
		
		
def enter_key_event(event):
		if(event.keysym == "Return"):
			my_gui.enter_button_event()
		

window = tkinter.Tk()
my_gui = GUI(window)
window.bind('<Key>', enter_key_event)
window.mainloop()