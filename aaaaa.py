import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Camino Simple")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir posiciones de las casillas
BOARD_POSITIONS = [(100 * i + 50, 200) for i in range(8)]

# Definir preguntas aleatorias
QUESTIONS = [
    {"question": "¿Cuál es el planeta más cercano al sol?", "answer": "Mercurio"},
    {"question": "¿Cuántos continentes hay en la Tierra?", "answer": "7"},
    {"question": "¿Qué gas es esencial para la respiración?", "answer": "Oxígeno"},
    {"question": "¿En qué continente se encuentra Egipto?", "answer": "África"},
]

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
    question = random.choice(QUESTIONS)
    print(f"Pregunta: {question['question']}")
    return question['answer']

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

# Bucle principal del juego
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not game_over:
                # El jugador actual lanza el dado
                dice_roll = roll_dice()
                print(f"{players[current_player].name} tiró un {dice_roll}")

                # Mover al jugador actual
                players[current_player].move(dice_roll)
                current_position = players[current_player].position
                print(f"{players[current_player].name} se movió a la casilla {current_position + 1}")

                # Si cae en una casilla con una pregunta
                if current_position in random.sample(range(1, 7), 2):  # Casillas con preguntas aleatorias
                    correct_answer = ask_random_question()
                    if players[current_player] == user_player:
                        user_answer = input("Tu respuesta: ")
                        if user_answer.lower() == correct_answer.lower():
                            print("¡Respuesta correcta!")
                        else:
                            print(f"Respuesta incorrecta. La correcta era: {correct_answer}")
                    else:
                        print(f"El {players[current_player].name} pasó por una casilla de pregunta.")

                # Verificar si el jugador actual ha llegado al final
                if current_position == len(BOARD_POSITIONS) - 1:
                    print(f"{players[current_player].name} ha ganado el juego!")
                    game_over = True

                # Cambiar de turno
                current_player = (current_player + 1) % 2

    # Dibujar tablero y actualizar pantalla
    draw_board()
    pygame.display.update()
