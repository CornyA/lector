#!/usr/bin/python3
import argparse
import lector

'''"Pensado en otro idioma"
def invertir(archivo):
    texto = lector.leer_archivo(archivo)
    lista_palabras = texto.split(" ")
    tam_lista = len(lista_palabras)
    lista_invertida = []
    for i in range(tam_lista-1,-1,-1):
        lista_invertida.append(lista_palabras[i])
    return lista_invertida
'''
def invertir(archivo):
    '''Recibe la ruta del archivo a leer y regresa
       una lista con las palabras en el texto en orden
       invertido.'''
    texto = lector.leer_archivo(archivo)
    lista_palabras = texto.split(" ")
    #tam_lista = len(lista_palabras)
    lista_invertida = []
    for palabra in lista_palabras:
        lista_invertida.insert(0,palabra)
    return lista_invertida

def escribir_invertido(fichero,lista_invertida):
    '''Recibe un fichero en el cual se va a escribir un texto
       y una lista invertida que será la que se escribirá.'''
    texto_invertido = " ".join(lista_invertida)
    try:
        with open(fichero,"w") as fw:
            fw.write(texto_invertido)
    except:
        print("Hubo un error")

def main(archivo,fichero):
    lista_invertida = invertir(archivo)
    escribir_invertido(fichero,lista_invertida)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--archivo", dest="archivo",help="Ruta de archivo",required=True)
    parser.add_argument("-o","--output", dest="output",help="Nombre de fichero",required=True)
    args = parser.parse_args()
    archivo = args.archivo
    fichero = args.output
    main(archivo,fichero)
