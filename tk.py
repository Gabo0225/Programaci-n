# Importar libreria

from tkinter import *
# 0. Clase principañ

class principal:
    def __init__(self):
        self.counter = 0

    # 1. crear la ventana principal
        self.root = Tk()
        self.root.title("Mi primera ventana")
        self.root.geometry("400x300")

    # 2. Añadir widget "etiqueta de texto"
    def counter_label(self):
        global counter
        counter += 1
        self.msg.config(text=f"Has clickeado el boton {counter} veces")
    def button_clicked(self):
        # Acciones a realizar al presionar el botón
        self.mensaje.config(text="Hola Mundo desde el boton")
        self.msg=Label(self.root, text="Hola Mundo")
        self.mensaje=Label(self.root, text="Hola Mundo")
        self.but=Button(self.root, text="Contador", command=self.counter_label)
        self.bot=Button(self.root, text="Presioname", command=self.button_clicked)
        self.boton=Button(self.root, text="Cerrar", command=self.root.quit)
        self.menu=Menu(self.root)
        self.root.config(menu=self.menu)
        

    # 3. Ubicarlo en la ventana
        self.entrada.pack()
        self.mensaje.pack()
        self.menu.add_command(label="Archivo")
        self.menu.add_command(label="Editar")
        self.msg.pack()
        self.but.pack()
        self.bot.pack()
        self.boton.pack()

    

# 4. Bucle principal
p=principal()
p.root.mainloop()

