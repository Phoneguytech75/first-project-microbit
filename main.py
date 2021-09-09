def on_logo_long_pressed():
    basic.show_leds("""
        . . . . .
                . . . . .
                . # . # .
                # . . . #
                . # # # .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . # . # .
                # . . . #
                . # # # .
    """)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
                . # . # .
                . # . # .
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_string("EPIC")
    basic.show_leds("""
        . . . . .
                . # . # .
                . # . # .
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
""")