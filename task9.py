from math import sqrt

number = 500
for a in range(1,number + 1):
	for b in range(2,number+1-a):
		#for c in range(3,number+1):	
		c = int(sqrt(a**2+b**2))
		if (a**2+b**2 == c**2)&(a+b+c == number):
			print("a = {}, b = {}, c = {}".format(a,b,c))
			print(a*b*c)