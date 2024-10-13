
import pygame
import imageio

# Inicializa Pygame
pygame.init()

# Configuración para pantalla completa
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Esto hace que la ventana sea pantalla completa
WIDTH, HEIGHT = screen.get_size()  # Obtiene el tamaño de la pantalla completa

# Cargar el GIF usando imageio
gif_path = "camino del saber/fondo2.gif"
gif = imageio.mimread(gif_path)

# Convertir las imágenes a superficies de Pygame
frames = [pygame.surfarray.make_surface(frame) for frame in gif]

# Si los fotogramas están en formato vertical, se pueden rotar a horizontal
# Lo que haremos es tomar la primera imagen, y reestructurarla de forma horizontal
frame_width = frames[0].get_width()
frame_height = frames[0].get_height()

# Crear una nueva lista con las imágenes rotadas
rotated_frames = []

# Aquí, si los fotogramas están organizados verticalmente (uno encima de otro),
# los reorganizamos en una secuencia horizontal. Esto es útil si tienes imágenes
# grandes en una sola columna.
for i in range(len(frames)):
    # En este caso no estamos rotando, solo reestructuramos
    rotated_frame = pygame.transform.rotate(frames[i], 270)  # Rotamos 90 grados para hacerlo horizontal
    rotated_frames.append(rotated_frame)

# Cargar las 5 imágenes adicionales
image_paths = [
    "camino del saber/ficha1.png",  # Cambia esto a tus imágenes
    "camino del saber/ficha2.png",
    "camino del saber/ficha3.png",
    "camino del saber/ficha4.png",
    "camino del saber/ficha5.png"

]

# Cargar las imágenes adicionales
images = [pygame.image.load(img_path) for img_path in image_paths]

# Animar los fotogramas
clock = pygame.time.Clock()
running = True
frame_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla (hacerla blanca o el color que desees)
    screen.fill((255, 255, 255))

    # Mostrar el fotograma del GIF
    gif_frame = pygame.transform.scale(rotated_frames[frame_index], (WIDTH, HEIGHT))
    screen.blit(gif_frame, (0, 0))

    # Mostrar las 5 imágenes encima del GIF
    positions = [
        (50, 50),  # Posición de la primera imagen
        (150, 100),  # Posición de la segunda imagen
        (250, 150),  # Posición de la tercera imagen
        (350, 200),  # Posición de la cuarta imagen
        (450, 250)   # Posición de la quinta imagen
    ]

    for img, pos in zip(images, positions):
        img_resized = pygame.transform.scale(img, (100, 100))  # Redimensionar a 100x100 px
        screen.blit(img_resized, pos)

    # Actualizar la pantalla
    pygame.display.update()

    # Avanzar al siguiente fotograma
    frame_index = (frame_index + 1) % len(rotated_frames)

    # Controlar la velocidad de la animación
    clock.tick(10)  # 10 FPS

pygame.quit()
