marks = [0, 0, 0, 0, 0]
marks[0] = int(input("Enter physics"))
marks[1] = int(input("Enter Chem"))
marks[2] = int(input("Enter Maths"))
marks[3] = int(input("Enter Bio"))
marks[4] = int(input("Enter Computer"))

grades = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/5
if grades >= 90:
	print("A")
elif grades >=80:
	print("B")
elif grades >=70:
	print("C")
elif grades >= 60:
	print("D")
elif grades >= 40:
	print("E")
else:
	print("F")
