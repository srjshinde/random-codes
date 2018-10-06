import RPi.GPIO as g
import time
g.setmode(g.BOARD)

class Ultrasonic:

	def __init__(self,trig,echo):

		self.trig=trig
		self.echo=echo

	def read_dist(self):

		g.setup(self.trig,g.OUT)
		g.setup(self.echo,g.IN)
		
		g.output(self.trig,True)
		time.sleep(0.000001)
		g.output(self.trig,False)


		while g.input(self.echo)==0:
			start=time.time()

		while g.input(self.echo)==1:
			stop=time.time()

		elapsed=stop-start
		d=((34300*elapsed)/2)
		return d
