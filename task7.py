def SimpleNumber(number):
	n = 0	
	for i in range(2, number):
		if (number%i) == 0:
			n+=1
			break	
	if n == 0:
		t_or_f = True
	else:
		t_or_f = False
	return t_or_f


number_1001 = 0
n = 2
while number_1001 != 1001:
	if SimpleNumber(n):
		number_1001+=1
	n+=1
print(n-1)