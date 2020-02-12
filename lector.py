#!/usr/bin/python3
# importacion de librerias
import argparse
#-------------
#2 Funciones

def leer_archivo(archivo):
    try:
        with open(archivo,"r") as fh:
            texto = fh.read()
            renglones = texto.splitlines()
            texto_limpio = " ".join(renglones)
    except:
        texto_limpio = ""
    return texto_limpio
    '''
    Lector = open(archivo,"r")
    Texto = Lector.read()
    Renglones = Texto.splitlines()
    Texto_Limpio = " ".join(Renglones)
    return Texto_Limpio
    '''
    
def contar_palabras(texto):
    Palabras = texto.split(" ")
    Diccionario = dict()
    for palabra in Palabras:
        p = palabra.strip(",.")
        if p in Diccionario:
            Diccionario[p] += 1
        else:
            Diccionario[p] = 1
    #del(Diccionario[""])
    return Diccionario
    
def imprime_diccionario(dp,minimo):
    lista = [(k,v) for k,v in dp.items() if v>=minimo]
    lista_ordenada = sorted(lista, key= lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
        print(tupla[0],"= ",tupla[1])
    return
    
def leer_stopwords(archivo):
    try:
        with open(archivo,"r") as fh:
            lista = fh.readlines()
        lista_palabras = [palabra.strip("\n") for palabra in lista]
        return set(lista_palabras)
    except:
        return set()

def limpia_diccionario(dp,set_stop):
    ndp = {}
    for k,v in dp.items():
        if k.lower() not in set_stop:
            ndp[k] = v
    return ndp

    
def main(archivo, minimo):
    texto = leer_archivo(archivo)
    dip = contar_palabras(texto)
    set_stop = leer_stopwords("/home/cassiopea/josenoriega/spanish_stopwords.txt")
    ndip = limpia_diccionario(dip,set_stop)
    #print(dip)
    imprime_diccionario(ndip,minimo)
#--------------------------------

#3 Ejecucion de main

if __name__ == "__main__":
    #archivo = "/tmp/episodio4.txt"
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", dest="archivo", help="nombre de archivo", required=True)
    parser.add_argument("-m", "--minimo", dest="minimo", help="minimo de repeticiones", required=False, default=2, type=int)
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    main(archivo,minimo)