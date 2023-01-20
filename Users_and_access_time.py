import time
import random as r
import json

def timer(cooldown_in_seconds):
    while time.sleep(cooldown_in_seconds):
        global timer_finished
        timer_finished = False
    return timer_finished

with open ('users.json', 'r') as userfile:
    global users
    users = json.load(userfile)

global list_of_users 
list_of_users = [user for user in users]

dict_of_users = {}
for i in range(len(list_of_users)):
    dict_of_users[users[i]["username"]] = True
print(dict_of_users)
def random_user():
    random_number = r.randint(0, len(list_of_users) - 1)
    random_user = str(list_of_users[random_number])
    print("\n\n\n", random_user)
    if dict_of_users[random_user] == "false":
        random_user()
    #users[str(random_user)]["selectable_for_random_user"] = timer(8400)
    return random_user