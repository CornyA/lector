#!/usr/bin/python3
''' TF-IDF: Term Frequency - Inverse Document Frecuency '''
import math

def computarTF(diccionario,lista_palabras):
    ''' Calcula la Frecuencia del Termino / Term Frequency 
        uso: dune_tf = (diccionario_dune/ lista_dune)
    '''
    tf = dict()
    total_palabras = len(lista_palabras)
    for k,v in diccionario.items():
        tf[k] = v / float(total_palabras)
    return tf


def computarIDF(documentos):
    ''' calcula la Frecuencia Inversa del documento
    uso: idfs = computarIDF([diccionario_dune, diccionario_luna])
    '''
    N = len(documentos)

    idfDict = dict.fromkeys(documentos[0].keys(), 0)
    for documento in documentos:
        for key, val in documento.items():
            if val > 0:
                idfDict[key] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict


def computarTFIDF(tf, idfs):
    ''' calcula Term Frequency-Inverse Document Frecuency
        para todos los documentos
        uso:tfidf_dune = computarTFIDF(dune_tf, idfs)
    ''' 
    tfidf = dict()
    for key, val in tf.items():
        tfidf[key] = val * idfs[key]
    return tfidf


