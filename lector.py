#!/usr/bin/python3
# importacion de librerias
import argparse
#-------------
#2 Funciones

def leer_archivo(archivo):
    '''Recibe una cadena con el nombre del archivo que se
       busca leer y regresa una cadena de texto sin saltos
       de linea.
    '''
    try:
        with open(archivo,"r") as fh:
            texto = fh.read()
            renglones = texto.splitlines()
            texto_limpio = " ".join(renglones)
    except:
        texto_limpio = ""
    return texto_limpio
    
def contar_palabras(texto):
    '''Recibe una cadena de cualquier tamano y regresa un
       diccionario con el numero de palabras repetidas sin
       espacios vacios.
    '''
    Palabras = texto.split(" ")
    Diccionario = dict()
    for palabra in Palabras:
        p = palabra.strip(",.")
        if p in Diccionario:
            Diccionario[p] += 1
        else:
            Diccionario[p] = 1
    del(Diccionario[""])
    return Diccionario
    
def imprime_diccionario(dp,minimo):
    '''Recibe un diccionario de palabras y un minimo de repeticiones
       de palabras e imprime cada palabra con su numero de repeticiones.
    '''
    lista = [(k,v) for k,v in dp.items() if v>=minimo]
    lista_ordenada = sorted(lista, key= lambda x:x[1], reverse=True)
    for tupla in lista_ordenada:
        print(tupla[0],"= ",tupla[1])
    return
    
def leer_stopwords(archivo):
    '''Recibe una cadena con la ruta del archivo y regresa un
       set de palabras con las palabras que vienen en el archivo.
    '''
    try:
        with open(archivo,"r") as fh:
            lista = fh.readlines()
        lista_palabras = [palabra.strip("\n") for palabra in lista]
        return set(lista_palabras)
    except:
        return set()

def limpia_diccionario(dp,set_stop):
    '''Recibe un dicionario de palabras y un set de palabras para
       para remover las palabras del diccionario que estan en el
       set dado y regresa un nuevo diccionario sin las palabras que
       estan en el set.
    '''
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