#!/usr/bin/env python3


from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def get_driver_acceso_jccm(usuario, clave):    
    driver = webdriver.Firefox()
    
    
    driver.get("http://papas.jccm.es")
    
    
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
    css_comunicacion="j_idt27:0:j_idt29"
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
    selector_xpath_aula_virtual_1="//a[@class='margenes_acceso'][12]"
    #selector_xpath_aula_virtual_2="//input[@type='hidden']/following-sibling::a"
    selector_xpath_aula_virtual_2='//*[@id="j_idt27:3:j_idt29:j_idt32"]'
    driver=get_driver_acceso_jccm(usuario, clave)
    sleep(2)
    try:
        enlace_acceso_aula=driver.find_element_by_xpath(selector_xpath_aula_virtual_2)
    except NoSuchElementException as e:
        print("Usando el enlace nuevo")
        
        enlace_acceso_aula=driver.find_element_by_xpath(selector_xpath_aula_virtual_2)
    except Exception as e:
        print("Fallo general")
    #print (enlace_acceso_aula)
    enlace_acceso_aula.click()
    return driver
    
    
def abrir_pestania_en_driver(driver, enlace, bajar_abajo=False):
    driver.execute_script('''window.open("{0}","_blank");'''.format(enlace))
    if bajar_abajo:
        pass