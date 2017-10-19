#!/usr/bin/env python3
#coding=utf-8


#Antes de ejecutar esto hay que poner el archivo geckodriver en /usr/bin
#ejecutando sudo cp geckodriver /usr/bin

import sys
from time import sleep

from constantes import *
from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def sincronizar(usuario, clave, nombre_curso):
    
    driver=get_driver_acceso_comunicacion(usuario, clave)
    sleep(3)
    #Primero necesitamos guardar la base
    ventana_base=driver.current_window_handle
    print("Ventana base")
    print(ventana_base)
    print ("Cambiando de frame")
    
    try:
        print("Cambiando al inferior")
        driver.switch_to.frame("inferior")
        print("Cambiando al menu")
        driver.switch_to.frame("menu")
        print("Cambiando al menusup")
        driver.switch_to.frame("menuSup")
        print ("Se ha cambiado al frame")
        
        enlace_gestion_aulas_docente=driver.find_element_by_xpath("//div[@alt='Aula Virtual']")
        
        enlace_gestion_aulas_docente.click()
        
        
        enlace_gestion_aulas_docente=driver.find_element_by_xpath("/html/body/div/div[4]/div[3]")
        
        enlace_gestion_aulas_docente.click()
        
        #Volvemos a empezar
        print("Volviendo a la raiz")
        driver.switch_to.parent_frame() #Salimos de menuSup y volvemos a menu
        driver.switch_to.parent_frame() #Salimos de menu y volvemos a inferior
        
        print("Cambiando al principal")
        driver.switch_to.frame("principal")
        print("Cambiando al cuerpo")
        driver.switch_to.frame("cuerpo")
        sleep(2)
        
        print("Sincronizando " + nombre_curso)
        enlace_curso=driver.find_element_by_link_text(nombre_curso)
        
        enlace_curso.click()
        
        driver.switch_to.parent_frame() #Salimos de cuerpo y volvemos a principal, para esperar a que recargue el frame
        driver.switch_to.frame("cuerpo")
        
        enlace_alumnos=driver.find_element_by_xpath("//div[@id='menuItem1']")
        print(enlace_alumnos.get_attribute("outerHTML"))
        
        
        
        
        #Intentamos movernos al elemento activo
        hover=ActionChains(driver).move_to_element(enlace_alumnos)
        print("Hacemos mouseover sobre el enlace alumnos")
        hover.perform()
        print("Hacemos click en el enlace 'Alumnos'")
        enlace_alumnos.click()
        
        
        
        sleep(10)
        print("Salimos de dormir")
        driver.switch_to.parent_frame() #Salimos de cuerpo y volvemos a principal
        driver.switch_to.frame("botoneraTitulo")
        
        enlace_actualizar=driver.find_element_by_xpath("//a[@id='a_ACTUALIZAR']")
        enlace_volver=driver.find_element_by_xpath("//a[@id='a_VOLVER']")
        enlace_actualizar.click()
        print("Sincronizando alumnos, esto es lento, dejaremos 60 segundos para que se complete la accion")
        sleep(30)
        url=driver.execute_script("return top.inferior.principal.cuerpo.volver()")
        print(url)
        # enlace_volver=driver.find_element_by_xpath("//a[@id='a_VOLVER']")
        # print(enlace_volver.get_attribute("outerHTML"))
        # enlace_volver.click()
        sleep(5)
        print("Terminamos el curso "+nombre_curso)
        url=driver.execute_script("return top.document.location.replace('./Logout.jsp')")
        print(url)
        
        driver.quit()                    
    except Exception as e:
        print("Hubo una excepcion")
        print (e)
    
    sleep(3)
    print ("Fin de la sincronizacion")
    
    
if __name__ == '__main__':
    try:
        usuario=sys.argv[1]
        clave=sys.argv[2]
        vector_cursos=["LE-Aplicaciones web MIF-E", "LE-Leng. marcas y sist. gest. inf DAW-E"]
        for nombre_curso in vector_cursos:
            sincronizar(usuario, clave, nombre_curso)
    except Exception as e:
        print(e)
        