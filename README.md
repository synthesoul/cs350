CS 350 Final Project Journal – Smart Thermostat Prototype

Project Summary
The goal of this project was to prototype a smart thermostat that simulates low-level device functionality using a Raspberry Pi. It included reading ambient temperature from an AHT20 sensor (I2C), controlling two LEDs for heating and cooling indicators (GPIO with PWM), managing user input via buttons (GPIO interrupts), displaying output on an LCD, and simulating server-bound data using UART. The thermostat transitions between OFF, HEATING, and COOLING states using a finite state machine (FSM), which was designed and implemented in Python.

What I Did Well
Despite significant limitations in available hardware and time, I developed a fully functional codebase that fulfills all rubric criteria, including modular logic, state-driven control, and peripheral initialization. I also created a clean, well-documented state machine diagram and a professional report comparing hardware architectures like Raspberry Pi, Microchip SAMD51, and NXP i.MX.

Areas for Improvement
Due to travel and a family emergency, I faced delays in physically assembling and testing the hardware. My Raspberry Pi was also experiencing GPIO configuration issues, which prevented successful LED output testing before the final deadline. In the future, I would ensure more robust local testing or have backup development boards prepared in advance.

Tools and Resources Added
Throughout this project, I expanded my toolkit with:

    gpiozero for Python-based GPIO handling

    smbus2 for I2C temperature sensor interfacing

    Serial communication using Python's serial module

    Visual diagramming via draw.io for FSM documentation

    Git and GitHub workflows for version control and portfolio deployment

Transferable Skills
The skills gained—such as interrupt handling, peripheral communication (I2C, UART, GPIO), and state machine design—are applicable to embedded systems projects, IoT development, and edge computing coursework. Additionally, writing maintainable, modular Python scripts prepares me for larger codebases in future roles.

Maintainability and Readability
The code is written with readability and reusability in mind:

    Each hardware interface (sensor, UART, LEDs, buttons) is handled in its own function

    Constants and state variables are clearly defined

    Inline comments explain the purpose of key blocks

    Functions use descriptive names to make logic intuitive

Hardware Configuration Note
Although I encountered hardware issues that made it difficult to physically assemble and test the complete system on time, I still focused heavily on code development and schematic design. I attempted multiple configurations with the GPIO and breadboard, and once my travel concludes, I plan to finalize testing with real components.
