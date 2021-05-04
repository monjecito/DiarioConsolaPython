"""
Proyecto python y mysql
Registro y login de usuarios
En función de la respuesta tendrá acceso a ciertas funcionalidades
Crear notas, mostrarlas o borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -Registro
    -Login
""")

hazEl=acciones.Acciones()
accion=input("Que deseas hacer?: ")
if accion=="registro":
    hazEl.registro()


elif accion=="login":
    hazEl.login()