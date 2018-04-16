class Employee:
	total_employee = 0
	def __init__ (self, name, salary):
		self.employee_name = name
		self.employee_salary = salary
		Employee.total_employee += 1

	def display_employee(self):
		print(self.employee_name + " " + str(self.employee_salary))

	def count_total(self):
		print(Employee.total_employee)

emp1 = Employee("John", 24000)
emp1.display_employee()
emp1.count_total()

emp1 = Employee("Jenna", 26000)
emp1.display_employee()
emp1.count_total()