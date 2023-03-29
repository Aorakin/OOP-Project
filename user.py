import _instanceUser
class User:
    def __init__(self,name,lastname,email,user_name,password,user_phone):
        self._name = name
        self._lastname = lastname
        self._email = email
        self._username = user_name
        self._password = password
        self._userphone = user_phone

    def get_name(self):
        return self._name
    def get_lastname(self):
        return self._lastname
    def get_email(self):
        return self._email
    def get_username(self):
        return self._username
    def get_password(self):
        return self._password
    def get_userphone(self):
        return self._userphone
    

def create_user(user_list):
    for key,value in _instanceUser.User_info.items() :
        new_user = User(name=_instanceUser.User_info[key]["name"],
                        lastname=_instanceUser.User_info[key]["last name"],
                        email=_instanceUser.User_info[key]["email"],
                        user_name=_instanceUser.User_info[key]["username"],
                        password=_instanceUser.User_info[key]["password"],
                        user_phone=_instanceUser.User_info[key]["user_phone"])
        user_list.append(new_user)

user_list = []

create_user(user_list=user_list)

for user in user_list:
    print(user.get_name())