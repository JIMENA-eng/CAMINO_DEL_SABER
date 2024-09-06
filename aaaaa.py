import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Camino Curvado")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definir posiciones de las casillas en forma de "gusano"
BOARD_POSITIONS = [
    (50, 50), (150, 50), (250, 50), (350, 50), (450, 50), (550, 50), (650, 50), (750, 50),
    (750, 150), (650, 150), (550, 150), (450, 150), (350, 150), (250, 150), (150, 150), (50, 150),
    (50, 250), (150, 250), (250, 250), (350, 250)
]

# Definir preguntas aleatorias
QUESTIONS = [
    {"question": "¿Cuál es el planeta más cercano al sol?", "answer": "Mercurio"},
    {"question": "¿Cuántos continentes hay en la Tierra?", "answer": "7"},
    {"question": "¿Qué gas es esencial para la respiración?", "answer": "Oxígeno"},
    {"question": "¿En qué continente se encuentra Egipto?", "answer": "África"},
]

# Fuente para texto
font = pygame.font.Font(None, 36)

# Definir clase Jugador
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0

    def move(self, steps):
        self.position = min(self.position + steps, len(BOARD_POSITIONS) - 1)

# Crear jugadores
user_player = Player("Usuario", BLUE)
bot_player = Player("Bot", RED)
players = [user_player, bot_player]
current_player = 0

# Crear un dado virtual
def roll_dice():
    return random.randint(1, 6)

# Pregunta aleatoria
def ask_random_question():
    return random.choice(QUESTIONS)

# Dibujar el tablero y los jugadores
def draw_board():
    screen.fill(WHITE)

    # Dibujar casillas
    for pos in BOARD_POSITIONS:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], 80, 80), 2)

    # Dibujar jugadores
    for player in players:
        pos = BOARD_POSITIONS[player.position]
        pygame.draw.circle(screen, player.color, (pos[0] + 40, pos[1] + 40), 30)

# Mostrar texto en la pantalla
def display_text(text, color=BLACK, y_offset=0):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (20, HEIGHT - 100 + y_offset))

# Bucle principal del juego
game_over = False
message = ""
question_message = ""
answer_message = ""
question_active = False
correct_answer = ""

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_over:
                if not question_active:  # No permitir tirar el dado si hay una pregunta activa
                    # El jugador actual lanza el dado
                    dice_roll = roll_dice()
                    message = f"{players[current_player].name} tiró un {dice_roll}"
                    
                    # Mover al jugador actual
                    players[current_player].move(dice_roll)
                    current_position = players[current_player].position
                    message += f" y se movió a la casilla {current_position + 1}"

                    # Si cae en una casilla con una pregunta
                    if current_position in random.sample(range(1, 19), 3):  # Casillas con preguntas aleatorias
                        question = ask_random_question()
                        question_message = question["question"]
                        correct_answer = question["answer"]
                        question_active = True  # Activar el estado de pregunta

                    # Verificar si el jugador actual ha llegado al final
                    if current_position == len(BOARD_POSITIONS) - 1:
                        message = f"{players[current_player].name} ha ganado el juego!"
                        game_over = True

                    # Cambiar de turno
                    current_player = (current_player + 1) % 2

        if event.type == pygame.KEYDOWN and question_active:
            # El usuario responde usando teclas (input simulado)
            if event.key == pygame.K_1:
                user_answer = "Mercurio"
            elif event.key == pygame.K_2:
                user_answer = "7"
            elif event.key == pygame.K_3:
                user_answer = "Oxígeno"
            elif event.key == pygame.K_4:
                user_answer = "África"
            else:
                user_answer = ""

            if user_answer:
                if user_answer.lower() == correct_answer.lower():
                    answer_message = "¡Respuesta correcta!"
                else:
                    answer_message = f"Incorrecto. La respuesta era: {correct_answer}"
                question_active = False  # La pregunta ha sido contestada

    # Dibujar tablero, jugadores y actualizar pantalla
    draw_board()
    
    # Mostrar el mensaje del dado y movimiento
    if message:
        display_text(message, BLACK, 0)

    # Mostrar la pregunta, si hay una activa
    if question_active:
        display_text("Pregunta: " + question_message, GREEN, 30)
        display_text("Responde con las teclas 1, 2, 3, 4", GREEN, 60)

    # Mostrar la respuesta si ha sido respondida
    if answer_message:
        display_text(answer_message, RED, 90)

    pygame.display.update()
