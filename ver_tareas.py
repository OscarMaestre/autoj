#!/usr/bin/env python3
#coding=utf-8


from constantes import *
import sys
from selenium.webdriver.common.keys import Keys
from time import sleep

usuario=sys.argv[1]
clave=sys.argv[2]


enlaces=[
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

driver=get_driver_acceso_aula_virtual(usuario, clave)

sleep(5)

for e in reversed(enlaces):
    print("Abriendo enlace "+e)
    abrir_pestania_en_driver(driver, e)
    print(e)


