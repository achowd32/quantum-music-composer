import pygame
pygame.init()

#screen dimensions
size = width, height = 960, 720

#colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

#fonts
my_font = pygame.font.SysFont('Arial', 20)

#hadamard gate GUI

hadamard_surface = pygame.Surface((28, 28), pygame.SRCALPHA, 32)
pygame.draw.rect(hadamard_surface, (black), (0, 0, 28, 28), 2)
pygame.draw.rect(hadamard_surface, (white), (2, 2, 24, 24))

hadamard_text = my_font.render('H', True, black)
hadamard_surface.blit(hadamard_text, (6, 2))

#x gate GUI

xgate_surface = pygame.Surface((28, 28), pygame.SRCALPHA, 32)
pygame.draw.rect(xgate_surface, (black), (0, 0, 28, 28), 2)
pygame.draw.rect(xgate_surface, (white), (2, 2, 24, 24))

xgate_text = my_font.render('X', True, black)
xgate_surface.blit(xgate_text, (6, 2))