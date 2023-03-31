import sys
import pygame
from principal import *


class Menu:

    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('Minecraftia-Regular.ttf', 40)
        self.seleccionado = 0
        self.total = len(self.opciones)

    def actualizar(self):
        #Altera el valor de 'self.seleccionado' con los direccionales.

        k = pygame.key.get_pressed()

        if k[K_UP]:
            self.seleccionado -= 1
        elif k[K_DOWN]:
            self.seleccionado += 1
        elif k[K_RETURN]:

            # Invoca a la función asociada a la opción.
            titulo, funcion = self.opciones[self.seleccionado]
            funcion()

        # procura que self.seleccionado esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

    def imprimir(self, screen):
        #Imprime sobre 'screen' el texto de cada opción del menú.

        indice = 0
        altura_de_opcion = 80
        x = 325
        y = 250
        for (titulo, funcion) in self.opciones:
                if indice == self.seleccionado:
                    color = COLOR_VERDE
                else:
                    color = COLOR_TEXTO
                imagen = self.font.render(titulo, 1, color)
                posicion = (x, y + altura_de_opcion * indice)
                indice += 1
                screen.blit(imagen, posicion)

#FUNCIONES QUE SE EJECUTAN DEPENDIENDO LO QUE ELIJA EL USUARIO

def juego(): #Cierra el menu e inicia el juego
    pygame.quit()
    main()

def salida(): #Cierra el menu y no inicia el juego
    pygame.quit()
    sys.exit()


#FUNCION PARA INVOCAR AL MENU
def menu():
    pygame.init()

#Le agrega música al menú
    pygame.mixer.music.load("musicaMENU.mp3")
    pygame.mixer.music.play()

#Le agrega nombre a la ventana
    pygame.display.set_caption("Menu principal")

    salir = False

#Define la lista opciones con el texto a mostrar en pantalla y las funciones correspondientes.
    opciones = [("Jugar", juego),("Salir", salida)]

    screen = pygame.display.set_mode((ANCHO, ALTO))
    fondo = pygame.image.load("fondo_juego.jpg").convert()
    menu = Menu(opciones) #Utiliza el metodo __init__

    while not salir:

        for e in pygame.event.get():

            screen.blit(fondo, (0, 0)) #Muestra el fondo
            menu.actualizar() #Cambia la posición de self.seleccionado (direccionales)
            menu.imprimir(screen) #Imprime sobre 'screen' el texto de cada opción del menú
            pygame.display.flip()

            if e.type == QUIT:
                pygame.quit() #Cierra el juego
                salir=True #Finaliza el ciclo WHILE













