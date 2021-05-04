import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\n Ok! Vamos a registrarte en el sistema")
        nombre=input("Introduce tu nombre ?:")
        apellidos=input("Introduce tus apellidos :")
        email=input("Introduce tu correo :")
        password=input("Introduce tu password :")

        usuario=modelo.Usuario(nombre,apellidos,email,password)
        registro=usuario.registrar()

        if registro[0]>=1:
            print(f"\n Perfecto {registro[1].nombre} te has registrado con el email :{registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\n Vale!!Identificate en el sistema...")
        try:
            email=input("Introduce tu email :")
            password=input("Introduce tu password :")

            usuario=modelo.Usuario('','',email,password)
            login=usuario.identificar()
            print(login)
            if email == login[3]:
                print(f"\n Bienvenido {login[1]}, te has logueado en el sistema {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo mas tarde")


    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles:
        -Crear nota(crear)
        -Mostrar tus notas(mostrar)
        -Eliminar notas(eliminar)
        -Salir(salir)
        """)

        accion=input("Que quieres hacer?")
        hazEl=notas.acciones.Acciones()

        if accion=="crear":
            hazEl.crear(usuario)
            print("\n Vamos a crear una nota")
            self.proximasAcciones(usuario)

        elif accion=="mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion=="eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion=="salir":
            print(f"\n Hasta pronto {usuario[1]}!")
            exit()
