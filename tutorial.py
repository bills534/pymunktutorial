import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()


def create_boundaries(space, width, height):
    rects = [
        [(width/2, height - 10), (width, 20)],  #floor
        [(width/2, 10), (width, 20)],           # ceiling
        [(10, height/2), (20, height)],         # left
        [(width - 10, height/2), (20, height)]  # right
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)


def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300,300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.9
    shape.friction = 0.5
    shape.color = (255, 0, 0, 100)
    space.add(body, shape)
    return shape


def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    delta_time = 1 / FPS

    space = pymunk.Space()
    space.gravity = (0, 981)

    ball = create_ball(space, 30, 10)
    create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(space, window, draw_options)
        space.step(delta_time)
        clock.tick(FPS)
    
    pygame.quit()


if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)