import RoboPiLib as RPL
import setup

L = pin
R = pin

def convert(speed):
  return(22.13*speed+1389.35)
def front(input):
  speed = convert(input)
  RPL.servoWrite(L,speed)
  RPL.servoWrite(R,speed)
def left(input):
  speed = convert(input)
  RPL.servoWrite(R,speed)
def right(input):
  speed = convert(input)
  RPL.servoWrite(L,speed)
