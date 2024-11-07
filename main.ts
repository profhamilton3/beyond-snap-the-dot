input.onButtonPressed(Button.A, function () {
    catcher.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    catcher.change(LedSpriteProperty.Y, -1)
})
input.onButtonPressed(Button.B, function () {
    catcher.move(1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    catcher.change(LedSpriteProperty.Y, 1)
})
let catcher: game.LedSprite = null
let sprite = game.createSprite(2, 2)
catcher = game.createSprite(4, 4)
basic.forever(function () {
    sprite.move(1)
    basic.pause(25)
    sprite.turn(Direction.Right, 45)
    basic.pause(100)
    sprite.ifOnEdgeBounce()
})
