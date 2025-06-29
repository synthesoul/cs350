import time
import serial

# === Serial Setup ===
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print("Client started.")
print("Enter a number to control the LED:")
print("  1 - ON")
print("  2 - OFF")
print("  3 - EXIT")
print("  4 - QUIT")

command_map = {
    '1': 'ON',
    '2': 'OFF',
    '3': 'EXIT',
    '4': 'QUIT'
}

try:
    while True:
        choice = input("Select (1-4): ").strip()
        command = command_map.get(choice)

        if command:
            ser.write((command + '\n').encode('utf-8'))
            ser.flush()
            print(f"Sent: {command}")
            time.sleep(0.05)  # Optional pacing
            if command in ['EXIT', 'QUIT']:
                print("Exiting client...")
                break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

except KeyboardInterrupt:
    print("\nClient interrupted with CTRL-C. Exiting...")

finally:
    ser.close()
    print("Serial port closed.")
