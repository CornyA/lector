#!/usr/bin/python3
import lector
import argparse

'''
def porcentaje_palabras_stop(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    lista_palab = texto.split(" ")
    tam_texto = len(lista_palab)
    tam_dip = contar_repeticiones(diccionario)
    stop_words = lector.leer_stopwords("/home/cassiopea/josenoriega/spanish_stopwords.txt")
    tam_stop = len(stop_words)
    porc_stop = (tam_stop*100)/tam_texto
    porc_clave = (tam_dip*100)/tam_texto
    print("Palabras en el texto: ",tam_texto,"| Porcentaje = 100%")
    print("Palabras stop:        ",tam_stop,"| Porcentaje = ",porc_stop, "%")
    print("Diccionario(clave):   ",tam_dip,"| Porcentaje = ",porc_clave, "%")
'''    
 
def porcentaje_palabras(archivo,set_stop):
    texto = lector.leer_archivo(archivo)
    lista_palabras = texto.split(" ")
    tam_texto = len(lista_palabras) #Numero de palabras
    
    stopwords = lector.leer_stopwords(set_stop)
    dpc = dict()
    dps = dict()
    
    for palabra in lista_palabras:
        p = palabra.lower().strip(".,")
        if p in stopwords:
            if p in dps:
                dps[p] += 1
            else:
                dps[p] = 1
        else:
            if p in dpc:
                dpc[p] += 1
            else:
                dpc[p] = 1
                
    sumapc = contar_repeticiones(dpc)
    sumaps = contar_repeticiones(dps)
    porc_stop = (sumaps*100)/tam_texto
    porc_clave = (sumapc*100)/tam_texto
    print("Palabras en el texto: ",tam_texto,"| Porcentaje = 100%")
    print("Palabras clave:       ",sumapc,"| Porcentaje = ",porc_clave, "%")
    print("Palabras stop:        ",sumaps,"| Porcentaje = ",porc_stop, "%")
    pcu = contar_palabras_unicas(dpc)
    pcs = contar_palabras_unicas(dps)
    total_pu = pcu + pcs
    print("---------------")
    print("Total palabras unicas:", total_pu)
    print("Palabras clave unicas:", pcu, pcu/total_pu)
    print("Palabras stop  unicas:", pcs, pcs/total_pu)
    
def contar_palabras_unicas(dp):
    total = len(set(dp))
    return total
    
    
def contar_repeticiones(diccionario):
    suma = 0
    for k,v in diccionario.items():
        suma += v
    return suma
    
def contar(texto, stopwords):
    lista_palabras = texto.split(" ")
    total_palabras = len(lista_palabras)
    dpc = dict() #dicc.palabras clave
    dps = dict() #dicc.palabras stop

    for palabra in lista_palabras:
        p = palabra.lower().strip(".,")
        if p in stopwords:
           if p in dps:
              dps[p] += 1 #sumamos 1
           else: 
              dps[p] = 1  #creamos
        else:
           if p in dpc:
              dpc[p] += 1 #sumamos
           else:
              dpc[p] = 1  #creamos
    sumapc = contar_repeticiones(dpc)
    sumaps = contar_repeticiones(dps)
    print("Total de palabras:",total_palabras)
    print("Palabras clave:",sumapc, sumapc/total_palabras)
    print("Palabras stop:",sumaps, sumaps/total_palabras)
    pcu = contar_palabras_unicas(dpc)
    pcs = contar_palabras_unicas(dps)
    total_pu = pcu + pcs
    print("---------------")
    print("Total palabras unicas:", total_pu)
    print("Palabras clave unicas:", pcu, pcu/total_pu)
    print("Palabras stop  unicas:", pcs, pcs/total_pu)
    
def contar_palabras_unicas(dp):
	  total = len(set(dp))
	  return total

def palabras_unicas(archivo):
    texto = lector.leer_archivo(archivo)
    diccionario = lector.contar_palabras(texto)
    set_stopw = lector.leer_stopwords("/home/cassiopea/josenoriega/spanish_stopwords.txt")
    lista_palabras = texto.split(" ")
    set_clave = set()
    set_stop = set()
    for palabra in lista_palabras:
        p = palabra.lower().strip(",.")
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

    

def main(archivo,arc_sw):
    print("----------------Porcentaje de palabras-------------")
    #porcentaje = porcentaje_palabras_stop(archivo)
    porcentaje_palabras(archivo,arc_sw)
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
