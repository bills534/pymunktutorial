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


def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    delta_time = 1 / FPS

    space = pymunk.Space()
    space.gravity = (0, 981)

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