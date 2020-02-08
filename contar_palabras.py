#!/usr/bin/python3
import lector
import argparse

def palabras(archivo):
    texto = lector.leer_archivo(archivo)

def main(archivo):
    print(palabras("/tmp/frankenstein.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", dest="archivo", help="Directorio del archivo", required=True)
    #parser.add_argument("-m", "--minimo", dest="minimo", help="Minimo de repeticiones", required=False, default=2, type=int)
    parser.add_argument("-s", "--stopwords", dest= "stopwords", help="Directorio de StopWords", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    #minimo = args.minimo
    sw = args.stopwords
    main(archivo)
