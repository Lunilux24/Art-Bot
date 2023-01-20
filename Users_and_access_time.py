import random as r
import json
import threading

def main():
    with open ('users.json', 'r') as userfile:
        global users
        users = json.load(userfile)

    global list_of_users
    list_of_users = [user for user in users]

    global dict_of_users
    dict_of_users = {}
    for i in range(len(list_of_users)):
        if users[i]["selectable_for_random_user"] == "default":
            dict_of_users[users[i]["username"]] = True

    print("dict of users: ", dict_of_users)

    random_user()


def check_user(username):
    # Check if the user exists in the dictionary
    if username in dict_of_users:
        # Set the value to False
        dict_of_users[username] = False
        print(f"{username}'s value set to False.")
        # Start a timer to set the value back to True after 24 hours
        threading.Timer(86400, set_user_true, args=[username]).start()
    else:
        print(f"{username} not found in the dictionary.")

def set_user_true(username):
    # Set the user's value back to True
    dict_of_users[username] = True
    print(f"{username}'s value set back to True.")

def random_user():
    random_number = r.randint(0, len(list_of_users) - 1)
    global random_username
    random_username = list_of_users[random_number]
    
    print("Random User: ")
    print(random_username["username"], "\n")
    print("dict of users: ", dict_of_users)

    check_user(random_username["username"])