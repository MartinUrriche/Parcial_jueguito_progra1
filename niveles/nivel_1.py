import pygame
import config
import enemigo.enemigo as enemigo

def reiniciar_nivel():
    # Pelota quieta, en posición inicial 
    config.pelota_superficie.centerx = config.girasol_superficie.centerx
    config.pelota_superficie.bottom = config.girasol_superficie.top

    # Velocidad original del nivel
    config.velocidad_pelota = [3, -3]

    # bandera de si la pelota fue lanzada
    config.pelota_lanzada = False


def nivel_1(eventos):
    
    # Fondo del nivel
    config.pantalla.blit(config.fondo_nivel_1, (0, 0))

    # dibujar enemigo
    for bloque in config.enemigos:
        enemigo.dibujar_bloque(bloque)

    #Dibujar corazon
    for corazon in config.corazones_superficie:
        config.pantalla.blit(config.corazon_img, corazon)

    # Dibujar girasol
    config.pantalla.blit(config.girasol_img, config.girasol_superficie)

    # Mantener pelota arriba del girasol
    if config.pelota_lanzada == False:
        config.pelota_superficie.centerx = config.girasol_superficie.centerx
        config.pelota_superficie.bottom = config.girasol_superficie.top

    # Dibujar pelota
    config.pantalla.blit(config.pelota_img, config.pelota_superficie)

    # Título
    texto = config.font.render("NIVEL 1", True, (255, 255, 255))
    config.pantalla.blit(texto, (config.ANCHO // 2 - 60, 20))

    # ------ PROCESAR EVENTOS ------
    for evento in eventos:

        if evento.type == pygame.QUIT:
            config.estado = "salir"
        
        # Menu pausa
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                config.nivel_guardado["pelota_pos"] = config.pelota_superficie.topleft
                config.nivel_guardado["velocidad_pelota"] = config.velocidad_pelota.copy()
                config.nivel_guardado["pelota_lanzada"] = config.pelota_lanzada
                config.estado = "Menu_pausa"

        # Lanzar pelota con click
        if evento.type == pygame.MOUSEBUTTONDOWN and config.pelota_lanzada == False:
            config.pelota_lanzada = True

    teclas = pygame.key.get_pressed()

    # ------ LÓGICA DE LA PELOTA ------
    if config.pelota_lanzada:

        # Movimiento
        config.pelota_superficie.x += config.velocidad_pelota[0]
        config.pelota_superficie.y += config.velocidad_pelota[1]

        # Rebotes
        if config.pelota_superficie.left <= 0 or config.pelota_superficie.right >= config.ANCHO:
            config.velocidad_pelota[0] *= -1

        if config.pelota_superficie.top <= 0:
            config.velocidad_pelota[1] *= -1

        #movimiento girasol si la pelota se disparo
        if teclas[pygame.K_LEFT] and config.girasol_superficie.left > 0:
            config.girasol_superficie.x -= 7
        if teclas[pygame.K_RIGHT] and config.girasol_superficie.right < config.ANCHO:
            config.girasol_superficie.x += 7
        
        #rebote girasol
        if config.pelota_superficie.colliderect(config.girasol_superficie):
            config.pelota_superficie.bottom = config.girasol_superficie.top
            config.velocidad_pelota[1] *= -1

        # Si colsiona con el bloque gana (para probar)
        for bloque in config.enemigos:
            if bloque["visible"] and config.pelota_superficie.colliderect(bloque["rect"]):
                # Rebota
                config.velocidad_pelota[1] *= -1
                # Recibe daño
                enemigo.bloquear_recibir_golpe(bloque)

        # Si toca el suelo pierde (para probar)
        if config.pelota_superficie.bottom >= config.ALTO:
            config.cantidad_vidas -= 1
            if config.cantidad_vidas > 0:
                config.corazones_superficie.pop()
            if config.cantidad_vidas == 0:
                config.estado = "salir"
            reiniciar_nivel()
            
