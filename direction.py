import RoboPiLib as RPL
import setup

L = 0
R = 1

#converts a value 1-10 with a speed
def convert(speed):
  R = int(-20 * speed + 1600)
  L = int(20 * speed + 1400)
  return(R,L)

#Default direction
def front(input):
  RPL.servoWrite(R, convert(input)[0])
  RPL.servoWrite(L, convert(input)[1])
def left(input):
  RPL.servoWrite(R,convert(input)[0])
def right(input):
  RPL.servoWrite(L,convert(input)[1])
def frontraw(input):
  RPL.servoWrite(L,input)
  RPL.servoWrite(R,-1*input+3000)

#Analog direction
def analogfront(input):
  RPL.servoWrite(L,leftanalog(input))
  RPL.servoWrite(R,rightanalog(input))
def analogright(input):
  RPL.servoWrite(R,rightanalog(input))
def analogleft(input):
  RPL.servoWrite(L,leftanalog(input))
def touch(input):
  RPL.servoWrite(R,int(-0.1515 * input + 1600))
  RPL.servoWrite(L,int(0.1515 * input + 1400))

#Analog reading to speed converter
def rightanalog(input):
  if input >= 500:
    return(1500)
  else:
    return(int(-0.23*input+1617))
def leftanalog(input):
  if input >= 500:
    return(1500)
  else:
    return(int(0.23*input+1383))

###Stop the Robots motors
def stop():
  pins = [L,R]
  for x in pins:
    RPL.servoWrite(x,0)
