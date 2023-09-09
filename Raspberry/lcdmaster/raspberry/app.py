import RPi.GPIO as GPIO

class Pin:
  
  def __init__(self, pin:int, mode:str) -> None:
    """
    pin: nomer pin?
    mode: 'in' == input and 'out' == output
    """
    self.pin = pin
    GPIO.setmode(GPIO.BCM)

    if self.mode == "in": GPIO.setup(self.pin, GPIO.IN);
    elif self.mode == "out": GPIO.setup(self.pin, GPIO.OUT);
    else: raise ValueError("Invalid Mode. ")

  def read(self):
    if self.mode != "in":
        raise ValueError("Cannot read from pin set as output.")
    return GPIO.input(self.pin)

  def write(self, value):
    if self.mode != "out":
        raise ValueError("Cannot write to pin set as input.")
    GPIO.output(self.pin, value)
