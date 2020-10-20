#!/usr/bin/env python3
#coding=utf-8


#Antes de ejecutar esto hay que poner el archivo geckodriver en /usr/bin
#ejecutando sudo cp geckodriver /usr/bin

import sys
from time import sleep, localtime, time, asctime
import datetime
from progress.bar import Bar

from constantes import *
from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium
from random import randint

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


MARCAS_DAW      =   "https://aulasfp2021.castillalamancha.es/course/view.php?id=592"

BANDEJA_ENTRADA =   "https://aulasfp2021.castillalamancha.es/local/mail/view.php?t=inbox"
EDITAR_AJUSTES  =   "https://aulasfp2021.castillalamancha.es/user/preferences.php"
CORREO_ENVIADO  =   "https://aulasfp2021.castillalamancha.es/local/mail/view.php?t=sent"
CICLO_COMUN     =   "https://aulasfp2021.castillalamancha.es/course/view.php?id=789"
CICLO_DAW       =   "https://aulasfp2021.castillalamancha.es/course/view.php?id=789"
CICLO_SMIR      =   ""
FORO_COMUN_CICLO=   "https://aulasfp2021.castillalamancha.es/mod/forum/view.php?id=94073"

TEMA_1_DAW=[
    "https://aulasfp2021.castillalamancha.es/mod/forum/view.php?id=67297",
    "https://aulasfp2021.castillalamancha.es/mod/resource/view.php?id=67311",
    "https://aulasfp2021.castillalamancha.es/mod/resource/view.php?id=67299",
    "https://aulasfp2021.castillalamancha.es/mod/resource/view.php?id=67285",
]
TEMA_2_DAW=[
    "",
    "",
    "",
    "",
    ""
    
]
TEMAS=[TEMA_1_DAW]
NO_TEMAS=[BANDEJA_ENTRADA, EDITAR_AJUSTES, CORREO_ENVIADO, CICLO_COMUN, CICLO_DAW]

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

    

def randboolean():
    valor_azar=randint(0, 1)
    if valor_azar==0:
        return True
    return False
    

def hora_actual_mayor_que_pasada(horapasada, minutospasados):
    hora_actual = datetime.datetime.now()
    h_auxiliar =datetime.datetime.now()
    h_auxiliar=h_auxiliar.replace(hour=int(horapasada), minute=int(minutospasados))
    print("Son las:         "+str(hora_actual))
    print("Hay que apagar a:"+str(h_auxiliar))
    
    
    if hora_actual>h_auxiliar:
        print("Tiempo consumido!")
        return True
    else:
        print("Aun no apagamos")
        return False

def visitar(usuario, clave, horapasada=None, minutospasados=None):
    TEMA_ACTUAL=1
    if horapasada!=None:
        print("Hay que apagar a las ")
        print(horapasada, minutospasados)
    navegador=get_driver_acceso_aula_virtual(usuario, clave)
    while True:
        if (horapasada!=None):
            salir=hora_actual_mayor_que_pasada(horapasada, minutospasados)
            if salir:
                print ("Hora de salir")
                sleep(12)
                navegador.visitar_pagina(MARCAS_DAW)
                sleep(5)
                #Abrimos el boton
		
                selector_personal="/html/body/div[2]/nav/ul[2]/li[3]/div/div/div/div/div/a/span/span[1]"
                
                navegador.hacer_click_por_ruta_xpath(selector_personal)
                sleep(4)
		
                
                selector_enlace_salida="/html/body/div[2]/nav/ul[2]/li[3]/div/div/div/div/div/div/a[6]"
                
                navegador.hacer_click_por_ruta_xpath(selector_enlace_salida)
                
                sleep(10)
                return
        navegador.esperar_tiempo_azar(27, 38)
        
        if randboolean()==True:
            enlace_a_visitar=elegir_enlace_tema(1)
        else:
            enlace_a_visitar=elegir_elemento_al_azar(NO_TEMAS)
        print("Visitando "+enlace_a_visitar)
        navegador.visitar_pagina(enlace_a_visitar)
    #Fin del while
        
    
    
    
if __name__ == '__main__':
    usuario=sys.argv[1]
    clave=sys.argv[2]
    horapasada=sys.argv[3]
    minutospasados=sys.argv[4]
    
    
    visitar(usuario, clave, horapasada, minutospasados)
    # try:
    #     usuario=sys.argv[1]
    #     clave=sys.argv[2]
    #     visitar(usuario, clave)
    # except Exception as e:
    #     print(e)
        
