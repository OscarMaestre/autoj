#!/usr/bin/env python3


from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium
from selenium.webdriver.common.keys import Keys

def get_driver_acceso_jccm(usuario, clave):
    driver = webdriver.Firefox()
    driver.get("http://papas.jccm.es")
    
    
    enlace_servicio_autenticacion_jccm=driver.find_element_by_partial_link_text("Acceso con Servicio")
    enlace_servicio_autenticacion_jccm.click()
    
    cuadro_nuestro_login    =   driver.find_element_by_id("username")
    cuadro_nuestro_login.send_keys(usuario)
    
    cuadro_nuestro_password =   driver.find_element_by_id("password")
    cuadro_nuestro_password.send_keys(clave)
    
    boton_iniciar_acceso=driver.find_element_by_name("submit")
    boton_iniciar_acceso.click()
    
    return driver


def get_driver_acceso_secretaria_virtual(usuario, clave):
    
    driver=get_driver_acceso_jccm(usuario, clave)
    enlace_acceso_aula=driver.find_element_by_xpath("//a[@class='margenes_acceso'][2]")
    print (enlace_acceso_aula)
    enlace_acceso_aula.click()
    return driver
    
def get_driver_acceso_comunicacion(usuario, clave):
    driver=get_driver_acceso_jccm(usuario, clave)
    enlace_acceso_aula=driver.find_element_by_xpath("//a[@class='margenes_acceso'][1]")
    print (enlace_acceso_aula)
    enlace_acceso_aula.click()
    return driver
    
def get_driver_acceso_aula_virtual(usuario, clave):
    driver=get_driver_acceso_jccm(usuario, clave)
    enlace_acceso_aula=driver.find_element_by_xpath("//a[@class='margenes_acceso'][3]")
    print (enlace_acceso_aula)
    enlace_acceso_aula.click()
    return driver
    