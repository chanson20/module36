import direction
import time
import RoboPiLib as RPL
pause = 0.53 #Time after autopilot goes away
speed = 1460 #Speed after autopilot goes away
apin = 7 #Analog Sensor 84.18mm from the front

while True:
  analog = RPL.analogRead(apin)
  if analog <= 600: #Autopilot
    direction.touch(analog)
  else:
    direction.frontraw(speed)
    time.sleep(pause)
    direction.stop()
    break
