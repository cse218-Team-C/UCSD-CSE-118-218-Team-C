import RPi.GPIO as GPIO

# gets the moisture reading of a list of sensors, 
#  connected at the channels identified by in_channels
# the default value is arbitrary and used only for debugging
def get_moisture_readings_from_channels (in_channels: list[int] = [17]) -> dict[int, float]:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in_channels, GPIO.IN)
    
    moisture_readings: dict[int, float] = {}
    
    for channel in in_channels:
        moisture_readings[channel] = GPIO.input(channel)
    
    GPIO.cleanup()
    
    return moisture_readings
    
if __name__ == "__main__":
    print(get_moisture_readings_from_channels())
