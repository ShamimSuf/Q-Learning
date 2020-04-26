import pygame
import time
from random import randint
from numpy import deg2rad

from ray import *

#Game properties
WIDTH = 800
HEIGHT = 800
SCREEN = (WIDTH, HEIGHT)
AZURE4 = (131 ,139 ,139)
WHITE  = (255, 255, 255)
FPS = 60

#Pygame stuff
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SCREEN)

#Initialize walls array
line_1 = [randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT)]
line_2 = [randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT)]
line_3 = [randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT)]
line_4 = [randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT), randint(0, HEIGHT)]

line_5 = [1, 1, 1, HEIGHT-1]
line_6 = [1, HEIGHT-1, WIDTH-1, HEIGHT-1]
line_7 = [WIDTH-1, HEIGHT-1, WIDTH-1, 1]
line_8 = [WIDTH-1, 1, 1, 1]


wall_array = [line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8]
#wall_array = [line_1, line_2]

while True:
    screen.fill(AZURE4)

    for event in pygame.event.get():			
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    #display all walls
    for wall in wall_array:
        pygame.draw.line(screen, WHITE, (wall[0], wall[1]), (wall[2], wall[3]))


    #generate ray_array
    ray_array = []
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(0, 360, 4):
        ray_array.append(Ray(mouse_x, mouse_y, deg2rad(i)))
    
    for ray in ray_array:
        closest = 10000000
        closestpt = None
        for wall in wall_array:
            pt = ray.cast(wall)

            if pt is not None:
                dis = linalg.norm(pt - pygame.mouse.get_pos())
                if (dis < closest):
                    closest = dis
                    closestpt = pt

        if closestpt is not None:
            pygame.draw.line(screen, (255, 255, 255), pygame.mouse.get_pos(), array(closestpt, int), 2)

    pygame.display.update()
    clock.tick(FPS)

'''    
    #display only valid rays
    for ray in ray_array:
        for wall in wall_array: 
            hit_point = ray.cast(wall)
            if hit_point is not None :
                pygame.draw.line(screen, WHITE, ray.pos, array(hit_point, int), 2)
'''


'''
import pygame
import time
from numpy import deg2rad

from ray import *
from Limits import *

WIDTH = 800
HEIGHT = 800
SCREEN = (WIDTH, HEIGHT)
AZURE4 = (131 ,139 ,139)
FPS = 60

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(SCREEN)


limit = Limits(700, 50, 700, 700)

rays = []
for i in range(0, 360, 4):
    rays.append(Ray(WIDTH/2, HEIGHT/2, deg2rad(i)))

while True:
    screen.fill(AZURE4)

    for event in pygame.event.get():			
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    limit.display(screen)

    for ray in rays:
        hit_point = ray.display(screen)


    for ray in rays:
        hit_point = ray.cast(limit)
        if hit_point is not None :
            pygame.draw.line(screen, (255, 255, 255), ray.pos, array(hit_point, int), 2)


    pygame.display.update()
    clock.tick(FPS)
'''