import random


def quitarSaltos(archivo):
#Elimina los \n del archivo
          lineas=archivo.readlines()
          listaPalabrasDiccionario=list(map (lambda l: l.rstrip("\n"),lineas))
          return(listaPalabrasDiccionario)


def dondeEsta(palabra,let):
#devuelve una lista de enteros que indican la posicion de las letras en la palabra
    cont=0
    posiciones=[]
    for letra in palabra:
        cont=cont+1
        if letra==let:
            posiciones.append(cont)
    return(posiciones)


def nuevaPalabra(salida):
#devuelve una palabra tomada al azar de la lista definitiva.
           palabraCorrecta=random.choice(salida)
           return(palabraCorrecta)


def lectura(archivo, salida, largo):
#rellena la lista definitiva
       for palabra in archivo:
           if len(palabra) == largo:
              salida.append(palabra)


def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
#devuelve true o false dependiendo de si el jugador adivino o no
#Tambien rellena las listas correctas, incorrectas y casi con las letras correspondientes
    if palabra==palabraCorrecta:
        return(True)
    for letra in palabra:
        if not letra in palabraCorrecta:
            incorrectas.append(letra)
        if dondeEsta(palabra,letra)==dondeEsta(palabraCorrecta,letra):
            correctas.append(letra)
        if letra in palabraCorrecta and dondeEsta(palabra,letra)!=dondeEsta(palabraCorrecta,letra):
            casi.append(letra)
    return(False)












