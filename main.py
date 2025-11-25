import pygame
import config
import menus.menu_inicial as menu_inicial

pygame.init()

corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    eventos = pygame.event.get()

    # Procesar QUIT global
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Estados
    if config.estado == "salir":
        pygame.quit()
        exit()

    elif config.estado == "menu_inicial":
        menu_inicial.menu_inicial(eventos)

    elif config.estado == "Nivel 1":
        import niveles.nivel_1 as nivel_1
        nuevo = nivel_1.nivel_1()
        config.estado = nuevo 
    

    pygame.display.flip()
    reloj.tick(60)

