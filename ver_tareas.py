#!/usr/bin/env python3
#coding=utf-8


from constantes import *
import sys
from selenium.webdriver.common.keys import Keys
from time import sleep

usuario=sys.argv[1]
clave=sys.argv[2]


enlaces=[
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=54994",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55010",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55023",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55036",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55068",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55091",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55107",
    "https://aulafp1920.castillalamancha.es/mod/forum/view.php?id=55124",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55133",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55112",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55097",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55073",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55041",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55028",
    "https://aulafp1920.castillalamancha.es/mod/assign/view.php?id=55015"
    
    
]

driver=get_driver_acceso_aula_virtual(usuario, clave)

sleep(5)

for e in reversed(enlaces):
    print("Abriendo enlace "+e)
    abrir_pestania_en_driver(driver, e)
    print(e)


