import sys
import spy_status
from spy_details import SPY 
import spy_friend
print("Welcome to SpyChat program")

# Module 1: Creating User Profile
# Now we have two options :-
# 1. Creating spy profile from default values.
# 2. Creating spy profile by taking input from the user.
print("Let's first create your profile\n")
profile_choice = input("Do you want to continue with the current settings? (y/n) ")

if profile_choice.upper() == 'Y':
	spy = SPY("Bond", "Mr.", 25, 4.8)
else :
	name = input("What is your name? ")
	salutation = input("What should we call you? (Mr./ Mrs.) ")
	age = int(input("how old are you? "))
	rating = float(input("What is your rating? "))

	#validating the name
	if name.isalpha() == False:
		print("\nGiven name is invalid.\nTerminating application")
		sys.exit(0)

	#validating the age
	if age <= 12 or age >= 50:
		print("\nGiven age is invalid.\nTerminating application")
		sys.exit(0)

	spy = SPY(name, salutation, age, rating)

# Printing spy details
print("\nHello %s %s " %(spy.salutation, spy.name))
print("We have successfully created your account")


# Module 2: Creating a menu
# To create menu, we will be defining the function start_chat()
def start_chat():
	show_menu = True
	while show_menu:
		print("\nYou can select from the operations")
		print("1. Add Friend\n2. Add Status\n3. Send Secret Message\n4. Read Secret Message\n5. Close application")
		menu_choice = int(input("What do you want to do: "))

		if menu_choice == 1:
			print("\nYou have chosen to add a friend")
			spy_friend.add_friend()
		elif menu_choice == 2:
			print("\nYou have chosen to add a status")
			spy.current_status_message = spy_status.add_status(spy.current_status_message)
		elif menu_choice == 3:
			print("\nYou have chosen to send message")
			spy_friend.send_message()
		elif menu_choice == 4:
			print("\nYou have chosen to read message")
			spy_friend.read_message()
		elif menu_choice == 5:
			print("\nYou have chosen to close the application")
			show_menu = False
		else:
			print("\nIncorrect choice")

spy_friend.load_friends()
spy.current_status_message = spy_status.load_status()
start_chat()
spy_friend.save_friends()
spy_status.save_status()