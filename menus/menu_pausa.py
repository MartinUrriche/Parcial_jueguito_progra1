import pygame
import config as config

def menu_pausa(eventos):
    #fondo
    config.pantalla.blit(config.fondo_menu_pausa_img,(0,0))

    #botones
    config.pantalla.blit(config.boton_jugar_img, config.boton_jugar)
    config.pantalla.blit(config.boton_salir_pausa_img, config.boton_salir_pausa)

    # --- MANEJO DE EVENTOS ---
    for evento in eventos:   # <<< USAMOS LOS EVENTOS QUE LLEGAN
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if config.boton_salir_pausa.collidepoint(evento.pos):
                print("SALIR")
                config.estado = "salir"

            if config.boton_jugar.collidepoint(evento.pos):
                config.pelota_superficie.topleft = config.nivel_guardado["pelota_pos"]
                config.velocidad_pelota = config.nivel_guardado["velocidad_pelota"]
                config.pelota_lanzada = config.nivel_guardado["pelota_lanzada"]
                config.estado = "Nivel_1"




