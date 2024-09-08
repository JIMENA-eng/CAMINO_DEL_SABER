import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dado con Pygame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaño del dado
DICE_SIZE = 100
DICE_CENTER = (WIDTH // 2, HEIGHT // 2)

# Crear superficie para el dado
dice_surface = pygame.Surface((DICE_SIZE, DICE_SIZE))
dice_surface.fill(WHITE)

# Dibujar el dado
def draw_dice_face(face_number):
    # Limpiar la superficie
    dice_surface.fill(WHITE)
    
    # Dibujar los puntos del dado según el número de la cara
    dot_radius = 10
    dot_offset = DICE_SIZE // 4

    if face_number == 1:
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE // 2, DICE_SIZE // 2), dot_radius)
    elif face_number == 2:
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, DICE_SIZE - dot_offset), dot_radius)
    elif face_number == 3:
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE // 2, DICE_SIZE // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, DICE_SIZE - dot_offset), dot_radius)
    elif face_number == 4:
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, DICE_SIZE - dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, DICE_SIZE - dot_offset), dot_radius)
    elif face_number == 5:
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE // 2, DICE_SIZE // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, DICE_SIZE - dot_offset), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, DICE_SIZE - dot_offset), dot_radius)
    elif face_number == 6:
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, dot_offset + dot_offset // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, dot_offset + dot_offset // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, DICE_SIZE // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, DICE_SIZE // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (dot_offset, DICE_SIZE - dot_offset - dot_offset // 2), dot_radius)
        pygame.draw.circle(dice_surface, BLACK, (DICE_SIZE - dot_offset, DICE_SIZE - dot_offset - dot_offset // 2), dot_radius)

# Bucle principal del juego
clock = pygame.time.Clock()
face_number = random.randint(1, 6)  # Número inicial del dado

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                face_number = random.randint(1, 6)  # Lanzar el dado al presionar la barra espaciadora
                draw_dice_face(face_number)

    # Actualizar pantalla
    screen.fill(WHITE)
    screen.blit(dice_surface, (DICE_CENTER[0] - DICE_SIZE // 2, DICE_CENTER[1] - DICE_SIZE // 2))
    
    pygame.display.flip()
    clock.tick(30)  # Limitar a 30 fotogramas por segundo
