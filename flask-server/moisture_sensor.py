import smbus

# gets the moisture reading of the connected moisture sensor
def get_moisture_readings_from_channel () -> int:

    address = 0x48
    A0 = 0x40
    bus = smbus.SMBus(1)
    
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
    
    return value
    
if __name__ == "__main__":
    print(get_moisture_readings_from_channels())
