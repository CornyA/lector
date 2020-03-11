#!/usr/bin/python3
import os
import clean
import tfidf
import lector
import argparse

def carga_textos(folder,termina):
    try:
        lista_textos = []
        lista_archivos = os.listdir(folder)
        lista_txt = [archivo for archivo in lista_archivos if archivo.endswith(termina)]
        for archivo in lista_txt:
            texto = lector.leer_archivo(os.path.join(folder,archivo))
            texto_limpio = clean.clean_text(texto)
            lista_textos.append(texto_limpio)
            
    except IOError as e:
        print(e)
        lista_textos = []
    return lista_textos

def obten_set_palabras(lista_textos):
    try:
        set_palabras_unicas = set()
        for texto in lista_textos:
            set_palabras = texto.split(" ")
            set_palabras_unicas = set_palabras_unicas.union(set_palabras)
    except:
        print("error al obtener palabras unicas")
        set_palabras_unicas= set()
    return set_palabras_unicas
    
def obten_lista_palabras(textos):
    lista_palabras = []
    for texto in textos:
        palabras = texto.split(" ")
        #print(len(palabras))
        lista_palabras.append(palabras)
    #print(len(lista_palabras))
    return lista_palabras
    
def obten_diccionarios_vacios(lista_palabras, palabras_unicas):
    lista_dict = []
    for lista in lista_palabras:
        diccionario = dict.fromkeys(palabras_unicas,0)
        lista_dict.append(diccionario)
    return lista_dict
    
def llena_diccionarios(lista_diccionarios,lista_palabras_textos):
    zipped = list(zip(lista_diccionarios,lista_palabras_textos))
    for z in zipped:
        diccionario = z[0]
        lista_palabras = z[1]
        for palabra in lista_palabras:
            diccionario[palabra] += 1
            
def obten_tf(lista_diccionarios,lista_palabras_textos):
    zipped = list(zip(lista_diccionarios,lista_palabras_textos))
    lista = []
    for z in zipped:
        diccionario = z[0]
        lista_palabras = z[1]
        tf = tfidf.computarTF(diccionario,lista_palabras)
        lista.append(tf)
    return lista
    
def obten_tfidf(lista_tf,idfs):
    lista = []
    for tf in lista_tf:
        tf_idf = tfidf.computarTFIDF(tf,idfs)
        lista.append(tf_idf)
    return lista
    
def despliega_lista(lista,n):
    for elemento in lista:
        despliega(elemento,n)
        
def despliega(tfidf,n):
    print("----------")
    lista_ordenada = sorted(tfidf.items(), key=lambda kv:(kv[1],kv[0]), reverse=True)
    for elemento in lista_ordenada[0:n]:
        print(elemento[0],":",elemento[1])
        

def main(folder,termina,numero,output):
    textos = carga_textos(folder,termina)
    set_palabras_unicas = obten_set_palabras(textos)
    print("len textos:",len(textos))
    print("len set palabras:",len(set_palabras_unicas))
    lista_palabras_textos = obten_lista_palabras(textos)
    print("len lista palabras:",len(lista_palabras_textos))
    lista_diccionarios = obten_diccionarios_vacios(lista_palabras_textos,set_palabras_unicas)
    print("len lista diccionarios:",len(lista_diccionarios))
    llena_diccionarios(lista_diccionarios,lista_palabras_textos)
    lista_tf = obten_tf(lista_diccionarios, lista_palabras_textos)
    idfs = tfidf.computarIDF(lista_diccionarios)
    lista_tfidf = obten_tfidf(lista_tf,idfs)
    despliega_lista(lista_tfidf,numero)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--folder", dest = "folder", help="Ruta del folder", required=True)
    parser.add_argument("-t","--termina", dest = "termina", help ="Terminacion del archivo(.txt,.py,etc)", required = False, default="txt")
    parser.add_argument("-n","--numero", dest = "numero", help="Numero de palabras a extraer", required=False, default=10, type=int)
    parser.add_argument("-o","--output", dest="output", help="Nombre del fichero a escribir", required=False)
    args = parser.parse_args()
    folder = args.folder
    termina = args.termina
    numero = args.numero
    output = args.output
    main(folder,termina,numero,output)
