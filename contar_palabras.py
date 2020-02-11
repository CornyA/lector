#!/usr/bin/python3
import lector
import argparse

def porcentaje_palabras_stop(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    tam_texto = len(texto)
    tam_dip = len(diccionario)
    tam_resta = tam_texto - tam_dip
    tam_porcentaje = (tam_resta*100)/tam_texto
    print("Palabras en el texto: ",tam_texto)
    print("Diccionario de palabras: ",tam_dip)
    return tam_porcentaje
    
def palabras_unicas(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    palabras = texto.split()
    d_clave = {}
    d_stop = {}
    


def main(archivo):
    porcentaje = porcentaje_palabras_stop(archivo)
    print(porcentaje,"% Stop Words")
    print((100-porcentaje),"% Palabras clave")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", dest="archivo", help="Directorio del archivo", required=True)
    parser.add_argument("-s", "--stopwords", dest= "stopwords", help="Directorio de StopWords", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    sw = args.stopwords
    main(archivo)
