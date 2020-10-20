#!/usr/bin/env python3


from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
from progress.bar import Bar

from random import randint


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navegador(object):
    def __init__(self, pagina):
        self.pagina=pagina
        self.driver = webdriver.Firefox()
        self.driver.get(self.pagina)

    def visitar_pagina(self, pagina):
        self.pagina=pagina
        self.driver.get(self.pagina)

    def get_elemento_por_id(self, id):
        elemento=self.driver.find_element_by_id(id)
        return elemento

    def get_elemento_xpath(self, ruta_xpath):
        elemento=self.driver.find_element_by_xpath(ruta_xpath)
        return elemento
    
    def get_elemento_por_texto_enlace(self, texto_enlace):
        elemento=self.driver.find_element_by_link_text(texto_enlace)
        return elemento

    def hacer_mouse_over_por_texto_enlace(self, texto_enlace):
        elemento=self.get_elemento_por_texto_enlace(texto_enlace)
        accion=ActionChains(self.driver).move_to_element(elemento)
        accion.perform()

    def hacer_click_por_texto_enlace(self, texto_enlace):
        elemento=self.get_elemento_por_texto_enlace(texto_enlace)
        accion=ActionChains(self.driver)
        accion.click(on_element=elemento)
        accion.perform()

    def hacer_mouse_over_por_ruta_xpath(self, ruta_xpath):
        elemento=self.get_elemento_xpath(ruta_xpath)
        accion=ActionChains(self.driver).move_to_element(elemento)
        accion.perform()

    def hacer_click_por_ruta_xpath(self, ruta_xpath):
        elemento=self.get_elemento_xpath(ruta_xpath)
        accion=ActionChains(self.driver)
        accion.click(on_element=elemento)
        accion.perform()


    def escribir_texto_en_elemento_por_id(self, id, texto):
        elemento=self.get_elemento_por_id(id)
        elemento.send_keys(texto)

    def esperar_tiempo_azar(self, segundos_como_minimo, segundos_como_maximo):
        segundos=randint(segundos_como_minimo, segundos_como_maximo)
        mensaje="Esperando {0} segundos".format(segundos)
        barra=Bar(mensaje, max=segundos)
        for i in range(0, segundos):
            sleep(1)
            barra.next()
        print()

    def abrir_pestania_en_driver(self, enlace):
        self.driver.execute_script('''window.open("{0}","_blank");'''.format(enlace))
    


def get_driver_acceso_jccm(usuario, clave):    
    driver = webdriver.Firefox()
    
    driver.get("https://aulasfp2021.castillalamancha.es/")
    
    
    #YA no es necesario estas dos lineas
    #enlace_servicio_autenticacion_jccm=driver.find_element_by_partial_link_text("Acceso con Servicio")
    #enlace_servicio_autenticacion_jccm.click()
    
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
    print("Esperando carga...")
    sleep(10)
    css_comunicacion="j_idt25:0:j_idt27:j_idt30"
    
    #css_comunicacion="j_idt25:0:j_idt29"
    #enlace_acceso_aula=driver.find_element_by_xpath("//a[@class='margenes_acceso'][1]")
    enlace_acceso_aula=driver.find_element_by_id(css_comunicacion)
    enlace_acceso_aula.click()
    print("Esperando carga comunicacion...")
    sleep(10)
    print (enlace_acceso_aula)
    
    return driver
    
    
def probar_algunos_selectores(driver):
    selectores=["//img", "//img[@class='iconoAplicacion']", "/html", "//img[@class='iconoAplicacion'][3]",
                "//input[@name='j_idt27:2:j_idt29']", "//input[@type='hidden']",
                "//input[@type='hidden']/following-sibling::a"]
    for selector in selectores:
        try:
            elemento=driver.find_element_by_xpath(selector)
            print("HTML de "+selector+":"+elemento.text)
        except NoSuchElementException as e:
            print("Fallo en selector--->"+selector)
        except Exception as e:
            print("Algo fallo con :"+selector)
            
def get_driver_acceso_aula_virtual(usuario, clave):
    index="https://aulasfp2021.castillalamancha.es/"
    driver=Navegador(index)
    driver.hacer_click_por_texto_enlace("Acceder")
    driver.esperar_tiempo_azar(4,10)
    print("Usando usuario {0}".format(usuario))
    driver.escribir_texto_en_elemento_por_id("userNameLDAP", usuario)
    print("Usando clave {0}".format(clave))
    driver.escribir_texto_en_elemento_por_id("passwordLDAP", clave)

    xpath_boton_login="//input[@tabindex=8]"
    driver.hacer_click_por_ruta_xpath(xpath_boton_login)
    driver.esperar_tiempo_azar(4,10)
    return driver
    
    
def abrir_pestania_en_driver(driver, enlace, bajar_abajo=False):
    driver.execute_script('''window.open("{0}","_blank");'''.format(enlace))
    if bajar_abajo:
        pass
