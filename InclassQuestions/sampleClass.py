import sys
import csv

read_object = open('test.csv', 'r')
reader = csv.reader(read_object)
for row in reader:
    print(row)
read_object.close()

write_data = open('test.csv', 'a')
writer = csv.writer(write_data)
writer.writerow(['4', 'Alex', 'Brandon'])
write_data.close()