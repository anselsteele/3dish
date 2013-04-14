from Tkinter import *
import math
import random
import time
master = Tk()
cvs = Canvas(master,width = 700,height = 700)
cvs.pack()
while True:
  rando1 = random.randint(50,650)
	rando2 = random.randint(50,650)
	complexity = random.randint(15,35)
	counter = 1
	array = []
	datapoint = [rando1,rando2]
	array.append(datapoint)
	while counter <= complexity:
		add1 = random.randint(-20,20)
		add2 = random.randint(-20,20)
		rando1 = rando1 + add1
		rando2 = rando2 + add2 
		datapoint = [rando1,rando2]
		array.append(datapoint)
		counter = counter + 1


	cvs.create_polygon(array,fill = 'blue')
	randolen = random.randint(10,50)
	deptharray = []
	caparray = []
	for item in array:
		xval = item[0]
		yval = item[1]
		xvalnew = xval
		yvalnew = yval + randolen
		datapoint = [xval,yval,xvalnew,yvalnew]
		minidata = [xvalnew,yvalnew]
		deptharray.append(datapoint)
		caparray.append(minidata)
	counterlim = len(deptharray)
	counter = 0
	redpurp = 1
	while counter < counterlim:
		redpurp = redpurp * -1
		if redpurp == 1:
			color = 'red'
		if redpurp == -1:
			color = 'purple' 
		pluscounter = counter + 1
		thing1 = deptharray[counter]
		if pluscounter >= counterlim:
			pluscounter = 0
		thing2 = deptharray[pluscounter]

		x1 = thing1[0]
		y1 = thing1[1]
		x2 = thing1[2]
		y2 = thing1[3]
		x3 = thing2[0]
		y3 = thing2[1]
		x4 = thing2[2]
		y4 = thing2[3]
		cvs.create_polygon(x1,y1,x2,y2,x4,y4,x3,y3,fill = color)
		counter = counter + 1
	cvs.create_polygon(caparray,fill = 'blue')
	time.sleep(1)
	cvs.update()
master.mainloop()
