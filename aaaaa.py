import pygame
import sys
import random
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Camino Curvado")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definir el tamaño de las casillas
BOX_SIZE = WIDTH // 16  # Ajusta el tamaño de las casillas a 1/16 del ancho de la pantalla

# Definir posiciones de las casillas en forma de "gusano"
BOARD_POSITIONS = []
x, y = 50, 50
for _ in range(8):  # Número de filas
    for _ in range(16):  # Número de columnas
        BOARD_POSITIONS.append((x, y))
        x += BOX_SIZE
    x = 50
    y += BOX_SIZE

# Definir preguntas aleatorias
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

# Fuente para texto
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)  # Fuente pequeña para el conteo

# Definir clase Jugador
class Player:
    def __init__(self, name, color, piece_image):
        self.name = name
        self.color = color
        self.position = 0
        self.x, self.y = BOARD_POSITIONS[0]
        self.correct_answers = 0  # Contador de respuestas correctas
        self.piece_image = piece_image  # Imagen de la ficha

    def move(self, steps):
        # Mover al jugador con animación
        for _ in range(steps):
            if self.position < len(BOARD_POSITIONS) - 1:
                self.position += 1
                target_x, target_y = BOARD_POSITIONS[self.position]
                while (self.x, self.y) != (target_x, target_y):
                    if self.x < target_x:
                        self.x += 5
                    elif self.x > target_x:
                        self.x -= 5
                    if self.y < target_y:
                        self.y += 5
                    elif self.y > target_y:
                        self.y -= 5
                    draw_board()
                    pygame.display.update()
                    pygame.time.delay(50)

    def auto_answer(self, question):
        # El bot responde automáticamente seleccionando una opción al azar
        selected_option = random.choice(question["options"])
        return selected_option

# Crear jugadores
bot_piece_image = pygame.image.load('camino del saber/ficha6.png')  # Imagen de la ficha del bot
bot_piece_image = pygame.transform.scale(bot_piece_image, (100, 100))

bot_player = Player("Bot", BLUE, bot_piece_image)
players = [bot_player]
current_player = 0

# Crear un dado virtual
dice_roll = 1  # Inicializar con un valor predeterminado

def roll_dice():
    global dice_roll
    dice_roll = random.randint(1, 6)
    return dice_roll

# Pregunta aleatoria con opciones
def ask_random_question():
    return random.choice(QUESTIONS)

# Dibujar el tablero y los jugadores
def draw_board():
    screen.fill(WHITE)

    # Ajustar el tamaño de las casillas
    box_size = BOX_SIZE

    # Dibujar casillas
    for pos in BOARD_POSITIONS:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], box_size, box_size), 2)

    # Dibujar jugadores
    for player in players:
        screen.blit(player.piece_image, (player.x, player.y))  # Dibujar la ficha del jugador

    # Mostrar el contador de respuestas correctas en tamaño pequeño
    for player in players:
        text_surface = small_font.render(f"{player.name}: {player.correct_answers}", True, BLACK)
        screen.blit(text_surface, (20, 20 + players.index(player) * 30))

    # Dibujar el área del dado
    dice_area_size = 150
    dice_area_rect = pygame.Rect(WIDTH - dice_area_size - 20, HEIGHT - dice_area_size - 20, dice_area_size, dice_area_size)
    pygame.draw.rect(screen, BLACK, dice_area_rect, 2)
    pygame.draw.rect(screen, WHITE, dice_area_rect.inflate(-4, -4))  # Dado blanco
    dice_value_surface = font.render(str(dice_roll), True, BLACK)
    screen.blit(dice_value_surface, (dice_area_rect.x + dice_area_size // 2 - dice_value_surface.get_width() // 2, 
                                     dice_area_rect.y + dice_area_size // 2 - dice_value_surface.get_height() // 2))

# Mostrar texto en la pantalla
def display_text(text, color=BLACK, y_offset=0):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (20, HEIGHT - 120 + y_offset))

# Temporizador para preguntas
def countdown_timer(start_time, duration=10):
    elapsed = time.time() - start_time
    remaining_time = max(0, duration - int(elapsed))
    return remaining_time

# Mostrar la pantalla de preguntas
def show_question_screen(question, options, selected_option, remaining_time):
    screen.fill(WHITE)

    # Mostrar pregunta
    question_text = font.render(question, True, BLACK)
    screen.blit(question_text, (20, 20))

    # Mostrar opciones de respuesta
    for i, option in enumerate(options):
        color = GREEN if i == selected_option else BLACK
        option_text = font.render(f"{i + 1}. {option}", True, color)
        screen.blit(option_text, (20, 100 + i * 50))

    # Mostrar temporizador
    timer_text = font.render(f"Tiempo restante: {remaining_time}s", True, RED)
    screen.blit(timer_text, (20, HEIGHT - 50))

# Pantalla de bienvenida
def show_welcome_screen():
    screen.fill(WHITE)
    # Cargar la imagen
    welcome_image = pygame.image.load('camino del saber/pantalla.png')  # Asegúrate de usar la ruta correcta
    # Redimensionar la imagen si es necesario
    welcome_image = pygame.transform.scale(welcome_image, (WIDTH, HEIGHT))
    screen.blit(welcome_image, (0, 0))
    pygame.display.update()
    pygame.time.wait(2000)  # Esperar 2 segundos


# Pantalla de inicio (selección de modo de juego)
def show_start_screen():
    screen.fill(WHITE)
    # Cargar imágenes para botones
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

    # Esperar la selección
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solitary_rect.collidepoint(event.pos):
                    return "solitario"
                if invite_rect.collidepoint(event.pos):
                    return "invitar"

# Pantalla de selección de ficha
def show_piece_selection_screen():
    screen.fill(WHITE)

    # Cargar las imágenes de las fichas
    piece_images = [
        pygame.image.load('camino del saber/ficha1.png'),
        pygame.image.load('camino del saber/ficha2.png'),
        pygame.image.load('camino del saber/ficha3.png'),
        pygame.image.load('camino del saber/ficha4.png')
    ]

    # Redimensionar las imágenes de las fichas
    piece_size = 100
    for i in range(len(piece_images)):
        piece_images[i] = pygame.transform.scale(piece_images[i], (piece_size, piece_size))

    # Mostrar imágenes de las fichas
    piece_rects = []
    for i, image in enumerate(piece_images):
        x = WIDTH // 2 - (piece_size * 2) + (i % 2) * (piece_size + 20)
        y = HEIGHT // 2 - (piece_size // 2) + (i // 2) * (piece_size + 20)
        rect = pygame.Rect(x, y, piece_size, piece_size)
        piece_rects.append(rect)
        screen.blit(image, rect.topleft)

    # Mostrar instrucciones
    instruction_text = font.render("Selecciona tu ficha", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - piece_size - 30))

    pygame.display.update()

    # Esperar la selección
    selected_piece = None
    while selected_piece is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(piece_rects):
                    if rect.collidepoint(event.pos):
                        selected_piece = piece_images[i]
                        break

    return selected_piece

# Pantalla de ingreso del nombre y selección de ficha
def show_name_and_piece_screen():
    screen.fill(WHITE)
    name_input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 40)
    name_color = pygame.Color('lightskyblue3')
    input_box_color = pygame.Color('black')
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    font = pygame.font.Font(None, 32)
    text = ''
    active = False
    piece_image = None

    # Mostrar instrucciones
    instruction_text = font.render("Ingresa tu nombre y selecciona tu ficha", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - 100))

    # Mostrar el cuadro de texto para el nombre
    pygame.draw.rect(screen, input_box_color, name_input_box, 2)
    txt_surface = font.render(text, True, name_color)
    screen.blit(txt_surface, (name_input_box.x + 5, name_input_box.y + 5))
    pygame.draw.rect(screen, input_box_color, name_input_box, 2)

    pygame.display.update()

    # Manejar eventos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:  # Verificar que el nombre no esté vacío
                            piece_image = show_piece_selection_screen()
                            return text, piece_image
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if name_input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False

        # Mostrar el cuadro de texto actualizado
        screen.fill(WHITE)
        pygame.draw.rect(screen, input_box_color, name_input_box, 2)
        txt_surface = font.render(text, True, name_color)
        screen.blit(txt_surface, (name_input_box.x + 5, name_input_box.y + 5))
        pygame.draw.rect(screen, input_box_color, name_input_box, 2)
        pygame.display.update()

# Función principal del juego
def main():
    show_welcome_screen()
    game_mode = show_start_screen()

    if game_mode == "invitar":
        # Aquí puedes agregar la lógica para el modo de invitación
        pass

    user_name, user_piece_image = show_name_and_piece_screen()

    # Crear jugador del usuario con la ficha seleccionada
    user_player = Player(user_name, RED, user_piece_image)
    players.append(user_player)

    # Bucle principal del juego
    global current_player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll_dice()
                    current_player = (current_player + 1) % len(players)
                    current_player_obj = players[current_player]
                    current_player_obj.move(dice_roll)
                    draw_board()

        draw_board()
        pygame.display.update()

if __name__ == "__main__":
    main()