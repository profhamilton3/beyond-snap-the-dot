joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    catcher.change(LedSpriteProperty.Y, 1)
})
function isHit (sprite: game.LedSprite, chase: game.LedSprite) {
    if (sprite.isTouching(chase)) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        return true
    }
    return false
}
input.onButtonPressed(Button.A, function () {
    catcher.move(-1)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    catcher.move(1)
})
input.onButtonPressed(Button.AB, function () {
    catcher.change(LedSpriteProperty.Y, 1)
})
input.onButtonPressed(Button.B, function () {
    catcher.move(1)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    catcher.change(LedSpriteProperty.Y, -1)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    catcher.move(-1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    catcher.change(LedSpriteProperty.Y, -1)
})
let catcher: game.LedSprite = null
let sprite2 = game.createSprite(2, 2)
catcher = game.createSprite(4, 4)
let randomangle = 45
joystickbit.initJoystickBit()
basic.forever(function () {
    sprite2.move(1)
    basic.pause(25)
    sprite2.turn(Direction.Right, randomangle)
    basic.pause(100)
    sprite2.ifOnEdgeBounce()
    randomangle = randint(30, 320)
    isHit(sprite2, catcher)
})
control.inBackground(function () {
    while (true) {
        if (joystickbit.getRockerValue(joystickbit.rockerType.X) <= 200) {
            music.playTone(262, music.beat(BeatFraction.Half))
        }
        if (joystickbit.getRockerValue(joystickbit.rockerType.X) >= 800) {
            music.playTone(294, music.beat(BeatFraction.Half))
        }
        if (joystickbit.getRockerValue(joystickbit.rockerType.Y) >= 800) {
            music.playTone(494, music.beat(BeatFraction.Half))
        }
        if (joystickbit.getRockerValue(joystickbit.rockerType.Y) <= 200) {
            music.playTone(440, music.beat(BeatFraction.Half))
        }
    }
})
