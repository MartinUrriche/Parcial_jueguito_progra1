import pygame

ANCHO, ALTO = 800, 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("No es plantas VS zombies")

font = pygame.font.SysFont("Arial", 40)

# Estado global del juego
estado = "menu_inicial"

# Botones menú inicial
boton_iniciar = pygame.Rect(300, ALTO/2-100, 200, 60)
boton_salir_inicial = pygame.Rect(300, ALTO/2+25, 200, 60)

# Botones menú principal
boton_niveles  = pygame.Rect(300, 200, 200, 60)
boton_opciones = pygame.Rect(300, 280, 200, 60)
boton_creditos = pygame.Rect(300, 360, 200, 60)
boton_salir    = pygame.Rect(300, 440, 200, 60)