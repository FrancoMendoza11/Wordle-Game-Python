import os,sys, random, pygame
from configuracion import *
from extras import *
from funcionesCLAVES import *
from Menu import *


#Funcion principal
def main():

#Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

#Le agrega musica al juego
        pygame.mixer.music.load("musicaPYGAME.mp3")
        pygame.mixer.music.play()

#Preparar la ventana
        pygame.display.set_caption("La palabra escondida")
        screen = pygame.display.set_mode((ANCHO, ALTO))

#tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 50

        palabraUsuario = ""
        listaDePalabrasUsuario = []

#Lista que se rellena con las palabras no válidas que el usuario desee ingresar.
        listaDePalabrasErroneas=[]

#listas que se rellenan con las letras correspondientes de la palabra arriesgada.
        correctas = []
        incorrectas = []
        casi = []

        gano = False

#Lista que se rellena en la funcion lectura con las palabras del largo adecuado.
        listaDefinitiva=[]

        archivo= open("palabras.txt","r")
        listaProvisional=quitarSaltos(archivo)

#Selecciona el largo de las palabras al azar, cada largo corresponde a una tematica/categoria distinta.
        LARGO=random.randint(4,6)

#lectura del diccionario
        lectura(listaProvisional, listaDefinitiva, LARGO)

#elige una al azar
        palabraCorrecta=nuevaPalabra(listaDefinitiva)
        print(palabraCorrecta)

        intentos = 5

        while segundos > fps/1000 and intentos > 0 and not gano:

# 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

#Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

#QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()

#Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra #es la palabra que escribe el usuario
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
#Controla que las palabras ingresadas por el usuario sean de la longitud correcta, pertenezcan al diccionario y no sean repetidas.
                            if len(palabraUsuario)==len(palabraCorrecta) and palabraUsuario in listaDefinitiva and not palabraUsuario in listaDePalabrasUsuario:
                                gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                                listaDePalabrasUsuario.append(palabraUsuario)
                                palabraUsuario = ""
                                intentos -= 1
                                if not gano:
                                        puntos-=10
                            else:
                                listaDePalabrasErroneas.append(palabraUsuario)

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

#Limpia la pantalla para evitar que se superpongan los segundos mostrados en pantalla.
            screen.fill(COLOR_FONDO)

#Ejecuta la funcion para mostrar error solo cuando es necesario.
            if len(listaDePalabrasErroneas)>0:
                mostrarError(screen, listaDefinitiva,listaDePalabrasErroneas,palabraCorrecta,palabraUsuario)

#Muestra en pantalla lo esencial del juego
            dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi)

#Muestra en pantalla la categoria que el usuario se encuentra jugando
            categoria(LARGO,screen,gano,intentos,segundos)

#Muestra en pantalla el resultado una vez que la partida haya finalizado
            resultado(screen,palabraCorrecta,gano,puntos,segundos,intentos)

            pygame.display.flip()

        while 1:
#Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    return

        archivo.close()



#Programa Principal ejecuta el menu y luego dependiendo la opcion elegida ejecuta el juego o se cierra.
if __name__ == "__main__":
    menu()