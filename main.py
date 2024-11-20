#next steps: fix dimension, add a compile button and compile the quantum circuit

#initialise 

from qiskit import *
import pygame
import circuits

import screen_data
width = screen_data.width
height = screen_data.height
comp_width = width*0.9
comp_height = height*0.4+32
y_offset = 32

pygame.display.init()
screen = pygame.display.set_mode((width, height))

#set up 2D array for circuit

cur_x = 0
cur_y = 0
circ_grid = circuits.CircuitGrid(9, 18)

#baseline template for composer:

combined_shape = pygame.Surface((comp_width, comp_height))
pygame.draw.rect(combined_shape, screen_data.white, pygame.Rect((0, 0), (comp_width, comp_height)))
for x in range(1, 10):
    pygame.draw.line(combined_shape, screen_data.black, (0, y_offset*x), (comp_width, y_offset*x), 2)

#baseline template for quantum gates and music surfaces:

gates_surface = pygame.Surface((comp_width, comp_height), pygame.SRCALPHA, 32)
music_surface = pygame.Surface((comp_width, comp_height), pygame.SRCALPHA, 32)

#loop and check events:

while True:
    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                if circ_grid.get_gate(cur_x, cur_y) == "":
                    circ_grid.set_gate(cur_x, cur_y, "H")
                    gates_surface.blit(screen_data.hadamard_surface, (48*(cur_x), y_offset*(cur_y)+18))
                    music_surface.blit(screen_data.half_note_surface, (48*(cur_x), y_offset*(cur_y)+18))
                elif circ_grid.get_gate(cur_x, cur_y) == "H":
                    circ_grid.set_gate(cur_x, cur_y, "")
                    pygame.draw.rect(gates_surface, pygame.SRCALPHA, pygame.Rect(48*(cur_x), y_offset*(cur_y)+18, 28, 28))
                    pygame.draw.rect(music_surface, pygame.SRCALPHA, pygame.Rect(48*(cur_x), y_offset*(cur_y)+18, 28, 28))
            if event.key == pygame.K_x:
                if circ_grid.get_gate(cur_x, cur_y) == "":
                    circ_grid.set_gate(cur_x, cur_y, "X")
                    gates_surface.blit(screen_data.xgate_surface, (48*(cur_x), y_offset*(cur_y)+18))
                    music_surface.blit(screen_data.quarter_note_surface, (48*(cur_x), y_offset*(cur_y)+18))
                elif circ_grid.get_gate(cur_x, cur_y) == "X":
                    circ_grid.set_gate(cur_x, cur_y, "")
                    pygame.draw.rect(gates_surface, pygame.SRCALPHA, pygame.Rect(48*(cur_x), y_offset*(cur_y)+18, 28, 28))
                    pygame.draw.rect(music_surface, pygame.SRCALPHA, pygame.Rect(48*(cur_x), y_offset*(cur_y)+18, 28, 28))
            if event.key == pygame.K_z:
                if circ_grid.get_gate(cur_x, cur_y) == "":
                    circ_grid.set_gate(cur_x, cur_y, "Z")
                    gates_surface.blit(screen_data.zgate_surface, (48*(cur_x), y_offset*(cur_y)+18))
                elif circ_grid.get_gate(cur_x, cur_y) == "Z":
                    circ_grid.set_gate(cur_x, cur_y, "")
                    pygame.draw.rect(gates_surface, pygame.SRCALPHA, pygame.Rect(48*(cur_x), y_offset*(cur_y)+18, 28, 28))
            if event.key == pygame.K_s:
                cur_y = min(cur_y + 1, 8)
            if event.key == pygame.K_w:
                cur_y = max(cur_y - 1, 0)
            if event.key == pygame.K_d:
                cur_x = min(cur_x + 1, 17)
            if event.key == pygame.K_a:
                cur_x = max(cur_x - 1, 0)
            if event.key == pygame.K_RETURN:
                circ_grid.compile()
    #fill screen, make black bg
    screen.fill(screen_data.black)
    #initialise circuit composer
    circuit_comp = combined_shape.copy()
    circuit_comp.blit(gates_surface, (0, 0))
    circuit_comp.blit(screen_data.cursor, (48*(cur_x)-4, y_offset*(cur_y)+14))
    #initialise music composer
    music_comp = combined_shape.copy()
    music_comp.blit(music_surface, (0, 0))
    music_comp.blit(screen_data.cursor, (48*(cur_x)-4, y_offset*(cur_y)+14))
    #draw composer to screen
    screen.blit(circuit_comp, (width*0.05, 0))
    screen.blit(music_comp, (width*0.05, 400))
    #update
    pygame.display.flip()