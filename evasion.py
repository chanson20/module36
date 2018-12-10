import RoboPiLib as RPL
import setup
import direction
rightsensor = PIN

while True:
  direction.front(10)
  while rightsensor == 0:
    direction.left(7)
