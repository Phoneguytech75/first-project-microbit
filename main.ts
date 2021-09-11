input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    basic.showLeds(`
        . . . . .
                . . . . .
                . # . # .
                # . . . #
                . # # # .
    `)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
                . # . # .
                . # . # .
                # . . . #
                . # # # .
    `)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        . . . . .
                . # . # .
                . # . # .
                # . . . #
                . # # # .
    `)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.clearScreen()
    basic.showString("EASTER EGG")
    basic.showLeds(`
        . . . . .
                . # . # .
                . # . # .
                # . . . #
                . # # # .
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . # . # .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    `)
})
basic.showLeds(`
    . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
`)
