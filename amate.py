import os
import pygame

print("Directorio actual:", os.getcwd())  # Imprime el directorio de trabajo actual

# Intenta cargar la imagen
try:
    welcome_image = pygame.image.load('pantalla.png')  # Asegúrate de usar la ruta correcta
    print("Imagen cargada exitosamente.")
except pygame.error as e:
    print(f"No se pudo cargar la imagen: {e}")