from sense_emu import SenseHat
import time

sense = SenseHat()

def get_sensor_data():
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    return temperature, humidity

def check_warnings(temperature, humidity) :
    warnings = []
    if temperature > 40 :
        warnings.append("High Temperature Detected")
    if humidity > 90 :
        warnings.append("High Humidity Detected")
    return warnings

while True:
    temperature, humidity = get_sensor_data()
    warnings = check_warnings(temperature, humidity)
    time.sleep(5)