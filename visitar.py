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

APLI_WEB_MIF    =   "https://aulafp1819.castillalamancha.es/course/view.php?id=447"
MARCAS_DAW      =   "https://aulafp1819.castillalamancha.es/course/view.php?id=458"

BANDEJA_ENTRADA =   "https://aulafp1819.castillalamancha.es/local/mail/view.php?t=inbox"
EDITAR_AJUSTES  =   "https://aulafp1819.castillalamancha.es/user/preferences.php"
CORREO_ENVIADO  =   "https://aulafp1819.castillalamancha.es/local/mail/view.php?t=sent"
CICLO_COMUN     =   "https://aulafp1819.castillalamancha.es/course/view.php?id=255"
CICLO_DAW       =   "https://aulafp1819.castillalamancha.es/course/view.php?id=270"
CICLO_SMIR      =   "https://aulafp1819.castillalamancha.es/mod/forum/view.php?f=4812"
FORO_COMUN_CICLO=   "https://aulafp1819.castillalamancha.es/mod/forum/view.php?f=2423"
TEMA_1=[
    "https://aulafp1819.castillalamancha.es/mod/scorm/view.php?id=51709",  #Material
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51716",     #Enunciado tarea 1
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51712",   #Mapa conceptual
    "https://aulafp1819.castillalamancha.es/mod/forum/view.php?id=51711",      #Foro
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51705",   #Orientaciones alumnado
    "https://aulafp1819.castillalamancha.es/mod/forum/discuss.php?d=2693",
    "https://aulafp1819.castillalamancha.es/mod/forum/discuss.php?d=2390",
    "https://aulafp1819.castillalamancha.es/mod/forum/discuss.php?d=2450",
    "https://aulafp1819.castillalamancha.es/mod/forum/discuss.php?d=1694",
    "https://aulafp1819.castillalamancha.es/mod/forum/discuss.php?d=2159",
    "https://aulafp1819.castillalamancha.es/mod/page/view.php?id=27538",    #Convalidaciones
    "https://aulafp1819.castillalamancha.es/mod/forum/subscribers.php?id=2423"  #Mostrar ajustes
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51716&action=grading", #Tareas
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51716&page=1", #Tareas 2
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51716&page=2", #Tareas 3
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51716&page=3", #Tareas 4
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51716&page=5" #Tareas 2
    
    
]
TEMA_2=[
    "https://aulafp1819.castillalamancha.es/mod/forum/view.php?id=51724",       #Foro
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51725",    #Mapa conceptual
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51718",    #Orientaciones
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51729",      #Tarea
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51729&action=grading", #Tarea 2
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51729&page=5", #Pagina 5 tareas
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51729&page=4", #Pagina 4 tareas
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51729&page=3", #Pagina 3 tareas
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?action=grading&id=51729&page=2", #Pagina 5 tareas
]

TEMA_3=[
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=49345",
    "https://aulafp1819.castillalamancha.es/mod/forum/view.php?id=49360",
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=49362",
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=49369"
    
]

TEMA_4=[
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/view.php?id=128485",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/resource/view.php?id=128486",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/quiz/view.php?id=128488",
    
]

TEMA_4_WEB=[
    "https://aulafp1819.castillalamancha.es/mod/scorm/view.php?id=49383",
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=49402",
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=49403",
    "https://aulafp1819.castillalamancha.es/mod/quiz/view.php?id=49405"
    
]

TEMA_5_WEB=[
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/assign/view.php?id=128457",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/resource/view.php?id=128453",
    "https://aulavirtual.castillalamancha.es/Curso_1718/mod/forum/view.php?id=128452"
            ]

TEMA_6_DAW=[
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51781",
    "https://aulafp1819.castillalamancha.es/mod/quiz/view.php?id=51779",
    "https://aulafp1819.castillalamancha.es/mod/forum/view.php?id=51776",
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51770",
    "https://aulafp1819.castillalamancha.es/mod/scorm/view.php?id=51774",
    
]

TEMA_7_DAW=[
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51783",
    "https://aulafp1819.castillalamancha.es/mod/scorm/view.php?id=51787",
    "https://aulafp1819.castillalamancha.es/mod/forum/view.php?id=51789",
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51794",
    "https://aulafp1819.castillalamancha.es/mod/resource/view.php?id=51790",
    
]
ENLACES_TAREAS=[
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=49304", #Apli web T1
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=49342", #Apli web T2
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=49369", #Apli web T3
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=49410", #Apli web T4
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=49447", #Apli web T5
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51716", #Marcas T1
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51729", #Marcas T2
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51742", #Marcas T3
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51755", #Marcas T4
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51768", #Marcas T5
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51781", #Marcas T6
    "https://aulafp1819.castillalamancha.es/mod/assign/view.php?id=51794", #Marcas T7
    
]
TEMAS=[TEMA_1, TEMA_2, TEMA_3, FORO_COMUN_CICLO, ENLACES_TAREAS, TEMA_4_WEB, TEMA_6_DAW, TEMA_7_DAW]
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
                selector_personal="//*[@id='action-menu-toggle-0']"
                #selector_personal="//*[@id='yui_3_17_2_1_1548758095547_345']"
                enlace_personal=driver.find_element_by_xpath(selector_personal)
                enlace_personal.click()
                sleep(4)
                selector_enlace_salida="//span[@class='menu-action-text' and @id='actionmenuaction-6']"
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
        