import direction
apin = PIN

while True:
  analog = RPL.analogRead(apin)
  direction.analogfront(analog)
