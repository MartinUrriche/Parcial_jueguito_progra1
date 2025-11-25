import pygame

ANCHO, ALTO = 800, 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("No es plantas VS zombies")

font = pygame.font.SysFont("Arial", 40)

# Estado global del juego
estado = "menu_inicial"

# Botones menú inicial
boton_iniciar_img = pygame.image.load('menus/botones/boton.iniciar.png').convert_alpha()
boton_iniciar = boton_iniciar_img.get_rect(center = (ANCHO // 2, ALTO // 2 - 50))


boton_salir_img = pygame.image.load('menus/botones/boton.salir.png').convert_alpha()
boton_salir_inicial = boton_salir_img.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))


# Botones menú principal
boton_niveles  = pygame.Rect(300, 200, 200, 60)
boton_opciones = pygame.Rect(300, 280, 200, 60)
boton_creditos = pygame.Rect(300, 360, 200, 60)
boton_salir    = pygame.Rect(300, 440, 200, 60)



#Rectangulo personaje
#rectangulo_girasol =