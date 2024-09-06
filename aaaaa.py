import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego con Pygame")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Configuración del jugador (un cuadrado)
x, y = ancho // 2, alto // 2
velocidad = 5
tamaño = 50

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Movimiento del jugador
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Limitar el movimiento del jugador a los bordes de la pantalla
    x = max(0, min(ancho - tamaño, x))
    y = max(0, min(alto - tamaño, y))

    # Dibujar en pantalla
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, ROJO, (x, y, tamaño, tamaño))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    pygame.time.Clock().tick(60)
