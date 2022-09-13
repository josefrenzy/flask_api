from hmac import compare_digest
from user import User

users = [
    User(1, 'admin', '1234abcd'),
    User(2, 'jose', '1234abcd'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
