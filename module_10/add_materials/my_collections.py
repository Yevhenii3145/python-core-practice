from collections import UserDict,UserList

class Phones(UserList):
    def set_phone(self, phone):
        if len(phone) == 12:
            new_phone = "+" + phone
        elif len(phone) < 12:
            new_phone = "+38" + phone
        self.data.append(new_phone)

    def get_phones(self):
        return self.data

phone_list  = Phones()
phone_list.set_phone("0989008080")
phone_list.set_phone("380987007070")
print(phone_list.get_phones()) # ['+380989008080', '+380987007070']

# {"name: имя", "phones": [phone, phone, phone]}
class User(UserDict):
    def set_name(self, name):
        self.data["name"] = name

    def get_name(self):
        return self.data.get("name")

    def set_phone(self, phone):
        phone_list = self.data.get("phones", Phones())
        phone_list.data.append(phone)
        self.data["phones"] = phone_list

    def get_phones(self):
        return self.data.get("phones")

user_1 = User()
user_1.set_name("Bill")
user_1.set_phone("38093009090")
print(user_1.get_name(), user_1.get_phones()) # Bill ['38093009090']
