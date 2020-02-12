#!/usr/bin/python3
import lector
import argparse

def porcentaje_palabras_stop(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    tam_texto = len(texto)
    tam_dip = contar_repeticiones(diccionario)
    tam_stop = tam_texto - tam_dip
    porc_stop = (tam_stop*100)/tam_texto
    porc_clave = 100-porc_stop
    print("Palabras en el texto: ",tam_texto,"| Porcentaje = 100%")
    print("Palabras stop:        ",tam_stop,"| Porcentaje = ",porc_stop, "%")
    print("Diccionario(clave):   ",tam_dip,"| Porcentaje = ",porc_clave, "%")
    
    
def contar_repeticiones(diccionario):
    suma = 0
    for k,v in diccionario.items():
        suma += v
    return suma
    
def palabras_unicas(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    set_stopw = lector.leer_stopwords("/home/cassiopea/josenoriega/spanish_stopwords.txt")
    lista_palabras = texto.split(" ")
    set_clave = set()
    set_stop = set()
    for palabra in lista_palabras:
        p = palabra.strip(",.")
        if p in set_stopw:
            set_stop.add(p)
        else:
            set_clave.add(p)
    #Numero de palabras unicas
    unic_clave = len(set_clave)
    unic_stop = len(set_stop)
    total_unic = unic_clave + unic_stop
    #Porcentaje de palabras unicas
    porc_clave = (unic_clave / total_unic)*100
    porc_stop = (unic_stop / total_unic)*100
    print("Palabras unicas: ", total_unic,"| Porcentaje = 100% ")
    print("Palabras clave:  ",unic_clave,"| Porcentaje = ", porc_clave, "%")
    print("Palabras stop:   ",unic_stop,"| Porcentaje = ", porc_stop, "%")

    

def main(archivo):
    print("----------------Porcentaje de palabras-------------")
    porcentaje = porcentaje_palabras_stop(archivo)
    print("---------------Porcentaje de palabras unicas-------")
    palabras_unicas(archivo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--archivo", dest="archivo", help="Directorio del archivo", required=True)
    parser.add_argument("-s", "--stopwords", dest= "stopwords", help="Directorio de StopWords", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    sw = args.stopwords
    main(archivo)
