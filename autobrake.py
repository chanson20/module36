import direction
import RoboPiLib as RPL
apin = 7

while True:
  analog = RPL.analogRead(apin)
  direction.analogfront(analog)
  if analog >= 500:
    break
