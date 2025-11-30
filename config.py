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

#fondo imagen menu incial
fondo_img = pygame.image.load('menus/fondos/maxresdefault.jpg').convert_alpha()
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

#Fondo imagen menu pausa
fondo_menu_pausa_img = pygame.image.load('menus/fondos/fondo_pausa.jpg').convert_alpha()
fondo_menu_pausa_img = pygame.transform.scale(fondo_menu_pausa_img,(ANCHO, ALTO))

#botones menu pausa
boton_jugar_img = pygame.image.load('menus/botones/boton.jugar.png').convert_alpha()
boton_jugar = boton_jugar_img.get_rect(center = (ANCHO // 2, ALTO // 2 - 50))

#FONDO NIVEL_1
fondo_nivel_1 = pygame.image.load('personajes/kindpng_1950544.png').convert_alpha()
fondo_nivel_1 = pygame.transform.scale(fondo_nivel_1, (ANCHO, ALTO))

#girasol imagen
girasol_img = pygame.image.load('personajes/Girasol 2.1.png')
girasol_img = pygame.transform.scale(girasol_img, (100, 100))
girasol_superficie = girasol_img.get_rect(center = (ANCHO // 2, ALTO // 2 + 200))

#PELOTA IMAGEN
pelota_img = pygame.image.load('personajes/bala.png')
pelota_img = pygame.transform.scale(pelota_img, (20,20))
pelota_superficie = pelota_img.get_rect(center = (ANCHO // 2, girasol_superficie.top))
velocidad_pelota = [5, -5]
pelota_lanzada = False


# Botones menú principal
boton_niveles  = pygame.Rect(300, 200, 200, 60)
boton_opciones = pygame.Rect(300, 280, 200, 60)
boton_creditos = pygame.Rect(300, 360, 200, 60)
boton_salir    = pygame.Rect(300, 440, 200, 60)

#guardar nivel
nivel_guardado = {
    "pelota_pos": None,
    "velocidad_pelota": None,
    "pelota_lanzada": None
}


#Rectangulo personaje
#rectangulo_girasol =