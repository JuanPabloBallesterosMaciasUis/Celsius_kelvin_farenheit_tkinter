#Se importa libreria tkinter con todas sus funciones

from tkinter import * 
from tkinter import messagebox

#ventana principal

# Funciones
def operar():
    messagebox.showinfo("Convertidor de temperatura 1.0", "hizo click en el boton operar")
    k = int(x.get())+ 273
    f = int(x.get())*9/5 + 32

    t_resultados.insert(INSERT, str(k)+ " grados kelvin. "+"\n" + str(f) + " grados farenheit."+"\n")

ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Convertidor de temperatura")
ventana_principal.geometry("650x335")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Variables globales
x = StringVar()

#--------------------
#frame entrada datos
#--------------------

# imagen de la app
logo = PhotoImage(file = "img/magnitudes.png")
lb_logo = Label(ventana_principal, image = logo)
lb_logo.place(x = 380 , y = 70)


# Entry para grados celsius

entry_x = Entry(ventana_principal,textvariable=x)
entry_x.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_x.focus_set()
entry_x.place(x=190, y=78, width=115, height=30)

# Etiquetas para el titulo de app
titulo = Label(ventana_principal, text = "Celsius, kelvin y farenheit")
titulo.config(fg = "red", font = ("Bahnschrift Condensed",20))
titulo.place(x = 45, y = 10)

# Etiqueta para el input
# Etiqueta para x
datos = Label(ventana_principal, text = "Digite los °C: ")
datos.config(bg="white", fg="blue", font=("Arial",16))
datos.place(x=23, y=78, width=140, height=30)


# Botones
boton_operar = Button(ventana_principal, text = "Operar",command=operar, width = 7, height = 1, fg = "red",font = ("Bahnschrift Condensed",15))
boton_operar.place(x=130, y=125)

t_resultados = Text(ventana_principal)
t_resultados.config( fg="black", font=("Rockwell Condensed",20))
t_resultados.place(x=20,y=200,width=300,height=75)


# Se ejecuta el metodo main loop() de la clase Tk atraves de la instancia ventana_principal
#Este metodo despliega una ventana simple en pantallla y queda a la espera de lo que el usuario ha
# como (click,escribir, etc) Cada accion del usuario se conoce como un evento. El metodo mainloop()
#es un bucle infinito

ventana_principal.mainloop()