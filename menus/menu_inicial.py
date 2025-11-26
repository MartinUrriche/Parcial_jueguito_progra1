import pygame
import config


def menu_inicial(eventos):

    #fondo
    config.pantalla.blit(config.fondo_img,(0,0))
    

    # Dibujar botones (IMÁGENES)
    config.pantalla.blit(config.boton_iniciar_img, config.boton_iniciar)
    config.pantalla.blit(config.boton_salir_img, config.boton_salir_inicial)

    # Obtener posición del mouse
    pos = pygame.mouse.get_pos()

    # HOVER para debug (cursor)
    pos_rect = pygame.Rect(pos[0], pos[1], 2, 5)
    pygame.draw.rect(config.pantalla, (255, 255, 255), pos_rect)

    # --- MANEJO DE EVENTOS ---
    for evento in eventos:   # <<< USAMOS LOS EVENTOS QUE LLEGAN
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if config.boton_salir_inicial.collidepoint(evento.pos):
                print("SALIR")
                config.estado = "salir"

            if config.boton_iniciar.collidepoint(evento.pos):
                config.estado = "Nivel 1"
