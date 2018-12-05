import RoboPiLib as RPL
import setup

L = 0
R = 1

def convert(speed):
  return(int(22.13*speed+1389.35))
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
def stop():
  pins = [0,1]
  for x in pins:
    RPL.servoWrite(x,0)
