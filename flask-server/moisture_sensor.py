import smbus

def get_moisture_readings_from_channel () -> int:
    """
    This function gets the moisture readings from the sensor.
    It uses the SMBus library to communicate with the I2C device.
    The value is then returned by the function.
    """
    address = 0x48
    A0 = 0x40
    bus = smbus.SMBus(1)
    
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
    
    return value
    
if __name__ == "__main__":
    print(get_moisture_readings_from_channels())
