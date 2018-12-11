import direction
import time
import RoboPiLib as RPL
pause = TIME HERE
speed = SPEED HERE
apin = 7

while True:
  analog = RPL.analogRead(apin)
  if analog <= 650: #EDIT THIS
    direction.touch(analog)
  else:
    direction.frontraw(speed)
    time.sleep(pause)
    direction.stop()
    break
