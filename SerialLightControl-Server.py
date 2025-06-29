import serial
import RPi.GPIO as GPIO
import time

# === GPIO Setup ===
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# === Serial Setup ===
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
ser.flush()

state = "IDLE"
print("Server started. Awaiting commands: ON, OFF, EXIT, QUIT")

try:
    while True:
        if ser.in_waiting > 0:
            time.sleep(0.05)  # Allow buffer to fill
            raw = ser.readline()
            try:
                line = raw.decode('utf-8').strip().upper()
                if not line:
                    continue
            except UnicodeDecodeError:
                print(f"Received unreadable bytes: {raw}")
                continue

            print(f"Received: {line}")

            if line == "ON":
                GPIO.output(LED_PIN, GPIO.HIGH)
                state = "LED_ON"
            elif line == "OFF":
                GPIO.output(LED_PIN, GPIO.LOW)
                state = "LED_OFF"
            elif line in ["EXIT", "QUIT"]:
                state = "EXIT"
                break
            else:
                print("Unknown command")

            if state == "LED_ON":
                print("State: LED_ON - LED is ON")
            elif state == "LED_OFF":
                print("State: LED_OFF - LED is OFF")
            elif state == "EXIT":
                print("State: EXIT - Exiting program")

        else:
            time.sleep(0.1)

except Exception as e:
    print(f"Error: {e}")

finally:
    GPIO.cleanup()
    ser.close()
    print("Shutdown complete. GPIO cleaned up.")
