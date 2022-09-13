user = {"username": "Jose", "access_level": "admin"}


def make_secure(func):
    def secure_function() -> str:
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No permissions for user: {user['username']}"
    return secure_function


@make_secure
def get_admin_password():
    return "1234"

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
