import pygame
import config

def reiniciar_nivel():
    config.velocidad_pelota, config.pelota_lanzada
    
    # Pelota quieta, en posición inicial (APOYADA EN EL GIRASOL)
    config.pelota_superficie.centerx = config.girasol_superficie.centerx
    config.pelota_superficie.bottom = config.girasol_superficie.top


def nivel_1(eventos):
    

    # Fondo del nivel
    config.pantalla.blit(config.fondo_nivel_1, (0, 0))

    # Rect de ejemplo como enemigo
    bloque_rect = pygame.Rect(400, 200, 30, 30)
    pygame.draw.rect(config.pantalla, (200, 50, 50), bloque_rect)  # visual para debug

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
                config.estado = "Menu_pausa"

        # Lanzar pelota con click
        if evento.type == pygame.MOUSEBUTTONDOWN and config.pelota_lanzada == False:
            config.pelota_lanzada = True

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

        # Si colsiona con el bloque gana (para probar)
        if config.pelota_superficie.colliderect(bloque_rect):
            reiniciar_nivel()
            config.estado = "menu_inicial"

        # Si toca el suelo pierde (para probar)
        if config.pelota_superficie.bottom >= config.ALTO:
            reiniciar_nivel()
            config.estado = "menu_inicial"
