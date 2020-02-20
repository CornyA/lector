#!/usr/bin/python3
import argparse
import lector

def escribir_archivo(lista_archivos,nuevo_fichero):
    textos = []
    for archivo in lista_archivos:
        texto = lector.leer_archivo(archivo)
        textos.append(texto)
        
    try:
        with open(nuevo_fichero,'w', encoding='utf-8') as fw:
            #texto = lector.leer_archivo(archivo)
            texto_limpio = " ".join(textos)
            nuevo_fichero = fw.write(texto_limpio)
    except:
        print("Hubo un error")
                
            
def main(lista_archivos,nuevo_fichero):
    escribir_archivo(lista_archivos,nuevo_fichero)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--archivo", dest = "archivo", help="Ruta de archivos", action="append", required=True)
    parser.add_argument("-o","--output", dest = "output", help ="Nombre de nuevo fichero", required = True)
    args = parser.parse_args()
    lista_archivos = args.archivo
    nuevo_fichero = args.output
    main(lista_archivos,nuevo_fichero)