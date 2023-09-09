import random
from firebase.api import RTDB
from time import sleep


db = RTDB()

BIAYA_PER_KWH = 1.525

def random_kwh(start, end, rounded=5):
    return round(random.uniform(start, end), rounded)

def biaya_listrik(kwh):
    biaya = kwh * BIAYA_PER_KWH
    return int(round(biaya + ( biaya * 0.1), 3) * 1000)

db.update('/', { 'harga_token': 5000})

while True:

    sisa_token = db.read('/harga_token')
    if sisa_token > 0:
        value_kwh  = random_kwh(0, 3, rounded=1)
        pemakaian_listrik = biaya_listrik(value_kwh)
        token_baru = sisa_token - pemakaian_listrik

        if token_baru < 0:
            db.update('/', { 'harga_token': 0})
            continue
        
        # update sisa token
        else:
            db.update('/', {'harga_token': token_baru})

    else: 
        db.update('/', {'harga_token': 0})
        print("TOKEN HABISS")

    sleep(3)