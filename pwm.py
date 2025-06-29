import RPi.GPIO as GPIO
import time

LED_PIN = 18  # Adjust if you use a different GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 100)  # 100Hz frequency
pwm.start(0)  # Start PWM with 0% duty cycle

try:
    while True:
        # Fade in
        for duty in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)
        # Fade out
        for duty in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()

