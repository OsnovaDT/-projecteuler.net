def SimpleNumber(number):
	t_or_f = False
	if number == 2:
		t_or_f = True		
	else:
		for i in range(2, number):
			if number % i == 0:
				t_or_f = False
				break
			else:
				t_or_f = True
	return t_or_f
summa = 0
for i in range(1,20000):
	if SimpleNumber(i):
		summa+=i
print(summa)

