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

class Reservation(Room):
    def __init__(self,check_in,reservation_detail,calendar):
        Room.__init__(self,room_id,room_rental,room_status,room_fac):
        self.__check_in = check_in
        self.__reservation_detail = reservation_detail
        self.__calendar = calendar
    def get_detail_payment():
        pass

class Room:
    def __init__(self,room_id,room_rental,room_status,room_fac):
        self._room_id = room_id
        self._room_rental = room_rental
        self._room_status = room_status
        self._room_fac = room_fac
    def get_name_dormitory():
        pass

class RoomReserved(Room):
    def __init__(self,date_reserved,end ):
        Room.__init__(self,room_id,room_rental,room_status,room_fac):
        self.__date_reserved = date_reserved
        self.__end  = end
    def get_reservation():
        pass

