import json

class User:
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        self._name = name
        self._lastname = lastname
        self._email = email
        self._user_name = user_name
        self._password = password
        self._user_phone = user_phone
    def add_user_toList(User):
        pass

class RegistrationSystem:
    def __init__(self):
        self.users = {}

    def register(self):
        name = input("Enter name: ") #เอาไว้แก้เป็นดึงข้อมูลจากหน้าบ้าน
        lastname = input("Enter lastname")
        email = input("Enter email: ")
        user_name = input("Enter UserName")
        password = input("Enter password: ")
        user_phone = input("Enter phone number")
        # Load the user info from a file
        with open("instanceUser.json", "r") as file:
            user_info = json.load(file)
        # Add a new user to the dictionary
        new_user = {
            "name": name,
            "last name": lastname,
            "email": email,
            "username": user_name,
            "password": password,
            "user_phone": user_phone
        }
        # Save the updated user info to a file
        for i in range:
            user_info[f"User{[i]}"] = new_user
        with open("user_info.json", "w") as file:
            json.dump(user_info, file, indent=4)