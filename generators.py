from faker import Faker

fake = Faker()

def generate_courier_body():
    return {
        'login': fake.user_name(),
        'password': fake.password(),
        'firstName': fake.first_name()
    }

def generate_login():
    return fake.user_name()

def generate_password():
    return fake.password()

def generate_first_name():
    return fake.first_name()

def generate_id_courier():
    return {'id': fake.random_int(1000000, 9999999)}

def generate_id_order():
    return {'order': {'id': fake.random_int(1000000, 9999999)}
            }
def generate_track_order():
    return fake.random_int(1000000, 9999999)

def generate_data_order():
    return {
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": fake.random_int(1, 9),
    "phone": fake.phone_number(),
    "rentTime": fake.random_int(1,9),
    "deliveryDate": fake.date_between('today', '+30d').isoformat(),
    "comment": fake.word()
}