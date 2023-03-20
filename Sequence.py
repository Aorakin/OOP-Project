class Peyment:
    def __init__(self,price,peyment_detail,peyment_status):
        self._price = price
        self._peyment_detail = peyment_detail
        self._peyment_status = peyment_status

    def get_detail_reserved(self):
        pass
    
    def get_detail_creaditpayment(self):
        pass
    
    def get_detail_debitpayment(self):
        pass


class CreaditPeyment:
    def __init__(self,card_name,card_number,card_expire,cvv):
        self._card_name = card_name
        self._card_number = card_number
        self._card_expire = card_expire
        self._cvv = cvv

    def create_Creaditpayment(self,card_number):
        pass


class System:
    def __init__(self):
        pass
    def create_reserved(self,user_name,check_in,reservation_detail,calendar):
        pass


class DebitPayment:
    def __init__(self,card_name,card_number,card_expire,cvv):
        self._card_name = card_name
        self._card_number = card_number
        self._card_expire = card_expire
        self._cvv = cvv

    def create_Debitpayment(self,card_number):
        pass


class Reservation:
    def __init__(self,check_in,reservation_detail,calendar):
        self._check_in = check_in
        self._reservation = reservation_detail
        self._calendar = calendar

    def get_detail_payment(self):
        pass


class RoomReserved:
    def __init__(self,date_reserved,end):
        self.__date_reserved = date_reserved
        self.__end = end

    def get_reservation(self):
        pass

    def create_reservarion(reserved):
        pass