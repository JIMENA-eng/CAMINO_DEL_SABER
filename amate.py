import tkinter as tk
from tkinter import messagebox
import random

# Clase de propiedad
class Propiedad:
    def __init__(self, nombre, precio, alquiler):
        self.nombre = nombre
        self.precio = precio
        self.alquiler = alquiler
        self.propietario = None

    def comprar(self, jugador):
        if jugador.dinero >= self.precio:
            jugador.dinero -= self.precio
            self.propietario = jugador
            jugador.propiedades.append(self)
            messagebox.showinfo("Compra", f"{jugador.nombre} compró {self.nombre} por {self.precio}.")
        else:
            messagebox.showwarning("Error", f"{jugador.nombre} no tiene suficiente dinero para comprar {self.nombre}.")

    def cobrar_alquiler(self, jugador):
        if self.propietario and self.propietario != jugador:
            jugador.dinero -= self.alquiler
            self.propietario.dinero += self.alquiler
            messagebox.showinfo("Alquiler", f"{jugador.nombre} pagó {self.alquiler} de alquiler a {self.propietario.nombre} por {self.nombre}.")
        elif self.propietario == jugador:
            messagebox.showinfo("Propietario", f"{jugador.nombre} ya es el propietario de {self.nombre}.")

# Clase de jugador
class Jugador:
    def __init__(self, nombre, label):
        self.nombre = nombre
        self.dinero = 1500
        self.posicion = 0
        self.propiedades = []
        self.label = label  # Etiqueta gráfica para mostrar la información del jugador

    def actualizar_label(self):
        self.label.config(text=f"{self.nombre}: ${self.dinero}")

    def mover(self, pasos, tablero):
        self.posicion = (self.posicion + pasos) % len(tablero)
        casilla_actual = tablero[self.posicion]
        messagebox.showinfo("Movimiento", f"{self.nombre} aterrizó en {casilla_actual.nombre}.")

        if casilla_actual.propietario is None:
            casilla_actual.comprar(self)
        else:
            casilla_actual.cobrar_alquiler(self)

        self.actualizar_label()

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

# Función para manejar los turnos
def turno_jugador(jugador, tablero, boton):
    dado = lanzar_dado()
    messagebox.showinfo("Dado", f"{jugador.nombre} lanzó un {dado}.")
    jugador.mover(dado, tablero)

    # Revisar si algún jugador se queda sin dinero
    if jugador.dinero <= 0:
        messagebox.showinfo("Fin del juego", f"{jugador.nombre} se ha quedado sin dinero. Fin del juego.")
        boton.config(state="disabled")

# Función principal del juego
def jugar_monopolio():
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Juego de Monopoly")

    # Crear el tablero
    tablero = [
        Propiedad("Salida", 0, 0),
        Propiedad("Mediterranean Avenue", 60, 2),
        Propiedad("Baltic Avenue", 60, 4),
        Propiedad("Oriental Avenue", 100, 6),
        Propiedad("Vermont Avenue", 100, 6),
        Propiedad("Connecticut Avenue", 120, 8)
    ]

    # Crear jugadores con etiquetas gráficas
    etiqueta_jugador1 = tk.Label(ventana, text="Jugador 1: $1500")
    etiqueta_jugador1.pack()
    jugador1 = Jugador("Jugador 1", etiqueta_jugador1)

    etiqueta_jugador2 = tk.Label(ventana, text="Jugador 2: $1500")
    etiqueta_jugador2.pack()
    jugador2 = Jugador("Jugador 2", etiqueta_jugador2)

    jugadores = [jugador1, jugador2]

    # Botón para turno del Jugador 1
    boton_jugador1 = tk.Button(ventana, text="Turno Jugador 1", command=lambda: turno_jugador(jugador1, tablero, boton_jugador1))
    boton_jugador1.pack()

    # Botón para turno del Jugador 2
    boton_jugador2 = tk.Button(ventana, text="Turno Jugador 2", command=lambda: turno_jugador(jugador2, tablero, boton_jugador2))
    boton_jugador2.pack()

    # Ejecutar la ventana
    ventana.mainloop()

# Iniciar el juego
jugar_monopolio()
