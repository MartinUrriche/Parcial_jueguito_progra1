import pygame
import config  as config
import menus.menu_inicial as menu_inicial


pygame.init()

corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif config.estado == "salir":
            corriendo = False
        elif config.estado == "menu_inicial":
            menu_inicial.menu_inicial()
        pygame.display.flip()
        reloj.tick(60)
        
