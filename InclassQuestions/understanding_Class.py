class Student:
	school_name = "KV"

	#creating constructor for the class
	def __init__(self, name, age, standard):
		self.student_name = name
		self.student_age = age
		self.student_class = standard

	def display_details(self):
		print(self.student_name)
		print(self.student_age)
		print(self.student_class)

	def change_school_name(self, new_school_name):
		self.school_name = new_school_name

#object create
new_student1 = Student("rohit", 16, 10)
print(new_student1.school_name)

new_student2 = Student("rajat", 17, 11)
print(new_student2.school_name)

# studentDB = []
#input the details
# for i in range(3):
# 	name = input("Enter your name: ")
# 	age = int(input("Enter your age: "))
# 	standard = int(input("Enter your class: "))
# 	new_student = Student(name, age, standard)
# 	studentDB.append(new_student)

# for i in range(len(studentDB)):
# 	print(studentDB[i].student_name)

