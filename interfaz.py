#Se importa libreria tkinter con todas sus funciones

from tkinter import * 

#ventana principal

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
logo = PhotoImage(file = "img/magnitudes.jpg")
lb_logo = Label(ventana_principal, image = logo)
lb_logo.place(x = 325 , y = 61)

# Entrada de numeros
e_texto = Entry(ventana_principal, font = ("Rubik 10"),justify= 'right', width = 15)
e_texto.place(x=241, y=85)

# Etiquetas para el titulo de app
titulo = Label(ventana_principal, text = "Celsius, kelvin y farenheit")
titulo.config(fg = "red", font = ("Bahnschrift Condensed",20))
titulo.place(x = 45, y = 10)

# Etiqueta para el input
texto_radio = Label(ventana_principal, text = "Dijite el valor del radio: ")
texto_radio.config(fg = "black", font = ("Arial",16))
texto_radio.place(x = 20, y = 80)

# Etiquetas para el output

resultado_perimetro = Label(ventana_principal, text = "El perimetro del circulo es: ")
resultado_perimetro.config(fg = "black", font = ("Arial",16))
resultado_perimetro.place(x = 20, y = 290)

resultado_area = Label(ventana_principal, text = "El área del circulo es: ")
resultado_area.config(fg = "black", font = ("Arial",16))
resultado_area.place(x = 20, y = 320)

# Botones
boton_operar = Button(ventana_principal, text = "Operar", width = 7, height = 1, fg = "red",font = ("Bahnschrift Condensed",15))
boton_operar.place(x=20, y=151)

# Se ejecuta el metodo main loop() de la clase Tk atraves de la instancia ventana_principal
#Este metodo despliega una ventana simple en pantallla y queda a la espera de lo que el usuario ha
# como (click,escribir, etc) Cada accion del usuario se conoce como un evento. El metodo mainloop()
#es un bucle infinito

ventana_principal.mainloop()