#Write a program that reads any angle and displays its sine, cosine and tangent

import math

ad = float(input('Enter the angle value in degrees '))

ar = math.radians(ad)

print('The values of sine, cosine and tangent of this angle are respectively {:.3f}, {:.3f}, {:.3f}'.format(math.cos(ar), math.sin(ar),math.tan(ar)))

