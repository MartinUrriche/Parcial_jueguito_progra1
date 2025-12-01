import pygame

ANCHO, ALTO = 800, 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("No es plantas VS zombies")

font = pygame.font.SysFont("Arial", 40)

# Estado global del juego
estado = "menu_inicial"

# Botones menú inicial
boton_iniciar_img = pygame.image.load('assets/img botones/boton.iniciar.png').convert_alpha()
boton_iniciar = boton_iniciar_img.get_rect(center = (ANCHO // 2, ALTO // 2 - 50))


boton_salir_img = pygame.image.load('assets/img botones/boton.salir.png').convert_alpha()
boton_salir_inicial = boton_salir_img.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))

#fondo imagen menu incial
fondo_img = pygame.image.load('assets/img fondos/maxresdefault.jpg').convert_alpha()
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

#Fondo imagen menu pausa
fondo_menu_pausa_img = pygame.image.load('assets/img fondos/fondo_pausa.jpg').convert_alpha()
fondo_menu_pausa_img = pygame.transform.scale(fondo_menu_pausa_img,(ANCHO, ALTO))

#botones menu pausa
boton_jugar_img = pygame.image.load('assets/img botones/boton.jugar.png').convert_alpha()
boton_jugar = boton_jugar_img.get_rect(center = (ANCHO // 2, ALTO // 2 - 50))

boton_salir_pausa_img = pygame.image.load('assets/img botones/boton.salir.png').convert_alpha()
boton_salir_pausa = boton_salir_pausa_img.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))

#FONDO NIVEL_1
fondo_nivel_1 = pygame.image.load('assets/img personajes/kindpng_1950544.png').convert_alpha()
fondo_nivel_1 = pygame.transform.scale(fondo_nivel_1, (ANCHO, ALTO))

#girasol imagen
girasol_img = pygame.image.load('assets/img personajes/Girasol 2.1.png')
girasol_img = pygame.transform.scale(girasol_img, (100, 100))
girasol_superficie = girasol_img.get_rect(center = (ANCHO // 2, ALTO // 2 + 200))

#PELOTA IMAGEN
pelota_img = pygame.image.load('assets/img personajes/bala.png')
pelota_img = pygame.transform.scale(pelota_img, (20,20))
pelota_superficie = pelota_img.get_rect(center = (ANCHO // 2, girasol_superficie.top))
velocidad_pelota = [2, -2]
pelota_lanzada = False

#Vidas imagen
corazon_img = pygame.image.load('assets/img corazones/corazon.png')
corazon_img = pygame.transform.scale(corazon_img, (30,30))
corazones_superficie = [
    corazon_img.get_rect(topleft = (30, 50)),
    corazon_img.get_rect(topleft = (60, 50)),
    corazon_img.get_rect(topleft = (90, 50))
    ]
cantidad_vidas = 3

#Botones menú principal
boton_niveles  = pygame.Rect(300, 200, 200, 60)
boton_opciones = pygame.Rect(300, 280, 200, 60)
boton_creditos = pygame.Rect(300, 360, 200, 60)
boton_salir    = pygame.Rect(300, 440, 200, 60)

#Guardar nivel
nivel_guardado = {
    "pelota_pos": None,
    "velocidad_pelota": None,
    "pelota_lanzada": None
}

#creacion de enemigo
enemigos = []
nivel_1_cargado = False
def crear_bloque(x, y, tipo):
    bloque = {}

    if tipo == 1:
        bloque["vidas"] = 1
        bloque["imagenes"] = [
            'assets/img personajes/zombie_base.png'
        ]

    elif tipo == 2:
        bloque["vidas"] = 2
        bloque["imagenes"] = [
            'assets/img personajes/zombie_2.png',
            'assets/img personajes/zombie_base.png'
        ]

    elif tipo == 3:
        bloque["vidas"] = 3
        bloque["imagenes"] = [
            'assets/img personajes/zombie_3.png',
            'assets/img personajes/zombie_3_1.png',
            'assets/img personajes/zombie_base.png'
        ]

    # primera img cargada
    imagen_original = pygame.image.load(bloque["imagenes"][0]).convert_alpha()

    ancho = imagen_original.get_width() // 2
    alto = imagen_original.get_height() // 2

    bloque["imagen"] = pygame.transform.scale(imagen_original, (ancho, alto))
    bloque["rect"] = bloque["imagen"].get_rect(topleft=(x, y))
    bloque["indice_imagen"] = 0
    bloque["visible"] = True

    return bloque
