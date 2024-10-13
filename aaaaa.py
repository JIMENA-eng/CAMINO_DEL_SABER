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
BOX_SIZE = WIDTH // 8  # Ajustado para 8 columnas en lugar de 16

# Definir posiciones de las casillas en 5x4
BOARD_POSITIONS = []
x, y = 50, 50
for row in range(4):  # 4 filas
    for col in range(5):  # 5 columnas
        BOARD_POSITIONS.append((x, y))
        x += BOX_SIZE
    x = 50
    y += BOX_SIZE

# Definir preguntas por nivel
QUESTIONS = {
    1: [  # Nivel 1
        {"question": "¿Cuál es el planeta más cercano al sol?", "options": ["Mercurio", "Venus", "Tierra", "Marte"], "answer": "Mercurio"},
        {"question": "¿Cuántos continentes hay en la Tierra?", "options": ["5", "6", "7", "8"], "answer": "7"}
    ],
    2: [  # Nivel 2
        {"question": "¿Qué gas es esencial para la respiración?", "options": ["Oxígeno", "Hidrógeno", "Nitrógeno", "Helio"], "answer": "Oxígeno"},
        {"question": "¿En qué continente se encuentra Egipto?", "options": ["África", "Asia", "Europa", "América"], "answer": "África"}
    ],
    # Agrega más niveles aquí
}

# Fuente para texto
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Definir clase Jugador
class Player:
    def __init__(self, name, color, piece_image):
        self.name = name
        self.color = color
        self.position = 0
        self.x, self.y = BOARD_POSITIONS[0]
        self.correct_answers = 0
        self.piece_image = piece_image

    def move(self, steps):
        for _ in range(steps):
            if self.position < len(BOARD_POSITIONS) - 1:
                self.position += 1
                target_x, target_y = BOARD_POSITIONS[self.position]

                # Ajuste para mover en forma de "gusanito"
                if self.position % 5 == 0 and self.position != 0:  # Cambia de fila
                    if (self.position // 5) % 2 == 1:  # Si es fila impar
                        target_x = BOARD_POSITIONS[self.position][0]
                    else:  # Si es fila par
                        target_x = BOARD_POSITIONS[self.position - 1][0] + BOX_SIZE
                
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
        selected_option = random.choice(question["options"])
        return selected_option

# Crear jugadores
bot_piece_image = pygame.image.load('camino del saber/ficha6.png')
bot_piece_image = pygame.transform.scale(bot_piece_image, (100, 100))

bot_player = Player("Bot", BLUE, bot_piece_image)
players = [bot_player]
current_player = 0

# Crear un dado virtual
dice_roll = 1

def roll_dice():
    global dice_roll
    dice_roll = random.randint(1, 6)
    return dice_roll

# Pregunta aleatoria según nivel
def ask_random_question(level):
    return random.choice(QUESTIONS[level])


# Dibujar el tablero y los jugadores
def draw_board():
    screen.fill(WHITE)
    for pos in BOARD_POSITIONS:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], BOX_SIZE, BOX_SIZE), 2)

    for player in players:
        screen.blit(player.piece_image, (player.x, player.y))

    for player in players:
        text_surface = small_font.render(f"{player.name}: {player.correct_answers}", True, BLACK)
        screen.blit(text_surface, (20, 20 + players.index(player) * 30))

    dice_area_size = 150
    dice_area_rect = pygame.Rect(WIDTH - dice_area_size - 20, HEIGHT - dice_area_size - 20, dice_area_size, dice_area_size)
    pygame.draw.rect(screen, BLACK, dice_area_rect, 2)
    pygame.draw.rect(screen, WHITE, dice_area_rect.inflate(-4, -4))
    dice_value_surface = font.render(str(dice_roll), True, BLACK)
    screen.blit(dice_value_surface, (dice_area_rect.x + dice_area_size // 2 - dice_value_surface.get_width() // 2, 
                                     dice_area_rect.y + dice_area_size // 2 - dice_value_surface.get_height() // 2))

def display_text(text, color=BLACK, y_offset=0):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (20, HEIGHT - 120 + y_offset))

# Pantalla de bienvenida
def show_welcome_screen():
    screen.fill(WHITE)
    welcome_image = pygame.image.load('camino del saber/pantalla.png')
    welcome_image = pygame.transform.scale(welcome_image, (WIDTH, HEIGHT))
    screen.blit(welcome_image, (0, 0))
    pygame.display.update()
    pygame.time.wait(2000)

# Pantalla de selección de niveles
# Pantalla de selección de niveles
def show_level_selection_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)
    instruction_text = font.render("Selecciona un nivel (1-20)", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - 200))
    


    level_buttons = []
    button_width = 80
    button_height = 50
    for i in range(20):
        col = i % 5  # 5 columnas
        row = i // 5  # 4 filas
        level_rect = pygame.Rect(WIDTH // 2 - (2.5 * button_width) + col * (button_width + 20),
                                  HEIGHT // 2 - 100 + row * (button_height + 10),
                                  button_width, button_height)
        level_buttons.append((level_rect, str(i + 1)))

    for rect, label in level_buttons:
        pygame.draw.rect(screen, BLACK, rect, 2)
        level_surface = font.render(label, True, BLACK)
        screen.blit(level_surface, (rect.x + button_width // 2 - level_surface.get_width() // 2,
                                     rect.y + button_height // 2 - level_surface.get_height() // 2))

    pygame.display.update()

    selected_level = None
    while selected_level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, label in level_buttons:
                    if rect.collidepoint(event.pos):
                        selected_level = int(label)
                        break

    return selected_level


# Pantalla de inicio
def show_start_screen():
    screen.fill(WHITE)
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
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solitary_rect.collidepoint(event.pos):
                    return "solitario"
                if invite_rect.collidepoint(event.pos):
                    return "invitar"

# Pantalla de selección de ficha
def show_piece_selection_screen():
    screen.fill(WHITE)
    piece_images = [pygame.image.load(f'camino del saber/ficha{i}.png') for i in range(1, 5)]
    piece_size = 100
    piece_images = [pygame.transform.scale(image, (piece_size, piece_size)) for image in piece_images]

    piece_rects = []
    for i, image in enumerate(piece_images):
        x = WIDTH // 2 - (piece_size * 2) + (i % 2) * (piece_size + 20)
        y = HEIGHT // 2 - (piece_size // 2) + (i // 2) * (piece_size + 20)
        rect = pygame.Rect(x, y, piece_size, piece_size)
        piece_rects.append(rect)
        screen.blit(image, rect.topleft)

    instruction_text = font.render("Selecciona tu ficha", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - piece_size - 30))

    pygame.display.update()

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
    active = False
    font = pygame.font.Font(None, 32)
    text = ''

    instruction_text = font.render("Ingresa tu nombre y selecciona tu ficha", True, BLACK)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:
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
        screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 - 100))
        pygame.display.update()

# Función principal del juego
def main():
    show_welcome_screen()
    game_mode = show_start_screen()
    selected_level = show_level_selection_screen()
    print(f"Nivel seleccionado: {selected_level}")

    user_name, user_piece_image = show_name_and_piece_screen()

    user_player = Player(user_name, RED, user_piece_image)
    players.append(user_player)

    global current_player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll_dice()
                    players[current_player].move(dice_roll)
                    draw_board()

                    # Pregunta aleatoria después de mover
                    question = ask_random_question(selected_level)
                    selected_option = players[current_player].auto_answer(question)
                    if selected_option == question["answer"]:
                        players[current_player].correct_answers += 1
                    
                    # Cambiar turno
                    current_player = (current_player + 1) % len(players)
                    time.sleep(1)

        # Mover al bot automáticamente
        if current_player == 0:  # Asumiendo que el bot es el primer jugador
            roll_dice()
            players[current_player].move(dice_roll)
            question = ask_random_question(selected_level)
            selected_option = players[current_player].auto_answer(question)
            if selected_option == question["answer"]:
                players[current_player].correct_answers += 1
            
            # Cambiar turno
            current_player = (current_player + 1) % len(players)

        draw_board()
        pygame.display.update()

if __name__ == "__main__":
    main()

