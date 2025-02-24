import time
import turtle 

pen = turtle.Turtle() 
pen.speed(5)

def curve(): 
	for i in range(200): 
		pen.right(1) 
		pen.forward(1)

def heart(): 
	pen.fillcolor('red') 
	pen.begin_fill() 
	pen.left(140) 
	pen.forward(113) 
	curve() 
	pen.left(120) 
	curve() 
	pen.forward(112) 
	pen.end_fill() 

def txt(): 
	pen.up() 
	pen.setpos(-45, 95) 
	pen.down() 
	pen.color('lightgreen') 
	pen.write("I love You", font=( "Verdana", 12, "bold"))
	pen.ht()
	time.sleep(2)

heart()
txt() 
