from firebase.api import RTDB
from time import sleep
from pzem.app import PZEM
from lcd.app import LCD
import drivers
import modbus_tk.exceptions as modbus_exceptions
import RPi.GPIO as GPIO
import time

# Mengatur mode GPIO
GPIO.setmode(GPIO.BCM)

# Mengatur pin 17 sebagai output
GPIO.setup(17, GPIO.OUT)


BIAYA_PER_KWH = 0.415

db = RTDB()
display = drivers.Lcd()
lcd = LCD()

def biaya_listrik(kwh):
    biaya = kwh * BIAYA_PER_KWH
    return int(round(biaya + ( biaya * 0.1), 3) * 1000)

# conecting 
lcd.progress_bar()
# display.lcd_clear()
def main():

    while True:
        try:

            pzem = PZEM()
            # display starting
            sisa_token = db.read('/harga_token')

            if sisa_token > 0:
                GPIO.output(17, GPIO.LOW) 

                display.lcd_display_string(f"1111 2008 0069", 1)
                display.lcd_display_string(f"Power: {round(pzem.get_energy_kwh(), 3)} kWh" , 2)
                value_kwh  = round(pzem.get_energy_kwh(), 3)
                pemakaian_listrik = biaya_listrik(value_kwh)
                token_baru = sisa_token - pemakaian_listrik
                print("sisa", sisa_token, "pemakaian", pemakaian_listrik)
                print(token_baru)
                if token_baru < 0:
                    db.update('/', { 'harga_token': 0})
                    continue
                
                # update sisa token
                else:
                    db.update('/', {'harga_token': token_baru})

            else: 
                db.update('/', {'harga_token': 0})
                print("TOKEN HABISS")
                GPIO.output(17, GPIO.HIGH) 

                display.lcd_clear()
                display.lcd_display_string(f"Token Runs Out", 1)
                display.lcd_display_string(f"Refill" , 2)


            db.update('/', {
                "arus": pzem.get_current(),
                "daya": round(pzem.get_energy(), 3),
                "tegangan": pzem.get_voltage(),
                "frekuensi": pzem.get_frekuensi()
            })    
    
            sleep(1)
            # display.lcd_clear()

        except modbus_exceptions.ModbusInvalidResponseError as e:
            print("pzem mati") 
            display.lcd_clear()
            display.lcd_display_string(f"Token Runs Out", 1)
            display.lcd_display_string(f"Refill" , 2)

            continue
        

if __name__ == "__main__":
  main()