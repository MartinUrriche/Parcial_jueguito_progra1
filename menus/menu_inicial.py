
import pygame

import config

def menu_inicial():
    config.pantalla.fill((50, 50, 50))

    pygame.draw.rect(config.pantalla, (200, 200, 200), config.boton_iniciar)
    pygame.draw.rect(config.pantalla, (200, 200, 200), config.boton_salir_inicial)
    texto = config.font.render("INICIAR", True, (0, 0, 0))
    config.pantalla.blit(texto, (config.boton_iniciar.x + 35, config.boton_iniciar.y + 10))
    texto = config.font.render("SALIR", True, (0, 0, 0))
    #config.pantalla.blit(texto, (config.boton_salir_inicial.x + 35, config.boton_salir_inicial.y + 10))
    pos = pygame.mouse.get_pos()
    pos_rect = pygame.Rect(pos[0], pos[1], 2, 5)
    pygame.draw.rect(config.pantalla, (255, 255, 255), pos_rect)
    print(
        "dimension boton_salir_inicial: x1:" + str(config.boton_salir_inicial.left),
            ", y1: " + str(config.boton_salir_inicial.left + config.boton_salir_inicial.width) + 
            ", x2: " + str(config.boton_salir_inicial.top) + 
            ", y2: " + str(config.boton_salir_inicial.top + config.boton_salir_inicial.height)
    )
    print("dimension pos: " + str(pos))
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pos_rect.colliderect(config.boton_salir_inicial):
                config.estado = "salir"
                print("salir")
        if config.boton_salir_inicial.colliderect((pos[0],pos[1],1,1)):
            print("estpoy en el botom")
                

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if config.boton_iniciar.collidepoint(evento.pos):
                config.estado = "menu_principal"

    
