#!/usr/bin/python3
import argparse
import lector
import os

def get_ListaEp(folder,inicia,termina):
    lista_archivos = [archivo for archivo in os.listdir(folder) if archivo.startswith(inicia) and archivo.endswith(termina)
    return lista_archivos
    
def escribir_episodios(lista,fichero):
    
    

def main(folder,inicia,termina,fichero):
    lista_ep = get_ListaEp(folder,inicia,termina)
    

if __name__ = "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", dest="folder", help="Ruta de carpeta", required=True)
    parser.add_argument("-i", "--inicia", dest="inicia", help="Nombre del archivo buscado", required=True)
    parser.add_argument("-t", "--termina", dest="termina", help="Terminacion del archivo buscado", required=True)
    parser.add_argument("-o", "--output", dest="output", help="Nuevo fichero a crear", required=True)
    args = parser.parse_args()
    ruta = args.folder
    inicia = args.inicia
    tipo_archivo = args.termina
    fichero = args.output
    main(ruta,inicia,tipo_archivo,fichero)