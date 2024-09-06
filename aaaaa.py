import pygame
import sys
import random
import time

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
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0
        self.x, self.y = BOARD_POSITIONS[0]
        self.correct_answers = 0  # Contador de respuestas correctas

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

# Crear jugadores
user_player = Player("Usuario", BLUE)
bot_player = Player("Bot", RED)
players = [user_player, bot_player]
current_player = 0

# Crear un dado virtual
def roll_dice():
    return random.randint(1, 6)

# Pregunta aleatoria con opciones
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
        pygame.draw.circle(screen, player.color, (player.x + 40, player.y + 40), 30)

    # Mostrar el contador de respuestas correctas en tamaño pequeño
    for player in players:
        text_surface = small_font.render(f"{player.name}: {player.correct_answers}", True, BLACK)
        screen.blit(text_surface, (20, 20 + players.index(player) * 30))

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

# El bot elige una opción al azar
def bot_choose_option(options):
    return random.randint(0, len(options) - 1)

# Bucle principal del juego
game_over = False
message = ""
question_message = ""
answer_message = ""
question_active = False
correct_answer = ""
options = []
selected_option = 0
start_time = 0

# Crear reloj para controlar el frame rate
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not question_active:
                if current_player == 0:  # Solo el jugador puede lanzar el dado
                    # El jugador actual lanza el dado
                    dice_roll = roll_dice()
                    message = f"{players[current_player].name} tiró un {dice_roll}"
                    
                    # Mover al jugador actual
                    players[current_player].move(dice_roll)
                    current_position = players[current_player].position
                    message += f" y se movió a la casilla {current_position + 1}"

                    # Si cae en una casilla con una pregunta
                    if current_position in random.sample(range(1, 19), 5):  # Casillas con preguntas aleatorias
                        question = ask_random_question()
                        question_message = question["question"]
                        correct_answer = question["answer"]
                        options = question["options"]
                        question_active = True  # Activar el estado de pregunta
                        selected_option = 0  # Reiniciar opción seleccionada
                        start_time = time.time()  # Iniciar temporizador

                    # Verificar si el jugador actual ha llegado al final
                    if current_position == len(BOARD_POSITIONS) - 1:
                        message = f"{players[current_player].name} ha ganado el juego!"
                        game_over = True

                    # Cambiar de turno
                    current_player = (current_player + 1) % 2

            if event.key == pygame.K_UP and question_active and current_player == 0:
                selected_option = (selected_option - 1) % len(options)
            elif event.key == pygame.K_DOWN and question_active and current_player == 0:
                selected_option = (selected_option + 1) % len(options)
            elif event.key == pygame.K_RETURN and question_active and current_player == 0:
                # El jugador elige la opción
                if options[selected_option].lower() == correct_answer.lower():
                    answer_message = "¡Respuesta correcta!"
                    players[current_player].correct_answers += 1
                else:
                    answer_message = f"Incorrecto. La respuesta era: {correct_answer}"
                question_active = False  # La pregunta ha sido contestada

    if not question_active and not game_over and current_player == 1:
        # El bot juega automáticamente
        dice_roll = roll_dice()
        message = f"{players[current_player].name} tiró un {dice_roll}"
        
        # Mover al bot
        players[current_player].move(dice_roll)
        current_position = players[current_player].position
        message += f" y se movió a la casilla {current_position + 1}"

        # Si cae en una casilla con una pregunta
        if current_position in random.sample(range(1, 19), 5):  # Casillas con preguntas aleatorias
            question = ask_random_question()
            question_message = question["question"]
            correct_answer = question["answer"]
            options = question["options"]
            selected_option = bot_choose_option(options)  # El bot elige una opción
            question_active = True  # Activar el estado de pregunta
            start_time = time.time()  # Iniciar temporizador

        # Verificar si el bot ha llegado al final
        if current_position == len(BOARD_POSITIONS) - 1:
            message = f"{players[current_player].name} ha ganado el juego!"
            game_over = True

        # Cambiar de turno
        current_player = (current_player + 1) % 2

    # Actualizar el temporizador
    if question_active:
        remaining_time = countdown_timer(start_time)
        if remaining_time == 0:  # Se acabó el tiempo
            answer_message = f"Se acabó el tiempo. La respuesta correcta era: {correct_answer}"
            question_active = False

        # Mostrar la pantalla de preguntas
        show_question_screen(question_message, options, selected_option, remaining_time)

    # Dibujar tablero y actualizar pantalla
    else:
        draw_board()

        # Mostrar el mensaje del dado y movimiento
        if message:
            display_text(message, BLACK, 0)

        # Mostrar la respuesta si ha sido respondida
        if answer_message:
            display_text(answer_message, RED, 50)

    pygame.display.update()
    clock.tick(30)  # Limitar a 30 fotogramas por segundo
