import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class BattleBots:
	def __init__(self):
		pass

	def start_pressed(self, event):
		print("Start pressed")

	def make_plot(self):
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
		bstart.on_clicked(self.start_pressed)

		plt.show()

	def main(self):
		self.make_plot()

if __name__=="__main__":
	bb = BattleBots()
	bb.main()

