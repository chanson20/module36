import direction
import time
apin = PIN

while True:
  analog = RPL.analogRead(apin)
  direction.analogfront(analog)   
