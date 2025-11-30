import pygame
import config as config

def menu_pausa(eventos):
    #fondo
    config.pantalla.blit(config.fondo_menu_pausa_img,(0,0))

    #botones
    config.pantalla.blit(config.boton_jugar_img, config.boton_jugar)
    config.pantalla.blit(config.boton_salir_img, config.boton_salir_inicial)

    # --- MANEJO DE EVENTOS ---
    for evento in eventos:   # <<< USAMOS LOS EVENTOS QUE LLEGAN
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if config.boton_salir_inicial.collidepoint(evento.pos):
                print("SALIR")
                config.estado = "salir"

            if config.boton_iniciar.collidepoint(evento.pos):
                config.estado = "Nivel 1"



