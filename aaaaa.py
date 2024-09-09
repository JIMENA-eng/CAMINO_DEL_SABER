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

    def auto_answer(self, question):
        # El bot responde automáticamente seleccionando una opción al azar
        selected_option = random.choice(question["options"])
        return selected_option

# Crear jugadores
user_player = Player("Usuario", RED)
bot_player = Player("Bot", BLUE)
players = [user_player, bot_player]
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

    # Dibujar el área del dado
    pygame.draw.rect(screen, BLACK, pygame.Rect(WIDTH - 120, HEIGHT - 120, 100, 100), 2)
    pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH - 118, HEIGHT - 118, 96, 96))  # Dado blanco
    dice_value_surface = font.render(str(dice_roll), True, BLACK)
    screen.blit(dice_value_surface, (WIDTH - 100, HEIGHT - 100))

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

# Función para generar un código aleatorio
def generate_code():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

# Pantalla de inicio
def show_start_screen():
    screen.fill(WHITE)
    
    # Botón "Solitario"
    solitary_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
    pygame.draw.rect(screen, BLUE, solitary_button)
    solitary_text = font.render("Solitario", True, WHITE)
    screen.blit(solitary_text, (WIDTH // 2 - solitary_text.get_width() // 2, HEIGHT // 2 - solitary_text.get_height() // 2))
    
    # Botón "Invitar"
    invite_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)
    pygame.draw.rect(screen, GREEN, invite_button)
    invite_text = font.render("Invitar", True, WHITE)
    screen.blit(invite_text, (WIDTH // 2 - invite_text.get_width() // 2, HEIGHT // 2 + 20 + invite_text.get_height() // 2))
    
    pygame.display.update()
    
    return solitary_button, invite_button

# Mostrar pantalla de invitación
def show_invite_screen(code):
    screen.fill(WHITE)
    invite_message = font.render(f"Comparte este código para invitar a otros jugadores: {code}", True, BLACK)
    screen.blit(invite_message, (20, HEIGHT // 2 - invite_message.get_height() // 2))
    pygame.display.update()

# Bucle principal del juego
def main_game():
    global current_player, question_active, correct_answer, options, selected_option, start_time, dice_roll
    
    game_over = False
    message = ""
    question_message = ""
    answer_message = ""
    question_active = False
    correct_answer = ""
    options = []
    selected_option = 0
    start_time = 0
    
    clock = pygame.time.Clock()
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Comprobar si se ha hecho clic en el área del dado
                if WIDTH - 120 <= mouse_x <= WIDTH - 20 and HEIGHT - 120 <= mouse_y <= HEIGHT - 20:
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
                        break

                    # Cambiar de turno al bot
                    current_player = (current_player + 1) % 2

            if event.type == pygame.KEYDOWN and question_active:
                # Navegar por las opciones de respuesta con las teclas arriba y abajo
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    # El jugador elige la opción
                    if options[selected_option].lower() == correct_answer.lower():
                        answer_message = "¡Respuesta correcta!"
                        if current_player == 0:  # Usuario
                            bot_player.correct_answers += 1  # Incrementar el contador del bot
                        else:  # Bot
                            user_player.correct_answers += 1  # Incrementar el contador del usuario
                    else:
                        answer_message = f"Incorrecto. La respuesta era: {correct_answer}"
                    question_active = False  # Terminar el estado de pregunta

        # Lógica de temporizador de preguntas
        if question_active:
            remaining_time = countdown_timer(start_time)
            if remaining_time == 0:
                answer_message = f"Tiempo agotado. La respuesta era: {correct_answer}"
                question_active = False

        # Movimiento automático del bot
        if not question_active and current_player == 1:  # Si es el turno del bot
            dice_roll = roll_dice()
            message = f"{players[current_player].name} tiró un {dice_roll}"
            
            # Mover al bot
            bot_player.move(dice_roll)
            current_position = bot_player.position
            message += f" y se movió a la casilla {current_position + 1}"

            # Si cae en una casilla con una pregunta
            if current_position in random.sample(range(1, 19), 5):  # Casillas con preguntas aleatorias
                question = ask_random_question()
                selected_option = bot_player.auto_answer(question)  # Bot responde automáticamente
                if selected_option.lower() == question["answer"].lower():
                    answer_message = "¡Respuesta correcta!"
                    bot_player.correct_answers += 1  # Incrementar el contador del bot
                else:
                    answer_message = f"Incorrecto. La respuesta era: {question['answer']}"

            # Cambiar de turno al usuario
            current_player = (current_player + 1) % 2

        # Actualizar pantalla
        draw_board()
        if question_active:
            show_question_screen(question_message, options, selected_option, remaining_time)
        if message:
            display_text(message, BLACK, y_offset=0)
        if answer_message:
            display_text(answer_message, RED, y_offset=50)

        pygame.display.update()
        clock.tick(30)  # Limitar a 30 fotogramas por segundo

# Pantalla principal
def main():
    while True:
        solitary_button, invite_button = show_start_screen()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if solitary_button.collidepoint(mouse_x, mouse_y):
                        main_game()
                        return
                    elif invite_button.collidepoint(mouse_x, mouse_y):
                        code = generate_code()
                        show_invite_screen(code)
                        time.sleep(5)  # Mostrar el código por 5 segundos
                        break

if __name__ == "__main__":
    main()
