# BBC micro:bit (MakeCode Python)
# A+B starts/stops a square-wave output on P0.
# A lowers the speed setting; B raises it. The setting is 1..9.
# Each setting is about 5..45 pulses per second (higher is faster).
#
# P0 is a low-voltage 3.3 V logic output. Connect only to suitable low-voltage
# circuits and share GND. Never connect the micro:bit directly to mains or
# another voltage source. Use suitable driver circuitry for loads such as motors.

OUTPUT_PIN = DigitalPin.P0
speed = 1
running = False
output_state = 0
previous_a = False
previous_b = False
previous_ab = False

basic.show_number(speed)

while True:
    a_pressed = input.button_is_pressed(Button.A)
    b_pressed = input.button_is_pressed(Button.B)
    ab_pressed = a_pressed and b_pressed

    # Toggle only once per A+B press, not repeatedly while held.
    if ab_pressed and not previous_ab:
        running = not running
        output_state = 0
        pins.digital_write_pin(OUTPUT_PIN, 0)

    # Adjust the speed once per individual button press. A+B takes priority.
    if not ab_pressed:
        if a_pressed and not previous_a:
            speed = max(1, speed - 1)
            basic.show_number(speed)
        if b_pressed and not previous_b:
            speed = min(9, speed + 1)
            basic.show_number(speed)

    previous_a = a_pressed
    previous_b = b_pressed
    previous_ab = ab_pressed

    if running:
        # One high/low transition per half-period. At speed 1 this is about
        # 5 Hz; at speed 9 it is about 45 Hz.
        pins.digital_write_pin(OUTPUT_PIN, output_state)
        output_state = 1 - output_state
        basic.pause(100 // speed)
    else:
        pins.digital_write_pin(OUTPUT_PIN, 0)
        basic.pause(10)
