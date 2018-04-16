import sys
import csv
from spy_details import SPY, ChatMessage

friends = []

def add_friend():
	friend_name = input("What is your friend's name? ")
	friend_salutation = input("Salutation? (Mr./ Mrs.) ")
	friend_age = int(input("Age? "))
	friend_rating = float(input("Rating? "))

	#validating the name
	if friend_name.isalpha() == False:
		print("\nGiven name is invalid.\nTerminating application")
		sys.exit(0)

	#validating the age
	if friend_age <= 12 or friend_age >= 50:
		print("\nGiven age is invalid.\nTerminating application")
		sys.exit(0)

	new_friend = SPY(friend_name, friend_salutation, friend_age, friend_rating)
	friends.append(new_friend)

	print("Here is the updated list of friends")
	counter = 0
	for f in friends:
		counter += 1
		print('%d. %s' % (counter, f.name))

def select_friend():

	#Printing all the friends of a User
	counter = 0
	for f in friends:
		counter += 1
		print('%d. %s' % (counter, f.name))

	#Asking the user to select a friend
	friend_choice = int(input("Choose from your friends: "))
	friend_choice -= 1
	
	#Returning the index
	return friend_choice

def send_message():
	print("Choose the friend to whom you want to send the message")
	friend_choice = select_friend()

	message = input("Enter the message to be send: ")
	new_chat_message = ChatMessage(message, True)

	friends[friend_choice].chats.append(new_chat_message)
	print("Your message has been sent to %s" %friends[friend_choice].name)

def read_message():
	print("Choose the friend whose message you want to read")
	sender = select_friend()

	if len(friends[sender].chats) == 0:
		print("You have no conversation with %s" %friends[sender].name)
	else:
		for i in range(len(friends[sender].chats)):
			print(friends[sender].chats[i].message)


def load_friends():
	read_object = open("friends.csv", 'r')
	reader = csv.reader(read_object)
	for row in reader:
		# order will be (name, salutation, age, rating)
		name = row[0]
		salutation = row[1]
		age = int(row[2])
		rating = float(row[3])
		is_online = bool(row[4])
		new_friend = SPY(name, salutation, age, rating)
		friends.append(new_friend)
	read_object.close()

def save_friends():
	write_object = open("friends.csv", 'wb')
	writer = csv.writer(write_object)
	for i in range(len(friends)):
		name = friends[i].name
		salutation = friends[i].salutation
		age = friends[i].age
		rating = friends[i].rating
		is_online = friends[i].is_online
		writer.writerow([name,salutation,age,rating,is_online])
	write_object.close()


def load_chats():
	read_object = open("chats.csv", 'r')
	reader = csv.reader(read_object)
	for row in reader:
		name = row[0]
		msg = ChatMessage(row[1], row[2])
		for i in range(len(friends)):
			if friends[i].name == name:
				friends[i].chats.append(msg)

	read_object.close()

def save_chats():
	write_object = open("chats.csv", 'wb')
	writer = csv.writer(write_object)

	for i in range(len(friends)):
		for j in range(len(friends[i].chats)):
			writer.writerow([friends[i].name, friends[i].chats[j].message,friends[i].chats[j].send_by_me])

	write_object.close()
