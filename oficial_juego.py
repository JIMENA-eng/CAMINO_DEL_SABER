import pygame
import random
import time


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Esto hace que la ventana sea pantalla completa
WIDTH, HEIGHT = screen.get_size()  # Obtiene el tamaño de la pantalla completa

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

fuente = pygame.font.Font(None, 36)
grande_fuente = pygame.font.Font(None, 24)

LEVEL_1_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (350, 150), (250, 150), (150, 150), (50, 150)
]

LEVEL_2_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250)
]

LEVEL_3_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350)
]

LEVEL_4_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (350, 450), (250, 450), (150, 450), (50, 450)
]

LEVEL_5_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (550, 450), (650, 450), (650, 550), (550, 550),
    (450, 550), (350, 550), (250, 550), (150, 550), (50, 550)
]

LEVEL_6_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (550, 450), (650, 450), (650, 550), (550, 550),
    (450, 550), (350, 550), (250, 550), (150, 550), (50, 550),
    (50, 650), (150, 650), (250, 650), (350, 650)
]

LEVEL_7_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (550, 450), (650, 450), (650, 550), (550, 550),
    (450, 550), (350, 550), (250, 550), (150, 550), (50, 550),
    (50, 650), (150, 650), (250, 650), (350, 650), (450, 650),
    (450, 750), (350, 750), (250, 750), (150, 750), (50, 750)
]

LEVEL_8_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (550, 450), (650, 450), (650, 550), (550, 550),
    (450, 550), (350, 550), (250, 550), (150, 550), (50, 550),
    (50, 650), (150, 650), (250, 650), (350, 650), (450, 650),
    (450, 750), (550, 750), (650, 750), (650, 850), (550, 850),
    (450, 850), (350, 850), (250, 850), (150, 850), (50, 850)
]

LEVEL_9_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (550, 450), (650, 450), (650, 550), (550, 550),
    (450, 550), (350, 550), (250, 550), (150, 550), (50, 550),
    (50, 650), (150, 650), (250, 650), (350, 650), (450, 650),
    (450, 750), (550, 750), (650, 750), (650, 850), (550, 850),
    (450, 850), (350, 850), (250, 850), (150, 850), (50, 850),
    (50, 950), (150, 950), (250, 950), (350, 950), (450, 950)
]

LEVEL_10_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
    (450, 150), (550, 150), (650, 150), (650, 250), (550, 250),
    (450, 250), (350, 250), (250, 250), (150, 250), (50, 250),
    (50, 350), (150, 350), (250, 350), (350, 350), (450, 350),
    (450, 450), (550, 450), (650, 450), (650, 550), (550, 550),
    (450, 550), (350, 550), (250, 550), (150, 550), (50, 550),
    (50, 650), (150, 650), (250, 650), (350, 650), (450, 650),
    (450, 750), (550, 750), (650, 750), (650, 850), (550, 850),
    (450, 850), (350, 850), (250, 850), (150, 850), (50, 850),
    (50, 950), (150, 950), (250, 950), (350, 950), (450, 950),
    (450, 1050), (550, 1050), (650, 1050), (650, 1150), (550, 1150),
    (450, 1150), (350, 1150), (250, 1150), (150, 1150), (50, 1150)
]

# Lista que se actualizará según el nivel actual
BOARD_POSITIONS = []  # Inicialmente vacío, se actualizará dependiendo del nivel

QUESTIONS = [
    {"question": "¿Cuál es el planeta más cercano al sol?", "options": ["Mercurio", "Venus", "Tierra", "Marte"], "answer": "Mercurio"},
    {"question": "¿Cuántos continentes hay en la Tierra?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "¿Qué gas es esencial para la respiración?", "options": ["Oxígeno", "Hidrógeno", "Nitrógeno", "Helio"], "answer": "Oxígeno"},
    {"question": "¿En qué continente se encuentra Egipto?", "options": ["África", "Asia", "Europa", "América"], "answer": "África"},
    {"question": "¿Qué animal es conocido como el rey de la selva?", "options": ["León", "Tigre", "Elefante", "Cebra"], "answer": "León"},
    {"question": "¿Qué instrumento musical tiene cuerdas?", "options": ["Guitarra", "Piano", "Trompeta", "Flauta"], "answer": "Guitarra"},
    {"question": "¿Cuál es el río más largo del mundo?", "options": ["Nilo", "Amazonas", "Yangtsé", "Danubio"], "answer": "Amazonas"},
    {"question": "¿Cuál es el idioma más hablado en el mundo?", "options": ["Inglés", "Chino", "Español", "Árabe"], "answer": "Chino"},
    {"question": "¿Qué país tiene la población más grande?", "options": ["India", "China", "EE.UU.", "Indonesia"], "answer": "China"},
    {"question": "¿Qué es la capital de Francia?", "options": ["París", "Londres", "Berlín", "Madrid"], "answer": "París"}
]

current_level = 1
# Función para actualizar las posiciones del tablero
def update_board_positions(level):
    global BOARD_POSITIONS  # Usamos la variable global BOARD_POSITIONS
    
    # Dependiendo del nivel, se asignan las posiciones
    if level == 1:
        BOARD_POSITIONS = LEVEL_1_POSITIONS
    elif level == 2:
        BOARD_POSITIONS = LEVEL_2_POSITIONS
    elif level == 3:
        BOARD_POSITIONS = LEVEL_3_POSITIONS
    elif level == 4:
        BOARD_POSITIONS = LEVEL_4_POSITIONS
    elif level == 5:
        BOARD_POSITIONS = LEVEL_5_POSITIONS
    elif level == 6:
        BOARD_POSITIONS = LEVEL_6_POSITIONS
    elif level == 7:
        BOARD_POSITIONS = LEVEL_7_POSITIONS
    elif level == 8:
        BOARD_POSITIONS = LEVEL_8_POSITIONS
    elif level == 9:
        BOARD_POSITIONS = LEVEL_9_POSITIONS
    elif level == 10:
        BOARD_POSITIONS = LEVEL_10_POSITIONS
    
    # Asegúrate de que BOARD_POSITIONS no esté vacío
    if not BOARD_POSITIONS:
        raise ValueError(f"Las posiciones del tablero no están definidas para el nivel {level}.")

def reproducir_musica(nivel):
    # Detener cualquier música previa
    pygame.mixer.music.stop()

    # Determinar qué música reproducir según el nivel
    if nivel == 1:
        pygame.mixer.music.load('camino del saber/music1.mp3')
    elif nivel == 2:
        pygame.mixer.music.load('camino del saber/music2.mp3')
    elif nivel == 3:
        pygame.mixer.music.load('camino del saber/music3.mp3')
    elif nivel == 4:
        pygame.mixer.music.load('camino del saber/music4.mp3')
    elif nivel == 5:
        pygame.mixer.music.load('caminos del saber/music5.mp3')
    elif nivel == 6:
        pygame.mixer.music.load('caminos del saber/music6.mp3')
    elif nivel == 7:
        pygame.mixer.music.load('camino del saber/music7.mp3')
    elif nivel == 8:
        pygame.mixer.music.load('camino del saber/music8.mp3')
    elif nivel == 9:
        pygame.mixer.music.load('camino del saber/music9.mp3')
    elif nivel == 10:
        pygame.mixer.music.load('camino del saber/music10.mp3')

    # Reproducir la música en un bucle (puedes cambiar el -1 a 0 si no quieres que se repita)
    pygame.mixer.music.play(-1)
class Player:
    def __init__(self, name, color, piece_image_path, level=1):
        self.name = name
        self.color = color
        self.position = 0  # El jugador comienza en la primera casilla

        # Actualizar las posiciones del tablero según el nivel
        update_board_positions(level)
        
        # Colocar la pieza en la primera casilla
        self.x, self.y = BOARD_POSITIONS[0]  # Tomamos la primera posición del tablero actualizado

        self.correct_answers = 0

        # Cargar la imagen de la pieza
        self.piece_image = pygame.image.load(piece_image_path)
        self.piece_image = pygame.transform.scale(self.piece_image, (100, 100))
    
    def move(self, steps):
        # Moverse a través de las posiciones en BOARD_POSITIONS
        for _ in range(steps):
            if self.position < len(BOARD_POSITIONS) - 1:
                self.position += 1
                target_x, target_y = BOARD_POSITIONS[self.position]

                # Movimiento suave del jugador
                while (self.x, self.y) != (target_x, target_y):
                    if self.x < target_x:
                        self.x += 5
                    elif self.x > target_x:
                        self.x -= 5
                    if self.y < target_y:
                        self.y += 5
                    elif self.y > target_y:
                        self.y -= 5

                    # Redibuja el tablero y actualiza la pantalla después de cada paso
                    draw_board()
                    pygame.display.update()
                    pygame.time.delay(50)

    def auto_answer(self, question):
        selected_option = random.choice(question["options"])
        return selected_option
    
bot_piece_image = pygame.image.load('camino del saber/ficha6.png')
bot_piece_image = pygame.transform.scale(bot_piece_image, (100, 100))

bot_player = Player("Bot", BLUE, 'camino del saber/ficha6.png')
players = [bot_player]
current_player = 0

dice_roll = 1

def roll_dice():
    global dice_roll
    dice_roll =random.randint(1,6)
    return dice_roll

def dibujar_dado(screen, numero, x, y, tamano_dado):
    # Dibuja un cuadrado blanco para el dado
    pygame.draw.rect(screen, WHITE, (x, y, tamano_dado, tamano_dado))
    pygame.draw.rect(screen, BLACK, (x, y, tamano_dado, tamano_dado), 5)  # Borde negro
    
    puntos = []
    
    # Dependiendo del número, dibuja los puntos
    if numero == 1:
        puntos = [(x + tamano_dado // 2, y + tamano_dado // 2)]  # Un punto en el centro
    elif numero == 2:
        puntos = [(x + tamano_dado // 4, y + tamano_dado // 4), (x + 3 * tamano_dado // 4, y + 3 * tamano_dado // 4)]  # Dos puntos en diagonal
    elif numero == 3:
        puntos = [(x + tamano_dado // 2, y + tamano_dado // 2),  # Punto central
                  (x + tamano_dado // 4, y + tamano_dado // 4), (x + 3 * tamano_dado // 4, y + 3 * tamano_dado // 4)]  # Diagonal
    elif numero == 4:
        puntos = [(x + tamano_dado // 4, y + tamano_dado // 4), (x + 3 * tamano_dado // 4, y + tamano_dado // 4),  # Esquinas superiores
                  (x + tamano_dado // 4, y + 3 * tamano_dado // 4), (x + 3 * tamano_dado // 4, y + 3 * tamano_dado // 4)]  # Esquinas inferiores
    elif numero == 5:
        puntos = [(x + tamano_dado // 2, y + tamano_dado // 2),  # Punto central
                  (x + tamano_dado // 4, y + tamano_dado // 4), (x + 3 * tamano_dado // 4, y + tamano_dado // 4),  # Esquinas superiores
                  (x + tamano_dado // 4, y + 3 * tamano_dado // 4), (x + 3 * tamano_dado // 4, y + 3 * tamano_dado // 4)]  # Esquinas inferiores
    elif numero == 6:
        puntos = [(x + tamano_dado // 4, y + tamano_dado // 4), (x + 3 * tamano_dado // 4, y + tamano_dado // 4),  # Columna superior
                  (x + tamano_dado // 4, y + tamano_dado // 2), (x + 3 * tamano_dado // 4, y + tamano_dado // 2),  # Columna del medio
                  (x + tamano_dado // 4, y + 3 * tamano_dado // 4), (x + 3 * tamano_dado // 4, y + 3 * tamano_dado // 4)]  # Columna inferior
    
    for punto in puntos:
        pygame.draw.circle(screen, BLACK, punto, tamano_dado // 10)

def ask_random_question():
    return random.choice(QUESTIONS)

def draw_board():
    screen.fill(WHITE)

    # Fondo del tablero
    wel_bt = pygame.image.load('camino del saber/fondo3.png')
    wel_bt = pygame.transform.scale(wel_bt, (WIDTH, HEIGHT))
    screen.blit(wel_bt, (0, 0))

    # Asegurarse de que BOARD_POSITIONS esté actualizado antes de dibujar el tablero
    # Aquí, asumiendo que tienes un "nivel actual" que seleccionaste previamente, 
    # se actualiza el tablero en función de ese nivel.
    update_board_positions(current_level) # Asegúrate de que `current_level` es el nivel actual seleccionado

    # Dibujar las posiciones del tablero
    for pos in BOARD_POSITIONS:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], 80, 80), 2)

    # Dibujar las piezas de los jugadores
    for player in players:
        screen.blit(player.piece_image, (player.x, player.y))

    # Dibujar el puntaje de los jugadores
    for player in players:
        text_surface = grande_fuente.render(f"{player.name}: {player.correct_answers}", True, BLACK)
        screen.blit(text_surface, (20, 20 + players.index(player) * 30))

    # Área para el dado
    dice_area_size = 150
    dice_area_rect = pygame.Rect(WIDTH - dice_area_size - 20, HEIGHT - dice_area_size - 20, dice_area_size, dice_area_size)
    
    # Dibujar el borde del área del dado
    pygame.draw.rect(screen, BLACK, dice_area_rect, 2)
    pygame.draw.rect(screen, WHITE, dice_area_rect.inflate(-4, -4))  # Fondo blanco dentro del área

    # Dibujar el dado visualmente (lo que ya tienes implementado)
    dibujar_dado(screen, dice_roll, dice_area_rect.x + 10, dice_area_rect.y + 10, dice_area_size - 20)

    
def display_text(text, color=BLACK, y_offset=0):
    text_surface = fuente.render(text, True, color)
    screen.blit(text_surface, (20, HEIGHT - 120 + y_offset))

def show_welcome_screen():
    screen.fill(WHITE)
    welcome_image = pygame.image.load('camino del saber/pantalla.png')
    welcome_image = pygame.transform.scale(welcome_image, (WIDTH, HEIGHT))
    screen.blit(welcome_image, (0, 0))
    pygame.display.update()
    pygame.time.wait(2000)

def segundo_screen():
    screen.fill(BLACK)
    
    # Ruta de las imágenes
    image_paths = [
        "camino del saber/encabezado.png",  
        "camino del saber/dialogo.png",
        "camino del saber/personaje1.png",
        "camino del saber/dado.png",
        "camino del saber/fichas.png"
    ]
    
    # Tamaños específicos para cada imagen
    sizes = [
        (500, 100),  # Tamaño para la primera imagen
        (400, 200),  # Tamaño para la segunda imagen
        (400, 400),  # Tamaño para la tercera imagen
        (300, 400),  # Tamaño para la cuarta imagen
        (500, 300)   # Tamaño para la quinta imagen
    ]
    
    # Cargar y redimensionar cada imagen
    images = []
    for img_path, size in zip(image_paths, sizes):
        img = pygame.image.load(img_path)
        img_resized = pygame.transform.scale(img, size)  # Redimensionar cada imagen
        images.append(img_resized)

    # Posiciones de las imágenes
    positions = [
        (450, 50),  # Posición de la primera imagen
        (580, 250),  # Posición de la segunda imagen
        (1000, 380),  # Posición de la tercera imagen
        (50, 100),  # Posición de la cuarta imagen
        (400, 450)   # Posición de la quinta imagen
    ]

    fade_duration = 1500  # Duración del fade en milisegundos para cada imagen
    fade_steps = 30  # Número de pasos por fade (más alto = más suave)

    # Para cada imagen, aplicaremos la transición de fade-in
    for img, pos in zip(images, positions):
        # Fade-in: Aumentamos la opacidad de 0 a 255 utilizando un rectángulo negro
        for step in range(fade_steps + 1):
            # Calcular la opacidad (de 0 a 255)
            opacity = int((step / fade_steps) * 255)
            
            # Crear una superficie del tamaño de la imagen redimensionada para el efecto de fade
            fade_surface = pygame.Surface(img.get_size())  # Usamos el tamaño real de la imagen
            fade_surface.fill((0, 0, 0))  # Llenar con color negro
            fade_surface.set_alpha(255 - opacity)  # Reducir la opacidad del rectángulo negro
            
            # Limpiar la pantalla antes de redibujar
            screen.fill(BLACK)

            # Dibujar las imágenes previas para que no desaparezcan
            for prev_img, prev_pos in zip(images[:images.index(img)], positions[:images.index(img)]):
                screen.blit(prev_img, prev_pos)

            # Dibujar la imagen actual con el fade (rectángulo negro sobre ella)
            screen.blit(img, pos)
            screen.blit(fade_surface, pos)  # Añadir el rectángulo semi-transparente

            # Actualizar la pantalla
            pygame.display.update()

            # Esperar un poco antes de continuar al siguiente paso
            pygame.time.delay(fade_duration // fade_steps)

    # Esperar 2 segundos al final de la animación
    pygame.time.delay(2000)

def tercer_web():
    screen.fill(BLACK)
    image_paths = [
        "camino del saber/tres.png",  
        "camino del saber/dos.png",
        "camino del saber/uno.png",
        "camino del saber/cero.png",
        "camino del saber/listo.png",
        "camino del saber/comenzar.png"
    ]
    
    # Tamaños específicos para cada imagen (puedes ajustar estos tamaños)
    sizes = [
        (300, 600),  # Tamaño para la primera imagen
        (300, 600),  # Tamaño para la segunda imagen
        (300, 600),  # Tamaño para la tercera imagen
        (300, 600),  # Tamaño para la cuarta imagen
        (1000, 500),   # Tamaño para la quinta imagen
        (1000, 500)
    ]
    
    # Posiciones de las imágenes
    positions = [
        (500 , 5),  # Posición de la primera imagen
        (500, 5),  # Posición de la segunda imagen
        (500, 5),  # Posición de la tercera imagen
        (500, 5),  # Posición de la cuarta imagen
        (150, 100),  # Posición de la quinta imagen
        (200, 100)
    ]
    
    # Cargar las imágenes y redimensionarlas
    images = [pygame.image.load(img_path) for img_path in image_paths]
    resized_images = [pygame.transform.scale(img, size) for img, size in zip(images, sizes)]

    # Control del tiempo con pygame.time.get_ticks()
    start_ticks = pygame.time.get_ticks()  # Obtiene el tiempo inicial en milisegundos
    duration_show = 4000  # Duración de cada imagen en milisegundos (2 segundos)
    current_image = 0  # Índice de la imagen que se está mostrando
    show_image_time = start_ticks  # Tiempo en que se debe mostrar la primera imagen

    while current_image < len(resized_images):
        screen.fill(BLACK)  # Limpiar la pantalla para cada ciclo
        
        # Mostrar la imagen actual
        if pygame.time.get_ticks() - show_image_time < duration_show:
            # Mostrar la imagen en la posición correspondiente
            screen.blit(resized_images[current_image], positions[current_image])
        else:
            # Cambiar a la siguiente imagen
            current_image += 1
            if current_image < len(resized_images):
                show_image_time = pygame.time.get_ticks()  # Reiniciar el tiempo para la nueva imagen
        
        pygame.display.update()  # Actualizar la pantalla
        pygame.time.Clock().tick(60)  # Limitar la velocidad de fotogramas a 60 FPS
        
def seleccionar_nivel():
    screen.fill(WHITE)
    wel_nivel = pygame.image.load('camino del saber/fondo4.png')
    wel_nivel = pygame.transform.scale(wel_nivel, (WIDTH, HEIGHT))
    screen.blit(wel_nivel, (0, 0))
    font = pygame.font.Font(None, 48)
    
    # Instrucciones para el usuario
    instruction_text = font.render("Selecciona un nivel (1-10)", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - 200))
    
    # Cargar las imágenes de los niveles (10 imágenes)
    level_images = [pygame.image.load(f'camino del saber/nivel{i}.png') for i in range(1, 11)]  
    image_size = (100, 100)
    level_images = [pygame.transform.scale(img, image_size) for img in level_images]
    
    # Crear una lista para los rectángulos de los niveles
    level_rects = []
    button_width, button_height = image_size
    
    # Distribuir las imágenes de los niveles
    for i in range(10):
        col = i % 5  # 5 columnas
        row = i // 5  # 2 filas
        level_rect = pygame.Rect(WIDTH // 2 - (2.5 * button_width) + col * (button_width + 20),
                                 HEIGHT // 2 - 100 + row * (button_height + 20),
                                 button_width, button_height)
        level_rects.append(level_rect)
        
        # Dibujar la imagen del nivel
        screen.blit(level_images[i], level_rect.topleft)
    
    pygame.display.update()

    selected_level = None
    while selected_level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detectar en qué imagen se hizo clic
                for rect, i in zip(level_rects, range(10)):
                    if rect.collidepoint(event.pos):
                        selected_level = i + 1  # El nivel seleccionado será el índice + 1
                        break

    # Asignar el nivel seleccionado a la variable global `current_level`
    global current_level
    current_level = selected_level

    # Llamar a la función para actualizar las posiciones del tablero
    update_board_positions(current_level)
    reproducir_musica(current_level)

    return selected_level


def seleccionar_ficha():
    screen.fill(WHITE)
    
    # Cargar y escalar el fondo
    wel_fi = pygame.image.load('camino del saber/fondo5.png')
    wel_fi = pygame.transform.scale(wel_fi, (WIDTH, HEIGHT))
    screen.blit(wel_fi, (0, 0))
    
    # Cargar las 14 imágenes de las fichas
    piece_images = [pygame.image.load(f'camino del saber/ficha{i}.png') for i in range(1, 15)]  # 14 fichas
    piece_size = 100  # Tamaño de cada ficha
    piece_images = [pygame.transform.scale(image, (piece_size, piece_size)) for image in piece_images]

    # Crear los rectángulos para cada ficha (para la detección de clics)
    piece_rects = []
    for i, image in enumerate(piece_images):
        # Distribuir las fichas en una cuadrícula de 4 filas y 4 columnas
        x = WIDTH // 2 - (2 * piece_size) + (i % 4) * (piece_size + 20)  # 4 columnas
        y = HEIGHT // 2 - (2 * piece_size) + (i // 4) * (piece_size + 20)  # 4 filas
        rect = pygame.Rect(x, y, piece_size, piece_size)
        piece_rects.append(rect)
        screen.blit(image, rect.topleft)

    # Mostrar texto de instrucciones
    instruction_text = fuente.render("Selecciona tu ficha", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - piece_size - 30))

    pygame.display.update()

    selected_piece = None
    while selected_piece is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(piece_rects):
                    if rect.collidepoint(event.pos):  # Si se hace clic sobre la ficha
                        selected_piece = piece_images[i]  # Seleccionar la ficha
                        break

    return selected_piece

def show_start_screen():
    screen.fill(WHITE)
    wel_bt = pygame.image.load('camino del saber/fondo2.png')
    wel_bt = pygame.transform.scale(wel_bt, (WIDTH, HEIGHT))
    screen.blit(wel_bt, (0, 0))

    solitary_image = pygame.image.load('camino del saber/solitario.png')
    invite_image = pygame.image.load('camino del saber/invitar.png')
    
    button_width, button_height = 300, 100
    solitary_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 - 60, button_width, button_height)
    invite_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 + 60, button_width, button_height)
    
    solitary_image = pygame.transform.scale(solitary_image, (button_width, button_height))
    invite_image = pygame.transform.scale(invite_image, (button_width, button_height))
    
    screen.blit(solitary_image, solitary_rect.topleft)
    screen.blit(invite_image, invite_rect.topleft)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solitary_rect.collidepoint(event.pos):
                    return "solitario"
                if invite_rect.collidepoint(event.pos):
                    return "invitar"

def ventana_ingresar_name():
    screen.fill(WHITE)

    # Cargar el fondo
    wel_name = pygame.image.load('camino del saber/fondo3.png')
    wel_name = pygame.transform.scale(wel_name, (WIDTH, HEIGHT))
    screen.blit(wel_name, (0, 0))

    font = pygame.font.Font(None, 48)
    title_text = font.render("Ingresa tu nombre:", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 200))

    input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 50)
    color = pygame.Color('lightskyblue3')
    
    user_name = ""
    pygame.draw.rect(screen, color, input_box, 2)
    input_text = font.render(user_name, True, BLACK)
    screen.blit(input_text, (input_box.x + 5, input_box.y + 5))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_name  # Retorna el nombre cuando presionan Enter
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    user_name += event.unicode
        
            # Redibujar para cada evento
            screen.fill(WHITE)
            screen.blit(wel_name, (0, 0))
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 200))
            pygame.draw.rect(screen, color, input_box, 2)
            input_text = font.render(user_name, True, BLACK)
            screen.blit(input_text, (input_box.x + 5, input_box.y + 5))
            pygame.display.update()

def eligir_ficha():
    screen.fill(WHITE)

    # Cargar el fondo
    wel_piece = pygame.image.load('camino del saber/fondo4.png')
    wel_piece = pygame.transform.scale(wel_piece, (WIDTH, HEIGHT))
    screen.blit(wel_piece, (0, 0))

    font = pygame.font.Font(None, 48)
    title_text = font.render("Selecciona una ficha:", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 200))

    # Cargar las imágenes de las fichas
    piece_images = [pygame.image.load(f'camino del saber/ficha{i}.png') for i in range(1, 15)]
    piece_size = 100
    piece_images = [pygame.transform.scale(img, (piece_size, piece_size)) for img in piece_images]

    # Crear los rectángulos para las fichas
    piece_rects = []
    for i, image in enumerate(piece_images):
        x = WIDTH // 2 - (2 * piece_size) + (i % 4) * (piece_size + 20)
        y = HEIGHT // 2 + 50 + (i // 4) * (piece_size + 20)
        rect = pygame.Rect(x, y, piece_size, piece_size)
        piece_rects.append(rect)
    
    # Mostrar las fichas
    for i, rect in enumerate(piece_rects):
        screen.blit(piece_images[i], rect.topleft)

    pygame.display.update()

    selected_piece = None
    while selected_piece is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(piece_rects):
                    if rect.collidepoint(event.pos):
                        selected_piece = f'camino del saber/ficha{i + 1}.png'  # Seleccionar la ficha al hacer clic

        pygame.display.update()

    return selected_piece  # Devuelve la ficha seleccionada


def main():
    show_welcome_screen()
    segundo_screen()
    tercer_web()
    show_start_screen()
    level_selected = seleccionar_nivel()
    update_board_positions(level_selected)
    
    global dice_roll, current_player
    # Solicitar el nombre del jugador y la ficha
    user_name = ventana_ingresar_name()
    user_piece_image = eligir_ficha()

    # Crear el jugador
    user_player = Player(user_name, RED, user_piece_image)
    players.append(user_player)

    # Configuración de variables globales
    current_player = 0
    clock = pygame.time.Clock()
    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Cuando se presiona espacio, lanzamos el dado
                    roll_dice()  # Lanza el dado
                    players[current_player].move(dice_roll)  # Mueve al jugador con el valor del dado
                    draw_board()  # Dibuja el tablero
                    
                    pygame.display.update()

                    # Realizar pregunta aleatoria
                    question = ask_random_question()
                    selected_option = players[current_player].auto_answer(question)
                    if selected_option == question["answer"]:
                        players[current_player].correct_answers += 1

                    # Cambiar al siguiente jugador
                    current_player = (current_player + 1) % len(players)
                    time.sleep(1)

        if current_player == 0:  # El bot mueve automáticamente
            roll_dice()
            players[current_player].move(dice_roll)  # Mueve al bot con el valor del dado
            question = ask_random_question()  # Bot responde la pregunta
            selected_option = players[current_player].auto_answer(question)
            if selected_option == question["answer"]:
                players[current_player].correct_answers += 1

            # Cambiar al siguiente jugador (bot en este caso)
            current_player = (current_player + 1) % len(players)

        # Dibuja el dado y el tablero
        draw_board()
   
        pygame.display.update()  # Actualiza la pantalla

        # Control de FPS (velocidad del juego)
        clock.tick(60)
if __name__ == "__main__":
    main()
