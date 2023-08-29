#write a program that displays a countdown to the burst of fireworks, from 10 to 0, with a 1 second pause between them.

from time import sleep

for countdown in range(10,0,-1):
    sleep(1)
    print (countdown)

sleep(1)
print('Happy new year!')