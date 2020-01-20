import json

users = {
    'user1': 'authentizated',
    'user2': 'authorized',
    'user3': 'anonym',
}

json_obj = json.dumps(users, indent=3)

result = json_obj

r = json.loads(result) # распечатываем жсон в питоновский формат
print(r)