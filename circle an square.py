import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((0,0,0))
    r = 255
    g = 0
    b = randint(120,255)
    center = (150,150)
    radius = 20
    c = 1

    for i in range(15):
        if c == 1:
            screen.draw.circle(center,radius,(r,g,b))
            radius += 10
            r = max(0, r - 10)
            g = min(255, g + 10)
            c = 2
        elif c == 2:
            x = center[0] - radius
            y = center[1] - radius

            screen.draw.rect(Rect((x,y), (radius * 2, radius * 2)), (r, g, b))
            radius += 10
            r = max(0, r - 10)
            g = min(255, g + 10)
            c = 1
        

pgzrun.go()