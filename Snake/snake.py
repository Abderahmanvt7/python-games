from random import randint
from ursina import *

app = Ursina()

snake = Entity(model='cube', texture='snake', scale=0.4, z=-1, collider='box')
ground = Entity(model='cube', texture='grass', rotation=(90, 0, 0), scale=(5, 1, 5), z=1)
apple = Entity(model='cube', texture='apple', scale=0.4, position=(1, -1, -1), collider='mesh')
body = [Entity(model='cube', scale=0.2, texture='body') for _ in range(14)]

camera.orthographic = True
camera.fov = 8

dx = dy = 0


def update():
    info = snake.intersects()
    if info.hit:
        apple.x = randint(-4, 4)/2
        apple.y = randint(-4, 4)/2
        new = Entity(model='cube', z=-1, scale=0.2, texture='body')
        body.append(new)
    for i in range(len(body)-1, 0, -1):
        pos = body[i-1].position
        body[i].position = pos
    body[0].x = snake.x
    body[0].y = snake.y
    snake.x += time.dt * dx
    snake.y += time.dt * dy


def input(key):
    global dx, dy
    if key == 'right arrow':
        snake.rotation_z = 0
        dx = 2
        dy = 0
    elif key == 'left arrow':
        snake.rotation_z = 180
        dx = -2
        dy = 0
    elif key == 'up arrow':
        snake.rotation_z = 90
        dx = 0
        dy = 2
    elif key == 'down arrow':
        snake.rotation_z = 270
        dx = 0
        dy = -2


app.run()
