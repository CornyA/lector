#!/usr/bin/python3
import lector
import argparse

def palabras(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    


def main(ahrchivo):
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", dest="archivo", help="Directorio del archivo", required=True)
    parser.add_argument("-s", "--stopwords", dest= "stopwords", help="Directorio de StopWords", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    sw = args.stopwords
    main(archivo)
