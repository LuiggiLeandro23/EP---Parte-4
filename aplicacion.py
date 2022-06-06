# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:38:51 2022

@author: admin
"""

user = "u"
password = "p"
usuario = "U"
clave = "P"
veces = 1

while (usuario!=user or clave!=password) and veces<4 :
    
    usuario = input("Digite el nombre de usuario: ")+"\n"
    clave = input("Digite su clave de usuario: ")+" \n"
    
    archivo = open("usuarios.txt","rt")
    user = archivo.read()
    
    archivo = open("claves.txt","rt")
    password = archivo.read()
    
    if (usuario==user and clave==password):
        print("\n-----DATOS PRODUCTO----")
        print("1. Listar")
        print("2. Agregar")
        print("3. Salir")
        
    else:
        print("\nDatos incorrectos, ingrese nuevamente")
        veces +=1
        if veces == 4:
            print("\nSe superó el límite de intentos, inténtelo más tarde...")