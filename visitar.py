#!/usr/bin/env python3
#coding=utf-8


#Antes de ejecutar esto hay que poner el archivo geckodriver en /usr/bin
#ejecutando sudo cp geckodriver /usr/bin

import sys
from time import sleep
from progress.bar import Bar

from constantes import *
from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium
from random import randint

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

APLI_WEB_MIF    =   "https://aulavirtual.castillalamancha.es/Curso_1718/course/view.php?id=376"
MARCAS_DAW      =   "https://aulavirtual.castillalamancha.es/Curso_1718/course/view.php?id=3048"

BANDEJA_ENTRADA =   "https://aulavirtual.castillalamancha.es/Curso_1718/local/mail/view.php?t=inbox"
EDITAR_AJUSTES  =   "https://aulavirtual.castillalamancha.es/Curso_1718/course/edit.php?id=3047"
CORREO_ENVIADO  =   "https://aulavirtual.castillalamancha.es/Curso_1718/local/mail/view.php?t=sent"
CICLO_COMUN     =   "https://aulavirtual.castillalamancha.es/Curso_1718/course/view.php?id=372"
CICLO_DAW       =   "https://aulavirtual.castillalamancha.es/Curso_1718/course/view.php?id=376"
CICLO_SMIR      =   "https://aulavirtual.castillalamancha.es/Curso_1718/course/view.php?id=372"
FORO_COMUN_CICLO=   "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/view.php?id=51345"
TEMA_1=[
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/scorm/view.php?id=128364",  #Material
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/assign/view.php?id=128371",     #Enunciado tarea 1
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/resource/view.php?id=128367",   #Mapa conceptual
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/discuss.php?d=2701",      #Foro
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/discuss.php?d=2539",      #Foro
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/resource/view.php?id=128360",   #Orientaciones alumnado
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/discuss.php?d=3603",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/discuss.php?d=3505",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/glossary/view.php?id=128398",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/discuss.php?d=3504"
    
    
]
TEMA_2=[
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/post.php?reply=12878#mformforum",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/resource/view.php?id=128380",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/quiz/view.php?id=128382",
]

TEMAS=[TEMA_1, TEMA_2]

NO_TEMAS=[BANDEJA_ENTRADA, EDITAR_AJUSTES, CORREO_ENVIADO, CICLO_COMUN, CICLO_DAW, CICLO_SMIR, FORO_COMUN_CICLO]

VISITAR_TEMA=0
VISITAR_OTROS=1
OPCIONES=[VISITAR_TEMA, VISITAR_OTROS]

def elegir_elemento_al_azar(vector):
    elemento=randint(0, len(vector)-1)
    return vector[elemento]

def elegir_enlace_tema(num_tema):
    #Hay que restar 1 porque los temas van de 1 en adelante
    #y los vectores de 0 en adelante
    vector_enlaces=TEMAS[num_tema-1]
    enlace=elegir_elemento_al_azar(vector_enlaces)
    return enlace

def esperar_tiempo_azar():
    segundos=randint(27, 509)
    mensaje="Esperando {0} segundos".format(segundos)
    barra=Bar(mensaje, max=segundos)
    for i in range(0, segundos):
        sleep(1)
        barra.next()
    print()
    
    

def randboolean():
    valor_azar=randint(0, 1)
    if valor_azar==0:
        return True
    return False
    


def visitar(usuario, clave):
    TEMA_ACTUAL=1
    driver=get_driver_acceso_aula_virtual(usuario, clave)
    while True:
        esperar_tiempo_azar()
        if randboolean()==True:
            enlace_a_visitar=elegir_enlace_tema(1)
        else:
            enlace_a_visitar=elegir_elemento_al_azar(NO_TEMAS)
        print("Visitando "+enlace_a_visitar)
        driver.get(enlace_a_visitar)
    #Fin del while
        
    
    
    
if __name__ == '__main__':
    usuario=sys.argv[1]
    clave=sys.argv[2]
    visitar(usuario, clave)
    # try:
    #     usuario=sys.argv[1]
    #     clave=sys.argv[2]
    #     visitar(usuario, clave)
    # except Exception as e:
    #     print(e)
        