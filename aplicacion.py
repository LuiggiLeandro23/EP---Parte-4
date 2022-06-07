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


def listar():
    with open("nombre.txt") as contenido,open("codigo.txt") as contenido2, open("precio.txt") as contenido3:
       print( "Producto          Codigo                 Precio ")    
       for l1,l2,l3 in zip(contenido,contenido2,contenido3):
            print("|{:20}|{:20}|{:10}|".format(l1.rstrip(), l2.rstrip(), l3.rstrip()))
        
        

def agregar():
    archivo_nombre=open("nombre.txt","at")
    conte1=input("Digite producto: ")
    archivo_nombre.write(conte1+'\n')
    print("Se agrego el nombre correctamente")
    archivo_nombre.close
    
    archivo_nombre=open("codigo.txt","at")
    conte2=input("Digite codigo: ")
    archivo_nombre.write(conte2+'\n')
    print("Se agrego codigo correctamente")
    archivo_nombre.close

    archivo_nombre=open("precio.txt","at")
    conte3=input("Digite precio: ")
    archivo_nombre.write(conte3+'\n')
    print("Se agrego el precio correctamente")
    archivo_nombre.close

def salir():
      print("Gracias ")
    
    
    
while (usuario!=user or clave!=password) and veces<4 :
    
    usuario = input("Digite el nombre de usuario: ")+"\n"
    clave = input("Digite su clave de usuario: ")+" \n"
    
    archivo = open("usuarios.txt","rt")
    user = archivo.read()
    
    archivo = open("claves.txt","rt")
    password = archivo.read()
    op=0
   
    if (usuario==user and clave==password):
            while op!=3:
                print("\n-----DATOS PRODUCTO----")
                print("1. Listar")
                print("2. Agregar")
                print("3. Salir")
                op=int(input("Digite opcion: "))
                
                if op==1:
                    listar()
                elif op==2:
                    agregar()
                else:
                    salir()
    else:
            print("\nDatos incorrectos, ingrese nuevamente")
            veces +=1
            if veces == 4:
                print("\nSe superó el límite de intentos, inténtelo más tarde...")