import pygame
import config as config

def menu_principal():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            config.estado = "salir"


