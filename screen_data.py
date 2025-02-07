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
comp_font = pygame.font.SysFont('Arial', 60)
label_font = pygame.font.SysFont('Arial', 25)

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

#z gate GUI
zgate_surface = pygame.Surface((28, 28), pygame.SRCALPHA, 32)
pygame.draw.rect(zgate_surface, (black), (0, 0, 28, 28), 2)
pygame.draw.rect(zgate_surface, (white), (2, 2, 24, 24))

zgate_text = my_font.render('Z', True, black)
zgate_surface.blit(zgate_text, (6, 2))

#cursor GUI
cursor_load = pygame.image.load("images/cursor.png")
cursor = pygame.transform.scale(cursor_load, (35, 35))

#half-note GUI
half_note_surface = pygame.Surface((28, 28), pygame.SRCALPHA, 32)
pygame.draw.ellipse(half_note_surface, black, (9, 11, 10, 8), 2)
pygame.draw.line(half_note_surface, black, (16, 15), (16, 0), 2)

#quarter-note GUI
quarter_note_surface = pygame.Surface((28, 28), pygame.SRCALPHA, 32)
pygame.draw.ellipse(quarter_note_surface, black, (9, 11, 10, 8))
pygame.draw.line(quarter_note_surface, black, (16, 15), (16, 0), 2)

#composer-text GUI
composer_text = comp_font.render('QHARMONY', True, white)