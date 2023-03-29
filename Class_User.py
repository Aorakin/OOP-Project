from AccountList import AccountList

class User:
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        self._name = name
        self._lastname = lastname
        self._email = email
        self._user_name = user_name
        self._password = password
        self._user_phone = user_phone
        self.users = {}

    def register(self):
        name = input("Enter name: ") #เอาไว้แก้เป็นดึงข้อมูลจากหน้าบ้าน
        lastname = input("Enter lastname")
        email = input("Enter email: ")
        user_name = input("Enter UserName")
        password = input("Enter password: ")
        user_phone = input("Enter phone number")

        # Add a new user to the accountlist
        account_list = AccountList()
        new_user = User(name,lastname,email,user_name,password,user_phone)
        account_list.add_account(new_user)