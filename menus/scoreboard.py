import pygame
import json
import config


def guardar_score(nombre, puntaje):
    try:
        with open(config.RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    # Agregar nuevo resultado (queda al final de los empates)
    datos.append({"nombre": nombre, "puntaje": puntaje})

    # Ordenar por puntaje (estable -> respeta orden de llegada en empates)
    datos.sort(key=lambda x: x["puntaje"], reverse=True)

    # Mantener solo los mejores 10
    datos = datos[:10]

    # Guardar en el archivo
    with open(config.RUTA_JSON, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def menu_scoreboard(eventos):
    # Iniciar música del scoreboard 
    if not getattr(config, "musica_score_activa", False):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(config.MUSICA_PUNTAJE)
        pygame.mixer.music.play(-1)
        config.musica_score_activa = True

    # Fondo scoreboard
    config.pantalla.blit(config.scoreboard_img, (0, 0))

    # -------- TEXTO QUE SE ESTÁ ESCRIBIENDO (ABAJO, MITAD DERECHA) --------
    texto_nombre = config.scoreboard_font.render(config.scoreboard_aka, True, (255, 255, 0))
    config.pantalla.blit(texto_nombre, (620, 560))

    # Cursor parpadeante estilo arcade
    tiempo_actual = pygame.time.get_ticks()
    if (tiempo_actual // 500) % 2 == 0:
        x_cursor = 620 + texto_nombre.get_width() + 10
        pygame.draw.rect(config.pantalla, (255, 255, 0), (x_cursor, 580, 20, 5))

    # -------- CARGAR SCORES DEL JSON --------
    try:
        with open(config.RUTA_JSON, "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    # -------- POSICIONES ALINEADAS CON TU IMAGEN (1ST ARRIBA) --------
    columna_score_x = 360
    columna_name_x = 560
    filas_y = [125, 145, 165, 185, 205, 225, 245, 265, 285, 305]

    # -------- DIBUJAR PUNTAJES Y NOMBRES --------
    for i, jugador in enumerate(datos):
        if i < 10:
            texto_score = config.scoreboard_font.render(
                str(jugador["puntaje"]), True, (255, 255, 255)
            )
            texto_nombre_rank = config.scoreboard_font.render(
                jugador["nombre"], True, (255, 255, 255)
            )

            config.pantalla.blit(texto_score, (columna_score_x, filas_y[i]))
            config.pantalla.blit(texto_nombre_rank, (columna_name_x, filas_y[i]))

    # -------- MANEJO DE TECLADO --------
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:

            # ENTER -> guardar nombre y volver al menú
            if evento.key == pygame.K_RETURN and len(config.scoreboard_aka) > 0:
                guardar_score(config.scoreboard_aka, config.puntaje_actual)
                config.scoreboard_aka = ""
                 # Detener música del scoreboard y volver al menú
                pygame.mixer.music.stop()
                config.musica_score_activa = False
                config.estado = "menu_inicial"

            # BORRAR
            elif evento.key == pygame.K_BACKSPACE:
                config.scoreboard_aka = config.scoreboard_aka[:-1]

            # Agregar letras y números
            else:
                if len(config.scoreboard_aka) < 10:
                    caracter = evento.unicode.upper()
                    if caracter.isalnum():
                        config.scoreboard_aka += caracter
