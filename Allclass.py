class Dormitory():
    def __init__(self,dor_name,address,detail,phone,electric,water,service_fee,internet,dormitory_picture,term_of_service,owner_name):
        self.__dor_name = dor_name
        self.__address = address
        self.__detail = detail
        self.__phone = phone
        self.__electric = electric
        self.__water = water
        self.__service_fee = service_fee
        self.__internet = internet
        self.__dormitory_picture = dormitory_picture
        self.__term_of_service = term_of_service
        self.__owner_name = owner_name
        self.__review = []

    def get__dor_name(self):
        return self.__dor_name
    
    def get__address(self):
        return self.__address
    
    def get__detail(self):
        return self.__detail
    
    def get__phone(self):
        return self.__phone
    
    def get__electric(self):
        return self.__electric
    
    def get__water(self):
        return self.__water
    
    def get__service_fee(self):
        return self.__service_fee
    
    def get__internet(self):
        return self.__internet
    
    def get__dormitory_picture(self):
        return self.__dormitory_picture
    
    def get__term_of_service(self):
        return self.__term_of_service
    
    def get__owner_name(self):
        return self.__owner_name
    
    def get__review(self):
        return self.__review 
       
    def find_facility(self,facility):
        pass

    def check_room_status(self,):
        pass

    def get_room_catalog(self,):
        pass

    def get_facility(self,):
        pass

    def check_rental(self,):
        pass

    def create_room(self,ID,type,status,rental,room_facility):
        pass

class Facility():
    def __init__(self,pets,ev_charger,salon,laudry,store,restaurant,security,cctv,finger_print,keycard,fitness,pool,lift,parking,smoking):
        self.__pets = pets
        self.__ev_charger = ev_charger
        self.__salon = salon
        self.__laudry = laudry
        self.__store = store
        self.__restaurant = restaurant
        self.__security = security
        self.__cctv = cctv
        self.__finger_print = finger_print
        self.__keycard = keycard
        self.__fitness = fitness
        self.__pool = pool
        self.__lift = lift
        self.__parking = parking
        self.__smoking = smoking

    def get__pets(self):
        return self.__pets
    
    def get__ev_charger(self):
        return self.__ev_charger
    
    def get__salon(self):
        return self.__salon
    
    def get__laudry (self):
        return self.__laudry
    
    def get__store(self):
        return self.__store
    
    def get__restaurant (self):
        return self.__restaurant
    
    def get__security (self):
        return self.__security
    
    def get__cctv (self):
        return self.__cctv
    
    def get__finger_print(self):
        return self.__finger_print
    
    def get__keycard (self):
        return self.__keycard
    
    def get__fitness (self):
        return self.__fitness
    
    def get__pool (self):
        return self.__pool
    
    def get__lift (self):
        return self.__lift
    
    def get__parking(self):
        return self.__parking
    
    def get__smoking(self):
        return self.__smoking

        
class Review():
    def __init__(self,rating,comment) :
        self.__rating = rating
        self.__comment = comment

    def add_review_to_list(self,rating,comment):
        pass

    def get_rating(self):
        return self.__rating
    
    def get_comment(self):
        return self.__comment
    
class RoomCatalog():
    
    def __init__(self, Room):
        self.__Room = Room
    
    def get_room_rental_list(self):
        pass
    def get_room_status_list(self):
        pass
    def create_room(self,Room):
        pass
    def save_to_room_list(self,):
        pass
