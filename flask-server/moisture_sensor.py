import RPi.GPIO as GPIO
import smbus

# gets the moisture reading of a list of sensors, 
#  connected at the channels identified by in_channels
# the default value is arbitrary and used only for debugging
def get_moisture_readings_from_channels (in_channels: list[int] = [17]) -> dict[int, float]:

    address = 0x48
    A0 = 0x40
    bus = smbus.SMBus(1)
    
    moisture_readings: dict[int, float] = {}
    
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
    
    for channel in in_channels:
        moisture_readings[channel] = value
    
    return moisture_readings
    
if __name__ == "__main__":
    print(get_moisture_readings_from_channels())
