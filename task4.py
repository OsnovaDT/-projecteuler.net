maximum = 0
for i in range(100,1000):
	for j in range(100,1000):
		palindrome = i*j
		s = str(palindrome)
		s_reversed = s[::-1]
		if s == s_reversed and palindrome > maximum:
			maximum = palindrome
print(maximum)