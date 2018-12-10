import RoboPiLib as RPL
import setup
import direction
apin = 7 #place the analog sensor on the front right

while True:
  sense = RPL.analogRead(apin)
  if sense >= 400:
    direction.right(4)
  else:
    direction.front(0)
