amount = int(input("Enter the amount"))
# 11463
notes = 0
notes += (amount//2000)  #notes = 5
amount = amount % 2000   #amount = 1463

notes += (amount//500)  #notes = 5+2= 7
amount = amount % 500   #amount = 463

notes += (amount//200)  #notes = 7+2 = 9
amount = amount % 200   #amount = 63

notes += (amount//100)  #notes = 9+0 = 9
amount = amount % 100   #amount = 63

notes += (amount//50)  #notes = 9+1 = 10
amount = amount % 50   #amount = 13

notes += (amount//20)  #notes = 10+0 = 10
amount = amount % 20   #amount = 13

notes += (amount//10)  #notes = 10+1 = 11
amount = amount % 10   #amount = 3

notes += (amount//5)  #notes = 11+0 = 11
amount = amount % 5   #amount = 3

notes += (amount//2)  #notes = 11+1 = 12
amount = amount % 2   #amount = 1

notes += (amount//1)  #notes = 12+1 = 13
amount = amount % 1   #amount = 0

print(notes)