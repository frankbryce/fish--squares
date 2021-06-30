def on_button_pressed_a():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # . . .
        # # # . .
        . # # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # # .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        . . # # .
        . # # # .
        . . # . .
        . . . . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . # # . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        . # # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . # # . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . . .
        # # # . .
        # # . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        # # . . .
        """)
    clear()
input.on_button_pressed(Button.A, on_button_pressed_a)

def clear():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)

def on_button_pressed_b():
    while True:
        basic.show_icon(IconNames.SQUARE)
        if input.button_is_pressed(Button.B):
            clear()
            break
        basic.show_icon(IconNames.SMALL_SQUARE)
        if input.button_is_pressed(Button.B):
            clear()
            break
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        if input.button_is_pressed(Button.B):
            clear()
            break
        basic.show_icon(IconNames.SMALL_SQUARE)
        if input.button_is_pressed(Button.B):
            clear()
            break
input.on_button_pressed(Button.B, on_button_pressed_b)
