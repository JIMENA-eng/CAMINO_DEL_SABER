import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly Simplificado")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definir variables del jugador
class Player:
    def __init__(self, name, color, money=1500):
        self.name = name
        self.color = color
        self.position = 0
        self.money = money
        self.properties = []

    def move(self, steps):
        self.position = (self.position + steps) % len(BOARD_POSITIONS)

# Definir propiedades
class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = None

# Crear el tablero
BOARD_POSITIONS = [
    (700, 700), (600, 700), (500, 700), (400, 700), (300, 700), (200, 700), (100, 700), (50, 700),
    (50, 600), (50, 500), (50, 400), (50, 300), (50, 200), (50, 100), (50, 50), (150, 50),
    (250, 50), (350, 50), (450, 50), (550, 50), (650, 50), (750, 50), (750, 150), (750, 250),
    (750, 350), (750, 450), (750, 550), (750, 650)
]

# Definir las propiedades (con un precio y una renta simplificada)
properties = [
    Property("Inicio", 0, 0),
    Property("Avenida Mediterráneo", 60, 2),
    Property("Comunidad", 0, 0),
    Property("Avenida Báltica", 60, 4),
    Property("Impuestos", 0, 0),
    Property("Ferrocarril Reading", 200, 25),
    Property("Avenida Oriental", 100, 6),
    Property("Suerte", 0, 0),
    Property("Avenida Vermont", 100, 6),
    Property("Avenida Connecticut", 120, 8),
    # Añadir más propiedades según sea necesario
]

# Crear jugadores
players = [Player("Jugador 1", BLUE), Player("Jugador 2", RED)]
current_player = 0

# Crear un dado virtual
def roll_dice():
    return random.randint(1, 6)

# Dibujar el tablero y los jugadores
def draw_board():
    screen.fill(WHITE)
    
    # Dibujar casillas
    for pos in BOARD_POSITIONS:
        pygame.draw.rect(screen, BLACK, pygame.Rect(pos[0], pos[1], 100, 100), 2)
    
    # Dibujar propiedades
    for idx, prop in enumerate(properties):
        pos = BOARD_POSITIONS[idx]
        if prop.owner:
            pygame.draw.rect(screen, prop.owner.color, pygame.Rect(pos[0]+10, pos[1]+10, 80, 80))
    
    # Dibujar jugadores
    for player in players:
        pos = BOARD_POSITIONS[player.position]
        pygame.draw.circle(screen, player.color, (pos[0] + 50, pos[1] + 50), 20)

# Lógica de comprar propiedad
def buy_property(player, property):
    if property.owner is None and property.cost > 0:
        if player.money >= property.cost:
            player.money -= property.cost
            player.properties.append(property)
            property.owner = player
            print(f"{player.name} compró {property.name} por ${property.cost}")

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Presionar espacio para tirar el dado
                dice_roll = roll_dice()
                print(f"{players[current_player].name} tiró un {dice_roll}")
                
                # Mover al jugador
                players[current_player].move(dice_roll)
                player_pos = players[current_player].position
                current_property = properties[player_pos]

                print(f"{players[current_player].name} está en {current_property.name}")

                # Ver si el jugador puede comprar la propiedad
                if current_property.owner is None:
                    buy_property(players[current_player], current_property)

                # Cambiar de turno
                current_player = (current_player + 1) % len(players)

    # Dibujar el tablero y actualizar la pantalla
    draw_board()
    pygame.display.update()
