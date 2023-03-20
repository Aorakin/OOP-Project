class DormitoryCatalog:
    def __init__(self):
        self._dormitory = []
        self._boost_dormity = []
    def check_facility():
        pass
    def save_to_dormitory_list():
        pass
    def check_price(self,max_price):
        pass
    def create_dormitory(self,name,address,detail,phone,electric,warter,sevice_fee,internet,dorm_picture,term_of_service):
        pass
    def get_dormitory_list(self,name_dor):
        pass
    def get_dormitory_list(self):
        pass

class Owner(User):
    def __init__(self,name,lastname,email,user_name,password,user_phone,verified):
        User.__init__(self,name,lastname,email,user_name,password,user_phone)
        self._verified = verified
    def add_owner_tolList(owner):
        pass

class AccountList:
    def __init__(self):
        self._account = []
    def check_user(self,user_name,password):
        pass

Dormitory = {
    jia_jia_place:{
        "dorm_name":'Jia Jia Place',
        "address":'Soi Hormai',
        "detail":'-',
        "phone":'0945593062',
        "electric":8,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Vorachot',
        },
    sabai_place:{
        "dorm_name":'Sabai Place',
        "address":'Soi V Condo',
        "detail":'-',
        "phone":'025479864',
        "electric":8,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Hom',
        },
    aj_park:{
        "dorm_name":'Aj Park',
        "address":'Soi Aj',
        "detail":'-',
        "phone":'0945593062',
        "electric":8,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Oak',
        },
    hor_nai:{
        "dorm_name":'Hornai',
        "address":'Soi Hornai',
        "detail":'-',
        "phone":'0945593062',
        "electric":8,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Ball',
        },
    rnp_place:{
        "dorm_name":'RNP Place',
        "address":'Soi RNP',
        "detail":'-',
        "phone":'0945593062',
        "electric":8,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Noon',
        },
    v_condo:{
        "dorm_name":'V Condo',
        "address":'Soi V Condo',
        "detail":'-',
        "phone":'0945593062',
        "electric":7,
        "water":17,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Boom',
        },
    u_place:{
        "dorm_name":'U Place',
        "address":'Soi RNP',
        "detail":'-',
        "phone":'0945593062',
        "electric":8,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Arm',
        },
   papamama:{
        "dorm_name":'PapaMama',
        "address":'Soi Hormai',
        "detail":'-',
        "phone":'0945593062',
        "electric":7,
        "water":17,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Pookie',
        },
    hor_dum:{
        "dorm_name":'Hor Dum',
        "address":'Soi Hordum',
        "detail":'-',
        "phone":'0945593062',
        "electric":5,
        "water":18,
        "service_fee":0,
        "internet":0,
        "picture":'-',
        "term_of_service":'-',
        "owner_name":'Mew',
        }
    }