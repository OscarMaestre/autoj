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


MARCAS_DAW      =   "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=54994"

BANDEJA_ENTRADA =   "https://aulafp1920.castillalamancha.es/message/index.php"
EDITAR_AJUSTES  =   "https://aulafp1920.castillalamancha.es/user/preferences.php"
CORREO_ENVIADO  =   "https://aulafp1920.castillalamancha.es/local/mail/view.php?t=inbox"
CICLO_COMUN     =   "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=28705"
CICLO_DAW       =   "https://aulafp1920.castillalamancha.es/mod/page/view.php?id=28718"
CICLO_SMIR      =   "https://aulafp1920.castillalamancha.es/mod/page/view.php?id=28715"
FORO_COMUN_CICLO=   "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=54994"

TEMA_1_DAW=[
    "https://aulafp1920.castillalamancha.es/mod/resource/view.php?id=55004",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55010",
    "https://aulafp1920.castillalamancha.es/mod/quiz/view.php?id=55013",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55015",
]
TEMA_2_DAW=[
    "https://aulafp1920.castillalamancha.es/mod/resource/view.php?id=55017",
    "https://aulafp1920.castillalamancha.es/mod/resource/view.php?id=55018",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55023",
    "https://aulafp1920.castillalamancha.es/mod/quiz/view.php?id=55026",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55028"
    
]
TEMAS=[TEMA_1_DAW, TEMA_2_DAW]
NO_TEMAS=[BANDEJA_ENTRADA, EDITAR_AJUSTES, CORREO_ENVIADO, CICLO_COMUN, CICLO_DAW, CICLO_SMIR]

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
    driver=get_driver_acceso_aula_virtual(usuario, clave)
    while True:
        if (horapasada!=None):
            salir=hora_actual_mayor_que_pasada(horapasada, minutospasados)
            if salir:
                print ("Hora de salir")
                sleep(12)
                #Abrimos el boton
		
                selector_personal="//*[@id='dropdown-6']"
                #selector_personal="//*[@id='yui_3_17_2_1_1548758095547_345']"
                enlace_personal=driver.find_element_by_xpath(selector_personal)
                enlace_personal.click()
                sleep(4)
		
                selector_enlace_salida="/html/body/div[4]/nav/ul[2]/li[2]/div/div/div/div/div/div/a[6]"
                enlace_salida=driver.find_element_by_xpath(selector_enlace_salida)

                enlace_salida.click()
                sleep(10)
                return
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
    horapasada=sys.argv[3]
    minutospasados=sys.argv[4]
    
    
    visitar(usuario, clave, horapasada, minutospasados)
    # try:
    #     usuario=sys.argv[1]
    #     clave=sys.argv[2]
    #     visitar(usuario, clave)
    # except Exception as e:
    #     print(e)
        
