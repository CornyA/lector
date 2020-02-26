#!/usr/bin/python3
import argparse
import lector
import os
import concatenar

def get_listaEp(folder,inicia,termina):
    lista_direcciones = os.listdir(folder)
    lista_txt = [archivo for archivo in lista_direcciones if archivo.endswith(termina)]
    if inicia != None:
        lista_archivos = [archivo for archivo in lista_txt if archivo.startswith(inicia)]
        return lista_archivos
    else:
        return lista_txt
    #lista_archivos = [archivo for archivo in os.listdir(folder) if archivo.startswith(inicia) and archivo.endswith(termina)]
    #return lista_archivos
    
def get_ruta(folder,lista):
    lista_rutas = [os.path.join(folder,ep) for ep in lista]
    return lista_rutas

def main(folder,inicia,termina,fichero):
    lista_ep = get_listaEp(folder,inicia,termina)
    lista_ep.sort()
    lista_rutas = get_ruta(folder,lista_ep)
    concatenar.escribir_archivo(lista_rutas,fichero)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", dest="folder", help="Ruta de carpeta", required=True)
    parser.add_argument("-i", "--inicia", dest="inicia", help="Nombre del archivo buscado", required=False, default=None)
    parser.add_argument("-t", "--termina", dest="termina", help="Terminacion del archivo buscado", required=True)
    parser.add_argument("-o", "--output", dest="output", help="Nuevo fichero a crear", required=True)
    args = parser.parse_args()
    ruta = args.folder
    inicia = args.inicia
    tipo_archivo = args.termina
    fichero = args.output
    main(ruta,inicia,tipo_archivo,fichero)