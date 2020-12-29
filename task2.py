array = [1,2]
number=4000000
summa = 0
i=0
j=1
while max(array)<number:
	appendNumber = array[j]+array[i]
	if appendNumber<=number:		
		array.append(appendNumber)
	else:
		break
	i+=1
	j+=1
	
for arrElement in array:
	if arrElement%2==0:
		summa+=arrElement
print("sum of even number is "+str(summa))