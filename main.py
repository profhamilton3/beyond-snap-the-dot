def my_function():
    catcher.change(LedSpriteProperty.Y, 1)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def isHit(sprite: game.LedSprite, chase: game.LedSprite):
    if sprite.is_touching(chase):
        music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        return True
    return False

def on_button_pressed_a():
    catcher.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function2():
    catcher.move(1)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def on_button_pressed_ab():
    catcher.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    catcher.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function3():
    catcher.change(LedSpriteProperty.Y, -1)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    catcher.move(-1)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

def on_logo_pressed():
    catcher.change(LedSpriteProperty.Y, 1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

catcher: game.LedSprite = None
sprite2 = game.create_sprite(2, 2)
catcher = game.create_sprite(4, 4)
randomangle = 45
joystickbit.init_joystick_bit()

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

def on_in_background():
    while True:
            if joystickbit.get_rocker_value(joystickbit.rockerType.X) <= 200:
                music.play_tone(262, music.beat(BeatFraction.HALF))
            if joystickbit.get_rocker_value(joystickbit.rockerType.X) >= 800:
                music.play_tone(294, music.beat(BeatFraction.HALF))
            if joystickbit.get_button(joystickbit.JoystickBitPin.P12):
                music.play_tone(330, music.beat(BeatFraction.HALF))
            if joystickbit.get_button(joystickbit.JoystickBitPin.P13):
                music.play_tone(349, music.beat(BeatFraction.HALF))
            if joystickbit.get_button(joystickbit.JoystickBitPin.P14):
                music.play_tone(392, music.beat(BeatFraction.HALF))
            if joystickbit.get_button(joystickbit.JoystickBitPin.P15):
                music.play_tone(440, music.beat(BeatFraction.HALF))
            if joystickbit.get_rocker_value(joystickbit.rockerType.Y) >= 800:
                music.play_tone(494, music.beat(BeatFraction.HALF))
control.in_background(on_in_background)
