input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . . .
        # # # . .
        . # # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . . # # .
        . . . . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . # # .
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . # # . .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        . # # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . # # . .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # . . .
        # # # . .
        # # . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        # # . . .
        `)
    clear()
})
function clear () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onButtonPressed(Button.B, function () {
    while (true) {
        basic.showIcon(IconNames.Square)
        if (input.buttonIsPressed(Button.B)) {
            clear()
            break;
        }
        basic.showIcon(IconNames.SmallSquare)
        if (input.buttonIsPressed(Button.B)) {
            clear()
            break;
        }
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        if (input.buttonIsPressed(Button.B)) {
            clear()
            break;
        }
        basic.showIcon(IconNames.SmallSquare)
        if (input.buttonIsPressed(Button.B)) {
            clear()
            break;
        }
    }
})
