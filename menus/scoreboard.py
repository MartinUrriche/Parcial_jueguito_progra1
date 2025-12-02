import pygame
import json
import config


def guardar_score(nombre, puntaje):
    """
    Guarda el nombre y puntaje en un JSON.
    Si el archivo no existe, lo crea.
    Mantiene solo el TOP 10.
    """
    try:
        with open(config.RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    datos.append({"nombre": nombre, "puntaje": puntaje})

    # Ordenar por puntaje DESC
    datos.sort(key=lambda x: x["puntaje"], reverse=True)

    # Mantener solo top 10
    datos = datos[:10]

    # Guardar
    with open(config.RUTA_JSON, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def menu_scoreboard(eventos):
    # Fondo scoreboard
    config.pantalla.blit(config.scoreboard_img, (0, 0))

    # Texto actual del jugador
    texto_nombre = config.scoreboard_font.render(config.scoreboard_aka, True, (255, 255, 0))
    config.pantalla.blit(texto_nombre, (250, 220))

    # Cursor parpadeante estilo arcade
    tiempo_actual = pygame.time.get_ticks()
    if (tiempo_actual // 500) % 2 == 0:  # parpadea cada 500ms
        x_cursor = 250 + texto_nombre.get_width() + 10
        pygame.draw.rect(config.pantalla, (255, 255, 0), (x_cursor, 230, 20, 5))

    # Procesar eventos del teclado
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:

            # ENTER -> guardar nombre y volver al menú
            if evento.key == pygame.K_RETURN and len(config.scoreboard_aka) > 0:
                print("AKA:", config.scoreboard_aka, " | tipo:", type(config.scoreboard_aka))
                print("PUNTAJE:", config.puntaje_actual, " | tipo:", type(config.puntaje_actual))
                guardar_score(config.scoreboard_aka, config.puntaje_actual)
                config.scoreboard_aka = ""
                config.estado = "menu_inicial"

            # BORRAR
            elif evento.key == pygame.K_BACKSPACE:
                config.scoreboard_aka = config.scoreboard_aka[:-1]

            # Agregar letras
            else:
                if len(config.scoreboard_aka) < 10:  # máximo 10 caracteres
                    caracter = evento.unicode.upper()

                    # Solo letras y números
                    if caracter.isalnum():
                        config.scoreboard_aka += caracter