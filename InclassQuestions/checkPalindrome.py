test = input("Enter a string: ")

def checkPalindrome(teststr):
	#this function check if a given 
	#string is palindrome or not
	i = 0
	j = len(teststr) - 1
	while i < j:
	 	if teststr[i] != teststr[j]:
	 		print("Not a palindrome")
	 		break
	 	else:
	 		i = i + 1
	 		j = j - 1

	if i >= j:
		print("It is palindrome")

checkPalindrome(test)