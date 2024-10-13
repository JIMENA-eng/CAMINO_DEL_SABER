import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO = 400
ALTO = 400
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dado con Pygame")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Tamaño del dado
TAMANO_DADO = 150
BORDES = 10  # Grosor de los bordes del dado

# Función para dibujar el dado
def dibujar_dado(numero, x, y):
    # Dibujar el fondo del dado (un cuadrado)
    pygame.draw.rect(screen, BLANCO, (x, y, TAMANO_DADO, TAMANO_DADO))
    pygame.draw.rect(screen, NEGRO, (x, y, TAMANO_DADO, TAMANO_DADO), BORDES)  # Borde negro
    
    # Posiciones de los puntos (distribución clásica de un dado)
    puntos = []
    
    if numero == 1:
        puntos = [(x + TAMANO_DADO // 2, y + TAMANO_DADO // 2)]  # Un punto en el centro
    elif numero == 2:
        puntos = [(x + TAMANO_DADO // 4, y + TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4)]  # Dos puntos en diagonal
    elif numero == 3:
        puntos = [(x + TAMANO_DADO // 2, y + TAMANO_DADO // 2),  # Punto central
                  (x + TAMANO_DADO // 4, y + TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4)]  # Diagonal
    elif numero == 4:
        puntos = [(x + TAMANO_DADO // 4, y + TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + TAMANO_DADO // 4),  # Esquinas superiores
                  (x + TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4)]  # Esquinas inferiores
    elif numero == 5:
        puntos = [(x + TAMANO_DADO // 2, y + TAMANO_DADO // 2),  # Punto central
                  (x + TAMANO_DADO // 4, y + TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + TAMANO_DADO // 4),  # Esquinas superiores
                  (x + TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4)]  # Esquinas inferiores
    elif numero == 6:
        puntos = [(x + TAMANO_DADO // 4, y + TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + TAMANO_DADO // 4),  # Columna superior
                  (x + TAMANO_DADO // 4, y + TAMANO_DADO // 2), (x + 3 * TAMANO_DADO // 4, y + TAMANO_DADO // 2),  # Columna del medio
                  (x + TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4), (x + 3 * TAMANO_DADO // 4, y + 3 * TAMANO_DADO // 4)]  # Columna inferior
    
    # Dibujar los puntos
    for punto in puntos:
        pygame.draw.circle(screen, NEGRO, punto, 10)

# Bucle principal
running = True
numero_dado = random.randint(1, 6)  # Inicializar el número del dado aleatoriamente
while running:
    screen.fill(ROJO)  # Fondo rojo
    
    # Dibujar el dado con el número aleatorio
    dibujar_dado(numero_dado, (ANCHO - TAMANO_DADO) // 2, (ALTO - TAMANO_DADO) // 2)

    # Actualizar pantalla
    pygame.display.flip()

    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Cuando presionamos la tecla de espacio, tiramos el dado
                numero_dado = random.randint(1, 6)  # Generar un número aleatorio entre 1 y 6

# Salir de pygame
pygame.quit()
sys.exit()
