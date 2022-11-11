#Se importa libreria tkinter con todas sus funciones

from tkinter import * 
from tkinter import messagebox

#ventana principal

# Funciones
def sumar():
    messagebox.showinfo("Suma 1.0", "hizo click en el boton sumar")
    z = int(x.get())+ int(y.get())
    boton_operar.insert(INSERT, "la suma de " + x.get()+ "+" +y.get()+ " casi siempre es " + str(z) + "\n")

ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Convertidor de temperatura")
ventana_principal.geometry("650x400")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)



#--------------------
#frame entrada datos
#--------------------

# imagen de la app
logo = PhotoImage(file = "img/magnitudes.png")
lb_logo = Label(ventana_principal, image = logo)
lb_logo.place(x = 380 , y = 70)


# Entry para grados celsius
#textvariable=x)
entry_x = Entry(ventana_principal)
entry_x.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_x.focus_set()
entry_x.place(x=190, y=78, width=115, height=30)

# Etiquetas para el titulo de app
titulo = Label(ventana_principal, text = "Celsius, kelvin y farenheit")
titulo.config(fg = "red", font = ("Bahnschrift Condensed",20))
titulo.place(x = 45, y = 10)

# Etiqueta para el input
# Etiqueta para x
lb_x = Label(ventana_principal, text = "Digite los °C: ")
lb_x.config(bg="white", fg="blue", font=("Arial",16))
lb_x.place(x=40, y=78, width=140, height=30)


# Botones
boton_operar = Button(ventana_principal, text = "Operar", width = 7, height = 1, fg = "red",font = ("Bahnschrift Condensed",15))
boton_operar.place(x=20, y=151)

# Se ejecuta el metodo main loop() de la clase Tk atraves de la instancia ventana_principal
#Este metodo despliega una ventana simple en pantallla y queda a la espera de lo que el usuario ha
# como (click,escribir, etc) Cada accion del usuario se conoce como un evento. El metodo mainloop()
#es un bucle infinito

ventana_principal.mainloop()