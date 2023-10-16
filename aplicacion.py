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

def listar_personas():
    with open("dni.txt", "r") as dnis, open("nombre.txt", "r") as nombres, open("apellido.txt", "r") as apellidos:
        for dni, nombre, apellido in zip(dnis, nombres, apellidos):
            print(f"DNI:\t{dni.strip()}\t|\tNombre:\t{nombre.strip()}\t|\tApellido:\t{apellido.strip()}")

def agregar_personas():
    dni = input("Ingrese DNI de la persona: ")
    nombre = input("Ingrese nombre de la persona: ")
    apellido = input("Ingrese apellido de la persona: ")

    with open("dni.txt", "a") as dnis:
        dnis.write(dni + "\n")
    with open("nombre.txt", "a") as nombres:
        nombres.write(nombre + "\n")
    with open("apellido.txt", "a") as apellidos:
        apellidos.write(apellido + "\n")

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
            while True:
                mostrar_menu()
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    listar_personas()
                elif opcion == "2":
                    agregar_personas()
                elif opcion == "3":
                    print("Saliendo...")
                    return
                else:
                    print("Opción inválida. Intente nuevamente.")
        else:
            print("Usuario o clave incorrectos.")
            intentos += 1

    print("Número de intentos excedido. Programa terminando.")

main()