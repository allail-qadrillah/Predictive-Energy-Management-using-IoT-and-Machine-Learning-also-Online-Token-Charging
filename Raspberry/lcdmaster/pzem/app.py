import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

class PZEM:
  def __init__(self) -> None:
    # Connect to the slave
    self.serial = serial.Serial(
                       port='/dev/ttyS0',
                       baudrate=9600,
                       bytesize=8,
                       parity='N',
                       stopbits=1,
                       xonxoff=0
                      )
    self.master = modbus_rtu.RtuMaster(self.serial)
    self.master.set_timeout(2.0)
    self.master.set_verbose(True)
  
  def read(self):
    return self.master.execute(1, cst.READ_INPUT_REGISTERS, 0, 10)
  
  def get_voltage(self):
    """                                                         read voltage (V)"""
    return self.read()[0] / 10.0
  
  def get_current(self):
    """read current (A)"""
    return ( self.read()[1] + (self.read()[2] << 16) ) / 1000.0

  def get_power(self):
    """read power (W)"""
    return ( self.read()[3] + (self.read()[4] << 16) ) / 10.0 

  def get_energy(self):
    """read energy (Wh)"""
    return self.read()[5] + (self.read()[6] << 16)  

  def get_frekuensi(self):
    """read frekuensi (Hz)"""
    return ( self.read()[7] / 10.0 ) 
  
  def get_energy_kwh(self):
    """read energy (kWh)"""
    return ( self.get_power() * 24 ) / 10000.0 