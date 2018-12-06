import RoboPiLib as RPL
import setup

L = pin
R = pin

#converts a value 1-10 with a speed
def convert(speed):
  return(22.13*speed+1389.35)

#Default Direction
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
def leftanalog(input):
  return(-0.23*input+1617)
def rightanalog(input):
  return(0.23*reading+1383)
