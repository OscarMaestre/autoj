#!/usr/bin/env python3



#Antes de ejecutar esto hay que poner el archivo geckodriver en /usr/bin
#ejecutando sudo cp geckodriver /usr/bin

import sys

from constantes import *
from selenium import webdriver #Si esto falla ejecutar sudo pip install selenium
from selenium.webdriver.common.keys import Keys

def comprobar_si_inician_sesion_en_la_plataforma(usuario, clave):
    driver=get_driver_acceso_aula_virtual(usuario, clave)
    
    
if __name__ == '__main__':
    try:
        usuario=sys.argv[1]
        clave=sys.argv[2]
        
        comprobar_si_inician_sesion_en_la_plataforma(usuario, clave)
    except Exception as e:
        print(e)
        