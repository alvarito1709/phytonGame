import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen_size = (800, 600)

# configuracion de los jugadores
player_width = 15
player_height = 90
# Jugador izquierdo
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0
# jugador derecho
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# puntaje
puntos_player1 = 0
puntos_player2 = 0

# pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

# colores de jugadores
color_jugador_1 = (0, 255, 0)
color_jugador_2 = (255, 0, 0)

screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

game_over = False

# def menu():
    # Dibuja el título del menú
  #  pygame.draw.rect(screen, (0, 0, 0), (200, 100, 400, 200), 2)
   # font = pygame.font.Font(None, 50)
    #texto = font.render("Menú de colores", True, (0, 0, 0))
    #screen.blit(texto, (250, 120))

    # Dibuja las opciones del menú
    #font = pygame.font.Font(None, 20)
    #texto = font.render("Color del jugador 1:", True, (0, 0, 0))
    #screen.blit(texto, (250, 200))
    #texto = font.render("Color del jugador 2:", True, (0, 0, 0))
    #screen.blit(texto, (250, 250))

    # Dibuja los rectángulos que rodean las opciones
    #pygame.draw.rect(screen, (0, 0, 0), (250, 220, 100, 20), 2)
    #pygame.draw.rect(screen, (0, 0, 0), (250, 270, 100, 20), 2)

    # Dibuja el cuadro de color
    #pygame.draw.rect(screen, (100, 100, 100), (250, 320, 100, 100))

# Función para dibujar el puntaje

def dibujar_puntaje():
    # Dibuja el puntaje del jugador 1
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, 100, 20))
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 100, 20), 2)
    font = pygame.font.Font(None, 20)
    texto = font.render(str(puntos_player1), True, (0, 0, 0))
    screen.blit(texto, (20, 15))

    # Dibuja el puntaje del jugador 2
    pygame.draw.rect(screen, (255, 0, 0), (700, 10, 100, 20))
    pygame.draw.rect(screen, (0, 0, 0), (700, 10, 100, 20), 2)
    font = pygame.font.Font(None, 20)
    text = font.render(str(puntos_player2), True, (0, 0, 0))
    screen.blit(text, (720, 15))


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        # Bucle para procesar los eventos del menú
       # if event.type == pygame.MOUSEBUTTONDOWN:
            # Si se hace clic en el rectángulo del color del jugador 1
           # if event.pos[0] > 250 and event.pos[0] < 350 and event.pos[1] > 220 and event.pos[1] < 240:
                # Obtiene el color del cuadro de color
              #  nuevo_color_jugador_1 = pygame.mouse.get_pos()
              #  nuevo_color_jugador_1 = screen.get_at(nuevo_color_jugador_1)
                # Actualiza el color del jugador 1
              #  color_jugador_1 = nuevo_color_jugador_1

            # Si se hace clic en el rectángulo del color del jugador 2
          #  if event.pos[0] > 250 and event.pos[0] < 350 and event.pos[1] > 270 and event.pos[1] < 290:
                # Obtiene el color del cuadro de color
             #   nuevo_color_jugador_2 = pygame.mouse.get_pos()
              #  nuevo_color_jugador_2 = screen.get_at(nuevo_color_jugador_2)
                # Actualiza el color del jugador 2
              #  color_jugador_2 = nuevo_color_jugador_2

        if event.type == pygame.KEYDOWN:
            # jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3

            # jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0

            # jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    # colision en eje vertical
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1

    # si la pelota sale del eje horizontal
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        puntos_player1 += 1

    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        puntos_player2 += 1


    # movimientos para jugadores y pelota
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    # pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    screen.fill(white)
    player1 = pygame.draw.rect(screen, color_jugador_1, (player1_x_coor, player1_y_coor, player_width, player_height))
    player2 = pygame.draw.rect(screen, color_jugador_2, (player2_x_coor, player2_y_coor, player_width, player_height))
    ball = pygame.draw.circle(screen, black, (pelota_x, pelota_y), 10)

    # Colisiones
    if ball.colliderect(player1) or ball.colliderect(player2):
        pelota_speed_x *= -1

    dibujar_puntaje()
    #menu()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
