class User:
    name = None
    age = None
    phone = None

    def greeting(self):
        print("self is", self)
        return f"I am {self.name}"

user_1 = User()
user_1.name = "Vlad"
user_1.age = 32
user_1.phone= "00634565534"
print(user_1) # <__main__.User object at 0x0000025073D3C710>
print(user_1.name, user_1.age,user_1.phone) # Vlad 32 00634565534
print(user_1.greeting()) # self is <__main__.User object at 0x0000025073D3C710> I am Vlad
