import time
import serial
from gpiozero import LED, Button, PWMLED
import board
import busio
import adafruit_ahtx0
from datetime import datetime

# I2C Setup for AHT2 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

# UART serial output (simulates cloud communication)
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# GPIO output: LEDs
led_heat = PWMLED(17)  # Heating indicator (GPIO 17)
led_cool = PWMLED(27)  # Cooling indicator (GPIO 27)

# GPIO input: Buttons
toggle_button = Button(22)    # Toggle between OFF/HEATING/COOLING
increase_button = Button(5)   # Increase temp setpoint
decrease_button = Button(6)   # Decrease temp setpoint

# State machine
states = ["OFF", "HEATING", "COOLING"]
state_index = 0
state = states[state_index]

setpoint = 72.0  # Initial temperature setpoint in Fahrenheit

# --- Button interrupt handlers ---
def toggle_state():
    global state_index, state
    state_index = (state_index + 1) % 3
    state = states[state_index]

def increase_temp():
    global setpoint
    setpoint += 1

def decrease_temp():
    global setpoint
    setpoint -= 1

# Register button callbacks
toggle_button.when_pressed = toggle_state
increase_button.when_pressed = increase_temp
decrease_button.when_pressed = decrease_temp

# --- Main control loop ---
def main():
    while True:
        try:
            temp_c = sensor.temperature
            temp_f = temp_c * 9/5 + 32
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Send UART message
            uart.write(f"{now} | Mode: {state} | Temp: {temp_f:.2f}°F | Setpoint: {setpoint}°F\n".encode())

            if state == "HEATING":
                led_cool.value = 0
                if temp_f < setpoint:
                    led_heat.pulse()
                elif temp_f == setpoint:
                    led_heat.value = 1
                else:
                    led_heat.value = 0

            elif state == "COOLING":
                led_heat.value = 0
                if temp_f > setpoint:
                    led_cool.pulse()
                elif temp_f == setpoint:
                    led_cool.value = 1
                else:
                    led_cool.value = 0

            else:  # OFF
                led_heat.value = 0
                led_cool.value = 0

            time.sleep(1)

        except Exception as e:
            print("Error:", e)
            time.sleep(2)

main()
