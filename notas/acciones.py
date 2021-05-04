import notas.nota as modelo
class Acciones:

    def crear(self,usuario):
        print(f"Ok {usuario[1]}! Vamos a crear una nueva nota")

        titulo=input("\n Introduce el titulo de tu nota: ")
        descripcion=input("\n Mete el contenido de tu nota: ")

        nota=modelo.Nota(usuario[0],titulo,descripcion)
        guardar=nota.guardar()

        if guardar[0]>=1:
            print(f"Perfecto, has guardado la nota {nota.titulo}")
        else:
            print(f"Lo siento {usuario[1]} no se ha guardado la nota")

    def mostrar(self,usuario):
        print(f"Vale {usuario[1]}!!,aquí tienes tus notas")

        nota=modelo.Nota(usuario[0])
        notas=nota.listar()

        for nota in notas:
            print("\n*****************")
            print(nota[2])
            print(nota[3])
            print("*****************")

    def borrar(self,usuario):
        print(f"\n Okey,{usuario[1]},Vamos a borrar notas")

        titulo=input("Introduce el titulo de la nota que quieres eliminar: ")

        nota=modelo.Nota(usuario[0],titulo)
        eliminar=nota.eliminar()

        if eliminar[0]>=1:
            print(f"Hemos borrado la nota :{nota.titulo} correctamente")
        else:
            print("No se ha borrado la nota, intentalo de nuevo")
        