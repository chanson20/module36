import RoboPiLib as RPL
import setup
import direction
apin = PIN #right side

while True:
  analog = RPL.analogRead(apin)
  if analog >= 300 and analog <= 400:
    direction.front(10)
  elif analog > 400:
    direction.left(7)
  elif analog < 300:
    direction.right(7)
