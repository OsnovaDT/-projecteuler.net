number = 1
temp = 0
while temp!=20:
	for i in range(1,21):
		if number%i==0:
			temp+=1
		else:
			temp = 0
			break
	if temp !=10:
		number +=1
else:
	print(number)
