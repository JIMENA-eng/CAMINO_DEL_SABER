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
NUM_BOXES = 25
BOX_SIZE = min(WIDTH // 5, HEIGHT // 5)  # Ajusta el tamaño de las casillas a 1/5 del ancho o alto de la pantalla

# Definir posiciones de las casillas en forma de "gusano"
BOARD_POSITIONS = []
x, y = 50, 50
direction = 1  # 1 para derecha, -1 para izquierda
for i in range(NUM_BOXES):
    BOARD_POSITIONS.append((x, y))
    if direction == 1:
        x += BOX_SIZE
        if len(BOARD_POSITIONS) % 5 == 0:  # Cambio de fila
            y += BOX_SIZE
            direction = -1
    else:
        x -= BOX_SIZE
        if len(BOARD_POSITIONS) % 5 == 0:  # Cambio de fila
            y += BOX_SIZE
            direction = 1
    if len(BOARD_POSITIONS) % 5 == 0:
        x = 50 if direction == 1 else WIDTH - 50 - BOX_SIZE

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
    pygame.time.wait(3000)  # Esperar 3 segundos

# Pantalla de inicio
def show_start_screen():
    screen.fill(WHITE)
    # Cargar las imágenes
    solitary_image = pygame.image.load('camino del saber/solitario.png')  # Asegúrate de usar la ruta correcta
    invite_image = pygame.image.load('camino del saber/invitar.png')  # Asegúrate de usar la ruta correcta
    
    # Redimensionar las imágenes
    button_width, button_height = 300, 100
    solitary_image = pygame.transform.scale(solitary_image, (button_width, button_height))
    invite_image = pygame.transform.scale(invite_image, (button_width, button_height))
    
    screen.blit(solitary_image, (WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 - 50))
    screen.blit(invite_image, (WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50))
    
    pygame.display.update()

# Función principal del juego
def main():
    global current_player, dice_roll
    show_welcome_screen()
    show_start_screen()
    
    clock = pygame.time.Clock()
    running = True
    game_started = False
    waiting_for_question = False
    question = None
    selected_option = None
    question_start_time = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not game_started:
                        game_started = True
                    else:
                        if waiting_for_question:
                            if selected_option is not None:
                                correct_answer = question["answer"]
                                if question["options"][selected_option] == correct_answer:
                                    players[current_player].correct_answers += 1
                                waiting_for_question = False
                                current_player = (current_player + 1) % len(players)
                                roll_dice()
                        else:
                            if dice_roll > 0:
                                players[current_player].move(dice_roll)
                                dice_roll = 0
                                waiting_for_question = True
                                question = ask_random_question()
                                selected_option = None
                                question_start_time = time.time()

        if waiting_for_question and question_start_time:
            remaining_time = countdown_timer(question_start_time)
            if remaining_time == 0:
                waiting_for_question = False
                current_player = (current_player + 1) % len(players)
                roll_dice()
            else:
                show_question_screen(question["question"], question["options"], selected_option, remaining_time)
                pygame.display.update()
        else:
            draw_board()
            pygame.display.update()
        
        clock.tick(30)

if __name__ == "__main__":
    main()
