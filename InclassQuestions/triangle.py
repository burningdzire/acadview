a = int(input("first side"))
b = int(input("second side"))
c = int(input("third side"))

def checkTriangle(x, y, z):
	if (a + b <= c) or (b + c <= a) or (a + c <= b):
		return False

	return True

res = checkTriangle(a, b, c)
if res == True:
	print ("Valid Triangle")
else:
	print("Invalid Triangle")
