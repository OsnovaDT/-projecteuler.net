def simpleNumber(number):
	array=[]
	x = 2
	while (number!=1)&(x<=number):
		if number%x==0:
			array.append(x)
			number=number/x
		else:
			x+=1
	return(array)
print(simpleNumber(100))