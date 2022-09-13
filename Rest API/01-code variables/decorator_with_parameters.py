import functools

user = {"username": "Jose", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No permissions for user: {user['username']}"
    return secure_function


@make_secure
def get_password(panel):
    print(panel)
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password.__name__)
