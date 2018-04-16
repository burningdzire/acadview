import csv

# mohit_object = open('test.csv', 'r')
# mohit = csv.reader(mohit_object)

# for row in mohit:
# 	print(row)

# mohit_object.close()

mohit_object = open('test.csv', 'a')
mohit = csv.writer(mohit_object)
mohit.writerow(['Rohit','Mr.','24','3.4','True'])
mohit_object.close()