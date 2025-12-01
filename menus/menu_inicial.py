import pygame
import config


def menu_inicial(eventos):

    #fondo
    config.pantalla.blit(config.fondo_menu_inicial_img,(0,0))
    

    # Dibujar botones 
    config.pantalla.blit(config.boton_iniciar_img, config.boton_iniciar)
    config.pantalla.blit(config.boton_salir_img, config.boton_salir_inicial)

    # --- MANEJO DE EVENTOS ---
    for evento in eventos:   # <<< USAMOS LOS EVENTOS QUE LLEGAN
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if config.boton_salir_inicial.collidepoint(evento.pos):
                print("SALIR")
                config.estado = "salir"

            if config.boton_iniciar.collidepoint(evento.pos):
                config.estado = "Nivel_1"
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                config.estado = "Nivel_1"

