#!/usr/bin/python3
import lector
import argparse
import random

def obtener_palabras_aleatorias(archivo,num_pal):
    '''Recibe la ruta del archivo y el numero de palabras
       aleatorias que se desea extraer del archivo y regresa
       una lista con las palabras aleatorias obtenidas.'''
    texto = lector.leer_archivo(archivo)
    lista_palabras = texto.split(" ")
    lista_palabras = remover_espacios(lista_palabras)
    lista_aleatoria = []
    tam_texto = len(lista_palabras)
    for i in range(0,num_pal):
        rand = random.randint(0,tam_texto-1)
        palabra = lista_palabras[rand]
        lista_aleatoria.append(palabra)
    return lista_aleatoria
    
def remover_espacios(lista_palabras):
    '''Recibe una lista de palabras y se regresa una lista
       sin puntos, comas y espacios.'''
    lista_limpia = [palabra.rstrip(",.") for palabra in lista_palabras if len(palabra)>0]
    return lista_limpia

def main(archivo,num_pal):
    lista_aleatoria = obtener_palabras_aleatorias(archivo,num_pal)
    print(lista_aleatoria)
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", dest="archivo", help="nombre de archivo", required=True)
    parser.add_argument("-n", "--numpal", dest="numpal", help="Numero de palabras aleatorias", required=False, default=3, type=int)
    args = parser.parse_args()
    archivo = args.archivo
    numpal = args.numpal
    main(archivo,numpal)
    