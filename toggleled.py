#!/usr/bin/env python3

def read_gpio():
    with open('/sys/devices/platform/pinctrl/ff230000.gpio/gpiochip2/gpio/gpio79/active_low', 'r') as file:
        return file.read().strip()

def write_gpio(state):
    with open('/sys/devices/platform/pinctrl/ff230000.gpio/gpiochip2/gpio/gpio79/active_low', 'w') as file:
        file.write(state)

def main():
    current_state = read_gpio()

    if current_state == '0':
        write_gpio('1')
    elif current_state == '1':
        write_gpio('0')
    else:
        print("Error: LED state is undefined.")

if __name__ == "__main__":
    main()
