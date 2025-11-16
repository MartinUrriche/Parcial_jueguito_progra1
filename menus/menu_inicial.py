import pygame
import config

def menu_inicial():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            config.estado = "salir"

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if config.boton_iniciar.collidepoint(evento.pos):
                config.estado = "menu_principal"

    config.pantalla.fill((50, 50, 50))

    pygame.draw.rect(config.pantalla, (200, 200, 200), config.boton_iniciar)
    pygame.draw.rect(config.pantalla, (200, 200, 200), config.boton_salir_inicial)
    texto = config.font.render("INICIAR", True, (0, 0, 0))
    config.pantalla.blit(texto, (config.boton_iniciar.x + 35, config.boton_iniciar.y + 10))
    texto = config.font.render("SALIR", True, (0, 0, 0))
    config.pantalla.blit(texto, (config.boton_salir_inicial.x + 35, config.boton_salir_inicial.y + 10))
