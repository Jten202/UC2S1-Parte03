# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:52:46 2023

@author: Usuario
"""

def obtener_credenciales_desde_archivos():
    with open("login.txt", "r") as archivo_login:
        login_almacenado = archivo_login.readline().strip()
    with open("clave.txt", "r") as archivo_clave:
        clave_almacenada = archivo_clave.readline().strip()
    return login_almacenado, clave_almacenada


def mostrar_menu():
    print("\nDatos Persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")


def main():
    login_almacenado, clave_almacenada = obtener_credenciales_desde_archivos()
    intentos = 0

    while intentos < 2:
        login_ingresado = input("Ingrese su usuario: ")
        clave_ingresada = input("Ingrese su clave: ")

        if login_ingresado == login_almacenado and clave_ingresada == clave_almacenada:
            mostrar_menu()
            return
        else:
            print("Usuario o clave incorrectos.")
            intentos += 1

    print("Número de intentos excedido. Programa terminando.")

main()