import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

while True:
    pygame.event.pump()
    screen.fill("blue")
    pygame.draw.rect(screen, "red", (200, 200, 150, 250))
    pygame.display.update()
