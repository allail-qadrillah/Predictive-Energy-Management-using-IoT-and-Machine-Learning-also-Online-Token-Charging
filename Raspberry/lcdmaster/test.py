import RPi.GPIO as GPIO
import time

# Mengatur mode GPIO
GPIO.setmode(GPIO.BCM)

# Mengatur pin 17 sebagai output
GPIO.setup(17, GPIO.OUT)

# Mengubah status output pin 17 secara berulang
while True:
    GPIO.output(17, GPIO.HIGH)  # Mengaktifkan output (HIGH/ON)
    time.sleep(1)               # Menunda selama 1 detik
    GPIO.output(17, GPIO.LOW)   # Mematikan output (LOW/OFF)
    time.sleep(1)               # Menunda selama 1 detik

# Membersihkan konfigurasi GPIO sebelum keluar dari program
GPIO.cleanup()
