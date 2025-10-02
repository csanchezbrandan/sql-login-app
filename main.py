import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import json

# Leer conexiones desde el archivo JSON
with open("conexiones.json", "r") as f:
    conexiones = json.load(f)

# Función para autocompletar login
def autocompletar_login(conexion):
    messagebox.showinfo("Info", f"Preparando para escribir en SQL Manager: {conexion['nombre']}")
    time.sleep(3)
    pyautogui.write(conexion["ip"])
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(conexion["usuario"])
    pyautogui.press('tab')
    pyautogui.write(conexion["password"])
    #pyautogui.press('enter')

# doble clic
def on_double_click(event):
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        conexion = conexiones[index]
        autocompletar_login(conexion)

# aqui se crea la ventana
ventana = tk.Tk()
ventana.title("Login SQL Automático")

# Permitir que la ventana se ajuste automáticamente
ventana.geometry("")  # Vacío = tamaño automático
ventana.resizable(True, True)  # Permite redimensionar manualmente

lista = tk.Listbox(ventana, width=60, height=10)
for conn in conexiones:
    lista.insert(tk.END, conn["nombre"])

lista.pack(padx=20, pady=20)
lista.bind("<Double-Button-1>", on_double_click)

ventana.mainloop()