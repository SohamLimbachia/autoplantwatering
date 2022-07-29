let OnButton = false
let reading = 0
input.onButtonPressed(Button.A, function () {
    OnButton = true
    while (true) {
        reading = pins.analogReadPin(AnalogPin.P2)
        while (reading > 700 && OnButton == true) {
            basic.pause(2000)
            pins.digitalWritePin(DigitalPin.P1, 1)
            basic.pause(1000)
            pins.digitalWritePin(DigitalPin.P1, 0)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    OnButton = false
})
basic.forever(function () {
    reading = pins.analogReadPin(AnalogPin.P2)
    if (reading > 700) {
        basic.showString("Low")
    } else if (reading <= 700 && reading > 550) {
        basic.showString("Med")
    } else if (reading <= 550) {
        basic.showString("Full")
    }
})
