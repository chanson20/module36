import RoboPiLib as RPL
import setup

L = 0
R = 1

#converts a value 1-10 with a speed
def convert(speed):
  return(int(22.13*speed+1389.35))

#Default direction
def front(input):
  speed = convert(input)
  RPL.servoWrite(L,speed)
  RPL.servoWrite(R,speed)
def left(input):
  RPL.servoWrite(R,convert(input))
def right(input):
  RPL.servoWrite(L,convert(input))


#Analog direction
def analogfront(input):
  RPL.servoWrite(L,leftanalog(input))
  RPL.servoWrite(R,rightanalog(input))
def analogright(input):
  RPL.servoWrite(R,rightanalog(input))
def analogleft(input):
  RPL.servoWrite(L,leftanalog(input))

#Analog reading to speed converter
def rightanalog(input):
  return(int(-0.23*input+1617))
def leftanalog(input):
  return(int(0.23*input+1383))

###Stop the Robots motors
def stop():
  pins = [L,R]
  for x in pins:
    RPL.servoWrite(x,0)
