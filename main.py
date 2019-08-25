import pygame
import random

SCREEN_SIZE = (400, 300)

BALL_VERTICAL_SPEED = 100  # pixels per second
BALL_RADIUS = 10  # pixels

screen = None
static_canvas = None
dynamic_balls = None


def get_random_color():
    return random.random() * 255, random.random() * 255, random.random() * 255


def setup():
    global screen, static_canvas, dynamic_balls

    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    static_canvas = pygame.Surface(SCREEN_SIZE)
    dynamic_balls = list()


def loop(dt, events):

    for event in events:
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONUP:
            dynamic_balls.append([*event.pos, get_random_color()])

    screen.blit(static_canvas, (0, 0))

    for ball in dynamic_balls:
        ball[1] += BALL_VERTICAL_SPEED * dt / 1000
        if ball[1] + BALL_RADIUS >= SCREEN_SIZE[1]:
            pygame.draw.circle(static_canvas, ball[2], (int(ball[0]), int(ball[1])), BALL_RADIUS)
            dynamic_balls.remove(ball)
        else:
            pygame.draw.circle(screen, ball[2], (int(ball[0]), int(ball[1])), BALL_RADIUS)

    return True


def clear():
    pygame.quit()


clock = pygame.time.Clock()
setup()
while True:
    events = pygame.event.get()
    dt = clock.tick()
    if not loop(dt, events):
        break
    pygame.display.flip()

clear()
