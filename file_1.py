import pygame


number = input()
w, hue = int(number.split()[0]), int(number.split()[1])
h = int(255 / 360 * hue)
pygame.init()
screen = pygame.display.set_mode((300, 300))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (int(h * 0.75), 0, 0), ((100, 100), (w, w)))
    pygame.draw.polygon(screen, (h, 0, 0), ((100, 100), (int(100 + w * 0.5), int(100 - w * 0.5)),
                                            (int(100 + w * 1.5), int(100 - w * 0.5)),
                                            (100 + w, 100)))
    pygame.draw.polygon(screen, (int(h * 0.5), 0, 0), ((100 + w, 100), (int(100 + w * 1.5), int(100 - w * 0.5)),
                                                       (int(100 + w * 1.5), int(100 + w * 0.5)),
                                                       (100 + w, 100 + w)))
    pygame.display.flip()

pygame.quit()