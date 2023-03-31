import pygame
from funcionesCLAVES import *
from pygame.locals import *
from configuracion import *



def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,correctas, incorrectas, casi):
    abcdario = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    defaultFont= pygame.font.Font('Minecraftia-Regular.ttf', TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font('Minecraftia-Regular.ttf', TAMANNO_LETRA_GRANDE)

#Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

#muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))

#muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (650, 10))

#muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

#muestra las palabras que se fueron arriesgando
    pos = 0
    intentos=5
    for palabra in listaDePalabrasUsuario:
        intentos-=1
        screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4,20 + 80 * pos))
        pos += 1

#Recorre abcdario y le pone color a las letras
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            if letra in correctas:
                color=COLOR_VERDE
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
                x += TAMANNO_LETRA
            elif letra in incorrectas:
                color=COLOR_ROJO
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
                x += TAMANNO_LETRA
            elif letra in casi:
                color=COLOR_AMARILLO
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
                x += TAMANNO_LETRA
            else:
                color = COLOR_LETRAS
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
                x += TAMANNO_LETRA
        y += TAMANNO_LETRA + 2
#Limpia la pantalla en caso de que el juego termine
    if gano:
        screen.fill(COLOR_FONDO)
    if intentos==0 and not gano:
        screen.fill(COLOR_FONDO)
    if segundos < 0 and not gano:
        screen.fill(COLOR_FONDO)


def categoria(largo,screen,gano,intentos,segundos): #Muestra en pantalla la categoria dependiendo del largo seleccionado al azar.
    defaultFont= pygame.font.Font('Minecraftia-Regular.ttf', TAMANNO_LETRA)
    if largo == 4:
        screen.blit(defaultFont.render("CATEGORIA:", 1, COLOR_TEXTO), (10, 40))
        screen.blit(defaultFont.render("Animales de 4 letras", 1, COLOR_TEXTO), (10, 70))
    elif largo == 5:
        screen.blit(defaultFont.render("CATEGORIA:", 1, COLOR_TEXTO), (10, 40))
        screen.blit(defaultFont.render("Países de 5 letras", 1, COLOR_TEXTO), (10, 70))
    else:
        screen.blit(defaultFont.render("CATEGORIA:", 1, COLOR_TEXTO), (10, 40))
        screen.blit(defaultFont.render("Películas de 6 letras", 1, COLOR_TEXTO), (10, 70))
    if gano:
        screen.fill(COLOR_FONDO)
    if intentos==0 and not gano:
        screen.fill(COLOR_FONDO)
    if segundos < 0 and not gano:
        screen.fill(COLOR_FONDO)



#muestra si ganaste o perdiste y la cantidad de puntos. Tambien reproduce sonido de victoria o derrota.
def resultado(screen,palabraCorrecta,gano,puntos,segundos,intentos):
    defaultFontGrande= pygame.font.Font('Minecraftia-Regular.ttf', TAMANNO_LETRA_GRANDE)
    defaultFont= pygame.font.Font('Minecraftia-Regular.ttf', TAMANNO_LETRA)
    if gano:
            pos=0
            screen.blit(defaultFontGrande.render("¡GANASTE!", 1, COLOR_VERDE), (ANCHO//2-len("¡GANASTE!")-10*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos += 2
            screen.blit(defaultFont.render("La palabra correcta es:", 1, COLOR_VERDE), (ANCHO//2-len("La palabra correcta es:")-70*TAMANNO_LETRA//4, 20 + 100 * pos))
            screen.blit(defaultFontGrande.render(palabraCorrecta, 1, COLOR_VERDE), (350, 180))
            pos +=2
            screen.blit(defaultFont.render("Su puntuación es:", 1, COLOR_VERDE), (ANCHO//2-len("Su puntuación es:")-70*TAMANNO_LETRA//4, 20 + 100 * pos))
            screen.blit(defaultFontGrande.render(str(puntos), 1, COLOR_VERDE), (350, 380))
            pos += 3
            pygame.mixer.music.load("sonidoVictoria.mp3")
            pygame.mixer.music.play()
    if intentos==0 and not gano:
            pos=0
            screen.blit(defaultFontGrande.render("¡PERDISTE!", 1, COLOR_ROJO), (ANCHO//2-len("¡PERDISTE!")-10*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos += 2
            screen.blit(defaultFont.render("La palabra correcta es:", 1, COLOR_ROJO), (ANCHO//2-len("La palabra correcta es:")-70*TAMANNO_LETRA//4, 20 + 100 * pos))
            screen.blit(defaultFontGrande.render(palabraCorrecta, 1, COLOR_ROJO), (350, 180))
            pos +=2
            screen.blit(defaultFont.render("Su puntuación es:", 1, COLOR_ROJO), (ANCHO//2-len("Su puntuación es:")-70*TAMANNO_LETRA//4, 20 + 100 * pos))
            screen.blit(defaultFontGrande.render(str(puntos), 1, COLOR_ROJO), (350, 380))
            pos += 3
            pygame.mixer.music.load("sonidoDerrota.mp3")
            pygame.mixer.music.play()
    if segundos < 0 and not gano:
            pos=0
            screen.blit(defaultFontGrande.render("¡PERDISTE!", 1, COLOR_ROJO), (ANCHO//2-len("¡PERDISTE!")-10*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos += 2
            screen.blit(defaultFont.render("La palabra correcta es:", 1, COLOR_ROJO), (ANCHO//2-len("La palabra correcta es:")-70*TAMANNO_LETRA//4, 20 + 100 * pos))
            screen.blit(defaultFontGrande.render(palabraCorrecta, 1, COLOR_ROJO), (350, 180))
            pos +=2
            screen.blit(defaultFont.render("Su puntuación es:", 1, COLOR_ROJO), (ANCHO//2-len("Su puntuación es:")-70*TAMANNO_LETRA//4, 20 + 100 * pos))
            puntos=0
            screen.blit(defaultFontGrande.render(str(puntos), 1, COLOR_ROJO), (350, 380))
            pos += 3
            pygame.mixer.music.load("sonidoDerrota.mp3")
            pygame.mixer.music.play()

#muestra un cartel en pantalla cuando el usuario quiere ingresar una palabra no valida.
def mostrarError(screen, listaDefinitiva, listaDePalabrasErroneas,palabraCorrecta,palabraUsuario):
    defaultFont= pygame.font.Font('Minecraftia-Regular.ttf', TAMANNO_LETRA)
#Para que el cartel no sea molesto procuramos que solo se muestre cuando la palabra que el usuario desea ingresar es igual o mayor a la palabra correcta.
    if len(palabraUsuario)>=len(palabraCorrecta):
        for palabra in listaDePalabrasErroneas:
            screen.fill(COLOR_FONDO)
            pos=5
            screen.blit(defaultFont.render("La palabra que desea ingresar no existe", 1, COLOR_ROJO), (ANCHO//2-len("La palabra que desea ingresar no existe")-3*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos+=1
            screen.blit(defaultFont.render("o la longitud es incorrecta", 1, COLOR_ROJO), (ANCHO//2-len("o la longitud es incorrecta")-3*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos+=1
    if palabraUsuario in listaDefinitiva:
        #Cuando el usuario escribe una palabra valida el cartel desaparece
                screen.fill(COLOR_FONDO)

















