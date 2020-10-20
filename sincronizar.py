#!/usr/bin/env python3
#coding=utf-8


#Antes de ejecutar esto hay que poner el archivo geckodriver en /usr/bin
#ejecutando sudo cp geckodriver /usr/bin

import sys
import traceback

from time import sleep

from constantes import *
from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def hacer_mouse_over_sobre_elemento_xpath(driver, ruta_xpath):
    elemento=driver.find_element_by_xpath(ruta_xpath)
    hover=ActionChains(driver).move_to_element(elemento)
    print("Haciendo mouse over sobre:"+ruta_xpath)
    hover.perform()
    print("Ejecutado mouse over sobre:"+ruta_xpath)
    sleep(2)

def hacer_click_sobre_elemento_xpath(driver, ruta_xpath):
    elemento=driver.find_element_by_xpath(ruta_xpath)
    print("A punto de hacer click en :"+ruta_xpath)
    accion=ActionChains(driver)
    accion.click(on_element=elemento)
    accion.perform();
    print("Hemos hecho click en :"+ruta_xpath)
    sleep(2)
    
    
    
    
def sincronizar(usuario, clave, nombre_curso):
    
    driver=get_driver_acceso_comunicacion(usuario, clave)
    sleep(3)
    #Primero necesitamos guardar la base
    ventana_base=driver.current_window_handle
    print("Ventana base")
    print(ventana_base)
    print ("Cambiando de frame")
    
    
    print("Cambiando al inferior")
    driver.switch_to.frame("inferior")
    print("Cambiando al menu")
    driver.switch_to.frame("menu")
    print("Cambiando al menu lateral")
    driver.switch_to.frame("menuLateral")
    print ("Se ha cambiado al frame")
    
    enlace_centro=driver.find_element_by_xpath("//div[@alt='Entorno de aprendizaje']")
    print("Click en gestión de participantes...")
    enlace_centro.click()

    enlace_gestion_aulas_docente=driver.find_element_by_xpath("//div[@alt='Gestión de participantes ']")
    
    enlace_gestion_aulas_docente.click()
    print ("Hemos hecho click en gestión de participantes y esperamos a que cargue")
    sleep(10)

    driver.switch_to.parent_frame() #Salimos de menuLateral y volvemos a menu
    #driver.switch_to.frame("principal")
    driver.switch_to.parent_frame() #Salimos de menu y volvemos al padre
    driver.switch_to.frame("principal") #Entramos en principal, que es hermano de menu
    driver.switch_to.frame("cuerpo") #Entramos en cuerpo, que está dentro de principal

    xpath_acceso_sincronizacion_marcas="/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/a"
    enlace_gestion_aulas_docente=driver.find_element_by_xpath(xpath_acceso_sincronizacion_marcas)
    
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
    print("Hacemos click en el curso")
    enlace_curso.click()
    
    driver.switch_to.parent_frame() #Salimos de cuerpo y volvemos a principal, para esperar a que recargue el frame
    driver.switch_to.frame("cuerpo")
    
    hacer_mouse_over_sobre_elemento_xpath(driver, "//div[@id='menuFg0']")
    
    xpath_cuadro_alumnos_para_sincronizar="//div[@id='menuItemHilite1']"
    hacer_mouse_over_sobre_elemento_xpath(driver, xpath_cuadro_alumnos_para_sincronizar)
    hacer_click_sobre_elemento_xpath(driver, xpath_cuadro_alumnos_para_sincronizar)
    

    
    
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

    
    sleep(3)
    print ("Fin de la sincronizacion")
    
    
if __name__ == '__main__':
    try:
        usuario=sys.argv[1]
        clave=sys.argv[2]
        marcas="LE-Leng. marcas y sist. gest. inf DAW E"
        vector_cursos=[marcas]
        for nombre_curso in vector_cursos:
            sincronizar(usuario, clave, nombre_curso)
    except Exception as e:
        print(e)
        