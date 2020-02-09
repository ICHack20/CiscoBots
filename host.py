import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def start_pressed(event):
	print("Start pressed")

def make_plot():
	# player 1
	plt.subplot(221)
	#plt.imshow()
	plt.title("player 1")

	# player 2
	plt.subplot(222)
	plt.title("player 2")

	# game
	plt.subplot(212)
	plt.title("score")

	# start button
	bstart = Button(plt.axes([0.9, 0.03,0.09,0.075]), "Start!")
	bstart.on_clicked(start_pressed)

	plt.show()

if __name__=="__main__":
	make_plot()


