OnButton = False
reading = 0

def on_button_pressed_a():
    global OnButton, reading
    OnButton = True
    while True:
        reading = pins.analog_read_pin(AnalogPin.P2)
        while reading > 600 and OnButton == True:
            basic.pause(2000)
            pins.digital_write_pin(DigitalPin.P1, 1)
            basic.pause(1000)
            pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global OnButton
    OnButton = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global reading
    reading = pins.analog_read_pin(AnalogPin.P2)
    if reading > 700:
        basic.show_string("Low")
    elif reading <= 700 and reading > 550:
        basic.show_string("Med")
    elif reading <= 550:
        basic.show_string("Full")
basic.forever(on_forever)
