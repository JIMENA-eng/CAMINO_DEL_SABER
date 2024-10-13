import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mover Triángulo con Pygame")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Coordenadas iniciales del triángulo
x = 350
y = 250

# Velocidad de movimiento
velocidad = 10

# Vértices del triángulo
punto1 = (x, y)  # Vértice superior
punto2 = (x - 50, y + 100)  # Vértice inferior izquierdo
punto3 = (x + 50, y + 100)  # Vértice inferior derecho

# Lista de los vértices del triángulo
vertices = [punto1, punto2, punto3]

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover el triángulo con las teclas de dirección
    if teclas[pygame.K_LEFT]:  # Tecla izquierda
        x -= velocidad
    if teclas[pygame.K_RIGHT]:  # Tecla derecha
        x += velocidad
    if teclas[pygame.K_UP]:  # Tecla arriba
        y -= velocidad
    if teclas[pygame.K_DOWN]:  # Tecla abajo
        y += velocidad

    # Actualizar los vértices del triángulo según la nueva posición
    punto1 = (x, y)
    punto2 = (x - 50, y + 100)
    punto3 = (x + 50, y + 100)
    vertices = [punto1, punto2, punto3]

    # Limpiar la ventana
    ventana.fill(BLANCO)

    # Dibujar el triángulo
    pygame.draw.polygon(ventana, AZUL, vertices)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la animación
    pygame.time.delay(20)
