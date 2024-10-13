import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación de Imagen Giratoria")

# Cargar imágenes
fondo = pygame.image.load("camino del saber/pantalla.png")
imagen = pygame.image.load("camino del saber/espiral2.png")

# Obtener el rectángulo de la imagen que gira
rect_imagen = imagen.get_rect(center=(ANCHO // 2, ALTO // 2))

# Variables para la rotación
angulo = 0

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Limpiar la ventana
    ventana.blit(fondo, (0, 0))  # Dibujar el fondo

    # Calcular la nueva imagen girada
    angulo += 1  # Incrementar el ángulo de rotación
    imagen_rotada = pygame.transform.rotate(imagen, angulo)
    rect_imagen = imagen_rotada.get_rect(center=rect_imagen.center)  # Actualizar el rectángulo

    # Dibujar la imagen girada
    ventana.blit(imagen_rotada, rect_imagen.topleft)

    # Actualizar la pantalla
    pygame.display.flip()
    pygame.time.delay(30)  # Controlar la velocidad de la animación
