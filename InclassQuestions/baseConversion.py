num = int(input("Enter the number: "))
rem = []
while num > 0:
	remainder = num%2
	rem.append(remainder)
	num = num//2

rem.reverse()

for i in range(len(rem)):
	print(rem[i], end = "-")
