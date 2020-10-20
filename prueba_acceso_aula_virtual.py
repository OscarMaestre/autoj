#!/usr/bin/env python3
from constantes import *
import sys

if __name__ == "__main__":
    usuario=sys.argv[1]
    clave=sys.argv[2]
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

    
    