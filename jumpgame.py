from ursina import *
from ursina import entity
from ursina import texture
from ursina.prefabs.first_person_controller \
    import FirstPersonController
from random import uniform

app = Ursina()
ground = Entity(model= 'plane', texture= 'grass', collider= 'mesh', scale= (100, 1, 100))
myBox = Entity(model= 'cube', color= color.black, collider= 'box', position= (15, 0.5, 5))
myBall = Entity(model= 'sphere', color= color.white, collider= 'sphere', position= (5, 0.5, 10))
goal = Entity(model = 'cube', color= color.gold, texture= 'white_cube', position= (0, 11, 55), scale= (10, 1, 10), collider= 'box')
pillar = Entity(model = 'cube', color= color.green, position= (0, 36, 58), scale= (1, 50, 1))

player = FirstPersonController(collider= 'box')
sky = Sky()
lvl = 1
jump = Audio('assets\jump.mp3', loop = False, autoplay = False)
walk = Audio('assets\walk.mp3', loop = False, autoplay = False)

blocks = []
directions = []
window.fullscreen = True

for i in range(10):
    r = uniform(-2,2)
    block = Entity(model= 'cube', color= color.dark_gray, texture= 'white_cube', position= (r, 1+i, 3+i*5), scale= (3, 0.5, 3), collider= 'box')
if r < 0:
    directions.append(1)
else:
    directions.append(-1)

blocks.append(block)

def update():
    global lvl
    i = 0
    for block in blocks:
        block.x -= directions[i]*time.dt
        if abs(block.x) > 5:
            directions [i] *= -1
        if block.intersects().hit:
            player.x -= directions[i]*time.dt
        i = i + 1
    if player.z > 56 and lvl == 1:
        lvl = 2
        sky.texture = 'sky_sunset'
    #walking = held_keys['w'] or held_keys ['a'] or held_keys['s'] or held_keys['d']
    #if walking and player.grounded:
        #if not walk.playing:
            #walk.play()
    #else:
        #if walk.playing:
        #walk.stop()

def input(key):
    if key == 'escape':
        quit()
    if key == 'space':
        if not jump.playing:
            jump.play()

app.run()