sprite = game.create_sprite(2, 2)
catcher = game.create_sprite(4, 4)
def on_forever():
    sprite.move(1)
    sprite.turn(Direction.RIGHT, 45)
    sprite.if_on_edge_bounce()
basic.forever(on_forever)
