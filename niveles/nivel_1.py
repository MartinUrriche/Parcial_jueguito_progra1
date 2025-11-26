import pygame
import config

def nivel_1(eventos):
    config.pantalla.fill((50, 50, 50))

    config.pantalla.blit(config.girasol_img, config.girasol_superficie)
    config.pantalla.blit(config.bala_img, config.bala_superficie)

    texto = config.font.render("NIVEL 1", True, (255, 255, 255))
    config.pantalla.blit(texto, (config.ANCHO // 2 - 60, 50))

    bloque = pygame.Rect(200, 200, 100, 400)
    pelota = pygame.Rect(300, 400, 150, 399)
    velocidad_pelota = [5, -5]
    pelota_lanzada = False
    girasol_x = config.ANCHO // 2
    girasol_y = config.ALTO - 80

    clock = pygame.time.Clock() #---> Agregado para controlar los FPS
    for evento in eventos:
        if evento.type == pygame.QUIT:
            return "salir"  
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pelota_lanzada = True
#---> LOGICA DE LA PELOTA 

        if pelota_lanzada:
            pelota.x += velocidad_pelota[0] #mueve en x
            pelota.y += velocidad_pelota[1] #mueve en y

#---> rebote en los bordes
        if pelota.left <= 0 or pelota.right >= config.ANCHO:
            velocidad_pelota[0] *= -1

        if pelota.top <= 0: 
            velocidad_pelota[1] *= -1

# ---> si toca el bloque se rompe y ganas el nivel
        if pelota.colliderect(bloque):
            return "menu_inicial"
#---> rebote en el suelo
        if pelota.bottom >= config.ALTO:
            return "menu_inicial"

    #dibuja todo de nuevo
    config.pantalla.fill((50, 50, 50))
    config.pantalla.blit(texto, (config.ANCHO // 2 - 60, 50)) #dibuja el texto 
    pygame.draw.circle(config.pantalla, (255, 255, 0), (girasol_x, girasol_y), 30) #dibuja el girasol
    pygame.draw.ellipse(config.pantalla, (255, 255, 255), pelota)
    

    pygame.display.flip()
    clock.tick(60) #---> Limita a 60 FPS








