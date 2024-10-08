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
user_player = None
bot_player = Player("Bot", BLUE, pygame.image.load('path_to_bot_piece_image.png'))  # Reemplaza con la imagen del bot
players = [bot_player]  # Inicia solo con el bot

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
    box_size = 80

    # Dibujar casillas
    for pos in BOARD_POSITIONS:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], box_size, box_size), 2)

    # Dibujar jugadores
    for player in players:
        screen.blit(player.piece_image, (player.x, player.y))  # Dibuja la imagen de la ficha en lugar del círculo

    # Mostrar el contador de respuestas correctas en tamaño pequeño
    for player in players:
        text_surface = small_font.render(f"{player.name}: {player.correct_answers}", True, BLACK)
        screen.blit(text_surface, (20, 20 + players.index(player) * 30))

    # Dibujar el área del dado
    dice_area_size = 100
    pygame.draw.rect(screen, BLACK, pygame.Rect(WIDTH - dice_area_size - 20, HEIGHT - dice_area_size - 20, dice_area_size, dice_area_size), 2)
    pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH - dice_area_size + 2, HEIGHT - dice_area_size + 2, dice_area_size - 4, dice_area_size - 4))  # Dado blanco
    dice_value_surface = font.render(str(dice_roll), True, BLACK)
    screen.blit(dice_value_surface, (WIDTH - dice_area_size + 30, HEIGHT - dice_area_size + 20))

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

# Pantalla de bienvenida
def show_welcome_screen():
    screen.fill(WHITE)
    # Cargar la imagen
    welcome_image = pygame.image.load('camino del saber/pantalla.png')  # Asegúrate de usar la ruta correcta
    # Redimensionar la imagen si es necesario
    welcome_image = pygame.transform.scale(welcome_image, (WIDTH, HEIGHT))
    screen.blit(welcome_image, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)  # Mostrar la pantalla de bienvenida durante 2 segundos

# Pantalla de selección de modo de juego
def show_start_screen():
    screen.fill(WHITE)
    
    # Cargar imágenes de botones
    solitary_image = pygame.image.load('path_to_solitary_image.png')  # Asegúrate de usar la ruta correcta
    invite_image = pygame.image.load('path_to_invite_image.png')  # Asegúrate de usar la ruta correcta

    # Redimensionar imágenes si es necesario
    button_width = 200
    button_height = 50
    solitary_image = pygame.transform.scale(solitary_image, (button_width, button_height))
    invite_image = pygame.transform.scale(invite_image, (button_width, button_height))

    # Dibujar imágenes en la pantalla
    solitary_button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 - 60, button_width, button_height)
    invite_button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 + 60, button_width, button_height)
    screen.blit(solitary_image, solitary_button_rect.topleft)
    screen.blit(invite_image, invite_button_rect.topleft)

    pygame.display.update()
    
    return solitary_button_rect, invite_button_rect

# Pantalla de selección de ficha
def show_piece_selection_screen():
    screen.fill(WHITE)
    
    # Cargar imágenes de fichas
    piece_images = [
        pygame.image.load('path_to_piece1_image.png'),
        pygame.image.load('path_to_piece2_image.png'),
        pygame.image.load('path_to_piece3_image.png')
    ]
    
    # Redimensionar imágenes si es necesario
    piece_width = 100
    piece_height = 100
    piece_rects = []
    
    for i, piece_image in enumerate(piece_images):
        piece_image = pygame.transform.scale(piece_image, (piece_width, piece_height))
        piece_rect = pygame.Rect(WIDTH // 2 - piece_width // 2, HEIGHT // 2 - piece_height // 2 - 60 + i * (piece_height + 20), piece_width, piece_height)
        piece_rects.append(piece_rect)
        screen.blit(piece_image, piece_rect.topleft)
    
    # Cargar imagen de aceptar
    accept_image = pygame.image.load('path_to_accept_image.png')
    accept_image = pygame.transform.scale(accept_image, (150, 50))
    accept_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + piece_height // 2 + 40, 150, 50)
    screen.blit(accept_image, accept_button_rect.topleft)
    
    pygame.display.update()
    
    return piece_rects, accept_button_rect

# Pantalla de ingreso de nombre
def show_name_entry_screen():
    screen.fill(WHITE)
    
    # Mostrar campo de ingreso de nombre
    name_input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    pygame.draw.rect(screen, BLACK, name_input_box, 2)
    
    # Cargar imagen de aceptar
    accept_image = pygame.image.load('path_to_accept_image.png')
    accept_image = pygame.transform.scale(accept_image, (150, 50))
    accept_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50)
    screen.blit(accept_image, accept_button_rect.topleft)
    
    pygame.display.update()
    
    return name_input_box, accept_button_rect

# Pantalla de juego terminado
def show_end_screen(winner):
    screen.fill(WHITE)
    end_text = font.render(f"¡{winner} ha ganado!", True, BLACK)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)  # Mostrar la pantalla de fin durante 2 segundos

# Función principal del juego
def main():
    global current_player, user_player

    show_welcome_screen()
    
    solitary_button_rect, invite_button_rect = show_start_screen()
    
    game_started = False
    while not game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if solitary_button_rect.collidepoint(x, y):
                    # Selección de ficha
                    piece_rects, accept_button_rect = show_piece_selection_screen()
                    selected_piece = None
                    while selected_piece is None:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = pygame.mouse.get_pos()
                                for i, piece_rect in enumerate(piece_rects):
                                    if piece_rect.collidepoint(x, y):
                                        selected_piece = piece_images[i]
                                        break
                                if accept_button_rect.collidepoint(x, y):
                                    if selected_piece:
                                        # Ingreso de nombre
                                        name_input_box, accept_button_rect = show_name_entry_screen()
                                        name = ''
                                        active = True
                                        while active:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    sys.exit()
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_RETURN:
                                                        user_player = Player(name, BLACK, selected_piece)
                                                        players.append(user_player)
                                                        active = False
                                                    elif event.key == pygame.K_BACKSPACE:
                                                        name = name[:-1]
                                                    else:
                                                        name += event.unicode
                                                screen.fill(WHITE)
                                                pygame.draw.rect(screen, BLACK, name_input_box, 2)
                                                name_surface = font.render(name, True, BLACK)
                                                screen.blit(name_surface, (name_input_box.x + 5, name_input_box.y + 5))
                                                screen.blit(accept_image, accept_button_rect.topleft)
                                                pygame.display.update()
                                                if accept_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                    if name:
                                                        user_player = Player(name, BLACK, selected_piece)
                                                        players.append(user_player)
                                                        active = False
                                                        break
                                    break
                                if selected_piece:
                                    break
                    game_started = True
                    game_mode = 'solitario'
                    break
                elif invite_button_rect.collidepoint(x, y):
                    # Implementar lógica para invitar a otro jugador
                    pass
    
    if game_mode == 'solitario':
        while True:
            draw_board()
            pygame.display.update()
            
            # Lanzar dado
            roll_dice()
            display_text(f"Dado: {dice_roll}")
            
            # Mover jugador
            current_player_instance = players[current_player]
            current_player_instance.move(dice_roll)
            
            # Pregunta aleatoria
            question = ask_random_question()
            options = question["options"]
            correct_answer = question["answer"]
            
            # Pregunta y temporizador
            start_time = time.time()
            remaining_time = 10
            selected_option = None
            
            while remaining_time > 0:
                draw_board()
                pygame.display.update()
                remaining_time = countdown_timer(start_time)
                
                show_question_screen(question["question"], options, selected_option if selected_option is not None else -1, remaining_time)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            selected_option = 0
                        elif event.key == pygame.K_2:
                            selected_option = 1
                        elif event.key == pygame.K_3:
                            selected_option = 2
                        elif event.key == pygame.K_4:
                            selected_option = 3
                        if selected_option is not None:
                            if options[selected_option] == correct_answer:
                                current_player_instance.correct_answers += 1
                            break
                
                if selected_option is not None:
                    break
            
            if selected_option is not None and options[selected_option] == correct_answer:
                display_text("Respuesta correcta!", GREEN, 40)
            else:
                display_text("Respuesta incorrecta!", RED, 40)
            
            pygame.display.update()
            pygame.time.delay(1000)
            
            # Verificar si el jugador ha ganado
            if current_player_instance.position >= len(BOARD_POSITIONS) - 1:
                show_end_screen(current_player_instance.name)
                break
            
            # Cambiar de jugador
            current_player = (current_player + 1) % len(players)
            
    pygame.quit()

if __name__ == "__main__":
    main()
