#!/usr/bin/python3
import argparse
import lector
import contar_palabras

def obten_cita(texto,inicio,cuenta):
    lista = texto.split(" ")
    longitud = len(lista)
    if(inicio+cuenta)< longitud:
        lista_palabras = lista[inicio:inicio+cuenta]
        cita = " ".join(lista_palabras)
    else:
        cita = ""
    return cita
    
def main(archivo,archivo_stop,inicio,cuenta):
     
     texto = lector.leer_archivo(archivo)
     cita = obten_cita(texto,inicio,cuenta)
     print("cita:", cita)
     stopwords = lector.leer_stopwords(archivo_stop)
     contar_palabras.contar(cita,stopwords)
     #contar_palabras.porcentaje_palabras(cita,stopwords)
     
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--archivo', dest='archivo', help='Nombre del archivo.', required=True)
    parser.add_argument('-i', '--inicio', dest='inicio', help='Palabra en la que inicia la cita.', required=True, type=int)
    parser.add_argument('-c', '--cuenta', dest='cuenta', help='Cantidad de palabras a citar.', required=True, type=int, default = 10)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help='Archivo de stopwords', required=True)
    
    args = parser.parse_args()
    archivo = args.archivo
    inicio = args.inicio
    cuenta = args.cuenta
    stopwords = args.stopwords
    
    main(archivo,stopwords,inicio,cuenta)
    
'''
def extraer_cita(inicio, cantidad, texto):
    inicio = inicio - 1 if inicio > 0 else inicio

    unwanted_strings = ["", "\ufeff"]

    # separar texto por palabras y remover saltor de linea
    palabras = [palabra.strip('\n\t') for palabra in texto.split(' ')]
    # remover strings vacios de lista de palabras
    palabras = [p for p in palabras if p not in unwated_strings]

    return ' '.join(palabras[inicio: inicio + cantidad])


def main(args):
    archivo = args.archivo
    archivo_stopwords = args.stopwords
    inicio = args.inicio
    cantidad = args.cantidad

    texto = lector.leer_archivo(archivo)
    cita = extraer_cita(inicio, cantidad, texto)

    print(cita)
    contarpalabras.main(cita, archivo_stopwords)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--archivo', dest='archivo', help='Nombre del archivo.', required=True)
    parser.add_argument('-i', '--inicio', dest='inicio', help='Palabra en la que inicia la cita.', required=True, type=int)
    parser.add_argument('-c', '--cantidad', dest='cantidad', help='Cantidad de palabras a citar.', required=True, type=int)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help='Archivo de stopwords', required=True)

    args = parser.parse_args()
    main(args)
'''