import direction
apin = PIN

while True:
  analog = RPL.analogRead(apin)
  if analog <= 450:
    direction.front(10)
  elif analog <= 500:
    direction.front(6)
  elif analog <= PUT_VALUE_HERE
    direction.stop()
