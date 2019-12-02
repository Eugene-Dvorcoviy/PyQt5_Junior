import pygame

pygame.init()
SCREENSIZE = width, height = 500, 500
screen = pygame.display.set_mode(SCREENSIZE)
clock = pygame.time.Clock()
running = True
screen.fill((0, 0, 255))
fps = 60
x1, y1, r = 100, 100, 40
drawing = False
v = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 255))
            x1, y1 = event.pos
            drawing = True
            r = 0
    if drawing:
        pygame.draw.circle(screen, (255, 255, 0), (x1, y1), int(r))
        r += v / fps
    pygame.display.flip()

