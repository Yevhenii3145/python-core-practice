# class User:
#     name = None
#     last_name = None


# user_1 = User()
# user_1.name = "Boris"
# user_1.last_name = "Johnson"
# print(user_1.name, user_1.last_name) # Boris Johnson

class User:
    def __init__(self, name, last_name=None) -> None:
        self.name = name
        self.last_name = last_name

    def get_fullname(self):
        print(f"Fullname: {self.name} {self.last_name}")

    def __str__(self):
        return f"STR Fullname: {self.name} {self.last_name}"

    def __repr__(self) -> str:
        return f"REPR Fullname: {self.name} {self.last_name}"


user_1 = User("Boris", "Johnson")
user_1.get_fullname()  # Fullname: Boris Johnson
print(user_1.name, user_1.last_name)  # Boris Johnson
print(user_1)  # STR Fullname: Boris Johnson

users = []
users.append(user_1)
print(users)  # [REPR Fullname: Boris Johnson]
