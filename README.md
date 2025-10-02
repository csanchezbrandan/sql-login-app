# 🖥️ SQL Login Automático

Aplicación de escritorio en Python que permite seleccionar una conexión predefinida y autocompletar los campos de IP, usuario y contraseña en el login de SQL Server Manager (u otro cliente SQL). Ideal para técnicos que gestionan múltiples servidores y quieren agilizar el acceso.

---

## 🚀 Características

- Interfaz gráfica con Tkinter.
- Lista de conexiones predefinidas (editable vía JSON).
- Doble clic para seleccionar una conexión.
- Escritura automática en el login del SQL Manager usando `pyautogui`.
- Fácil de empaquetar como `.exe` para otras PCs.

---

## 📦 Dependencias

Instalá las siguientes librerías con `pip`:

```bash
pip install pyautogui

Para el archivo JSON, debe tener esta estructura: 
[
  {
    "nombre": "Servidor Córdoba",
    "ip": "192.168.1.10",
    "usuario": "admin",
    "password": "1234"
  },
  {
    "nombre": "Servidor Buenos Aires",
    "ip": "10.0.0.5",
    "usuario": "root",
    "password": "abcd"
  }
]
