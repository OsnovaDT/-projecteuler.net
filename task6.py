def sumOfSquares(number):
	sum = 0
	for i in range(1,number+1):
		sum += i**2
	return sum
def squareOfSum(number):
	sum = 0
	for i in range(1,number+1):
		sum += i
	sum = sum**2
	return sum
print(squareOfSum(100) - sumOfSquares(100))