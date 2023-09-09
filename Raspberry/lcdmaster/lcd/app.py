from .progress import progress_bar
from .drivers.i2c_dev import Lcd

class LCD:

  def __init__(self) -> None:
    self.lcd = Lcd

  def display(self, text:str, line:int):
    return self.lcd.lcd_display_string(text, line)
  
  def progress_bar(self):
    return progress_bar()
  
  def clear(self):              
    return Lcd.lcd_clear()