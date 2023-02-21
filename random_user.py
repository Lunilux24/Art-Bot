import random as r
import json, os , uuid
from datetime import datetime, timezone, timedelta

filename = 'user_db.json'

def get_random_user() -> str:
    with open (filename, 'r') as userfile:
        users = json.load(userfile)

    random_number = r.randint(0, len(users) - 1)

    for i in range(len(users)):
        current_user = users[(random_number + i) % len(users)]
        if(is_valid_access_time(current_user)):
            current_user["last_accessed"] = datetime.now(timezone.utc).isoformat()
            write_new_data(users)

            return current_user["username"]
        
    current_user = users[random_number]
    current_user["last_accessed"] = datetime.now(timezone.utc).isoformat()
    write_new_data(users)

    return current_user["username"]

def is_valid_access_time(user):
    return not user["last_accessed"] or datetime.fromisoformat(user["last_accessed"]) + timedelta(hours=1) < datetime.now(timezone.utc)

def write_new_data(data) -> None:
    tempfile = os.path.join(os.path.dirname(filename), str(uuid.uuid4()))
    with open(tempfile, 'w') as f:
        json.dump(data, f, indent=4)
    
    os.rename(tempfile, filename)