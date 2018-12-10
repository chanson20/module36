import direction
import time
pause = TIME HERE
apin = 7

while True:
  analog = RPL.analogRead(apin)
  if analog <= 650:
    direction.touch(analog)
  else:
    direction.frontraw(1505) #EDIT THIS
    time.sleep(pause)
    direction.stop()
    break
