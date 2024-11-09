def isHit(sprite: game.LedSprite, chase: game.LedSprite):
    if sprite.is_touching(chase):
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        return True
    return False

def on_button_pressed_a():
    catcher.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    catcher.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    catcher.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    catcher.change(LedSpriteProperty.Y, -1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

catcher: game.LedSprite = None
sprite2 = game.create_sprite(2, 2)
catcher = game.create_sprite(4, 4)
randomangle = 45
MaxTime = 5000

def on_forever():
    global randomangle
    sprite2.move(1)
    basic.pause(25)
    sprite2.turn(Direction.RIGHT, randomangle)
    basic.pause(100)
    sprite2.if_on_edge_bounce()
    randomangle = randint(30, 320)
    isHit(sprite2, catcher)
basic.forever(on_forever)
