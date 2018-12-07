import direction
import time
import RoboPiLib as RPL
apin = 7

while True:
  analog = RPL.analogRead(apin)
  direction.analogfront(analog)
  time.sleep(0.05)
