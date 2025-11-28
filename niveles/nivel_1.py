import pygame
import config

def reiniciar_nivel():
    config.velocidad_pelota, config.pelota_lanzada
    
    # Pelota quieta, en posición inicial (APOYADA EN EL GIRASOL)
    config.bala_superficie.centerx = config.girasol_superficie.centerx
    config.bala_superficie.bottom = config.girasol_superficie.top

    pelota_lanzada = False
    velocidad_pelota = [5, -5]  # velocidad inicial

def nivel_1(eventos):
    

    # Fondo del nivel
    config.pantalla.blit(config.fondo_nivel_1, (0, 0))

    # Bloque (usamos un rect con imagen para simplificar)
    bloque_rect = pygame.Rect(200, 200, 120, 120)
    pygame.draw.rect(config.pantalla, (200, 50, 50), bloque_rect)  # visual para debug

    # Dibujar girasol
    config.pantalla.blit(config.girasol_img, config.girasol_superficie)

    # Si la pelota NO fue lanzada, mantenerla arriba del girasol
    if not config.pelota_lanzada:
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

        # Lanzar pelota con click
        if evento.type == pygame.MOUSEBUTTONDOWN and not config.pelota_lanzada:
            pelota_lanzada = True

    # ------ LÓGICA DE LA PELOTA ------
    if config.pelota_lanzada:

        # Movimiento
        config.bala_superficie.x += config.velocidad_pelota[0]
        config.bala_superficie.y += config.velocidad_pelota[1]

        # Rebote en bordes laterales
        if config.bala_superficie.left <= 0 or config.bala_superficie.right >= config.ANCHO:
            config.velocidad_pelota[0] *= -1

        # Rebote en el techo
        if config.bala_superficie.top <= 0:
            config.velocidad_pelota[1] *= -1

        # Colisión con bloque → GANASTE
        if config.bala_superficie.colliderect(bloque_rect):
            reiniciar_nivel()
            config.estado = "menu_inicial"
            return

        # Si toca el suelo → PERDISTE
        if config.bala_superficie.bottom >= config.ALTO:
            reiniciar_nivel()
            config.estado = "menu_inicial"
            return
