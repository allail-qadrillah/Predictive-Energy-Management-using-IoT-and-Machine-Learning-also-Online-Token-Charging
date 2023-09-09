from pzem.app import PZEM
from time import sleep
from raspberry.app import Pin 


pzem = PZEM()

# relay.write(HIGH)
while True:
  data = pzem.read()

  print(
    "voltage", pzem.get_voltage(),
    "current", pzem.get_current(),
    "power", pzem.get_power(),
    "energy", pzem.get_energy(),
    "frekuensi", pzem.get_frekuensi(), 
    "kwh", round(pzem.get_energy_kwh(), 3)
  )

  sleep(1)
