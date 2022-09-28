#---------------------------
#-------    RAIZ    --------
#---------------------------

from os import preadv
from re import I
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math 

#-------------------------
#--FUNCIONES DE LA APP----
#-------------------------

def sumar ():
    D = int(B.get())**2-4*int(A.get())*int(C.get())
    if D > 0 :
        x1=(-int(B.get())+math.sqrt(D))/2*int(A.get())
        x2=(-int(B.get())-math.sqrt(D))/2*int(A.get())
        t_resultados.insert( INSERT,"El valor de x1 es :"+str(x1)+" y el valor de x2 es: "+str(x2))

    else:
        if D == 0 :
            x1 =-int(B.get())/(2*int(A.get()))                      
            t_resultados.insert,(INSERT, "El valor de x1 y x2 es:" +str(x1))
        else:
            t_resultados.insert(INSERT,"Son raices imaginarias o complejas")


def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    A.set("")
    B.set("")
    C.set("")
    t_resultados.delete("1.0", "end")

def salir():
     messagebox.showinfo("La appp se cerrarrá ...")
     ventana_principal.destroy()



#------------------------
#---ventana principal----
#------------------------

 # Se declara una variable que llamamos ventana_principal y que se adquiere las caracteristicas de un objeto TK 
 

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("iris Alviarez")

#Establecer tamaño de la venta
ventana_principal.geometry("800x500")

ventana_principal.iconbitmap("")

#deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="black")

#-------------------------
#--Variables globales----
#-------------------------

A= StringVar()
B= StringVar()
C= StringVar()
D= IntVar()
x1= IntVar()
x2= IntVar()




#----------------------
#----frame entrada-----
#----------------------

frame_entrada = Frame(ventana_principal) 
frame_entrada.config(bg="light sea green", width=320, height=480)
frame_entrada.place(x=10,y=10)

 #Etiqueta para el subtitulo de la app
subtitule = Label(frame_entrada, text="Especialidad de sistemas")
subtitule.config(bg="light sea green", fg="snow", font=("Times New Roman", 12))
subtitule.place(x=60, y=260)

 #Etiqueta para el subtitulo2 de la app
subtitule2 = Label(frame_entrada, text="RAIZ CUADRATICA")
subtitule2.config(bg="light sea green", fg="snow", font=("Times New Roman", 15), anchor = CENTER)
subtitule2.place(x=45 , y=230)

# Imagen - logo de la app
logo = PhotoImage(file="guia_02/raiz.png")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=40 , y=10)

#Etiqueta para valor a
etiq_a = Label(frame_entrada , text="Introduzca el valor de A = ")
etiq_a.config(bg="light sea green", fg="snow", font=("Arial", 15), anchor = CENTER)
etiq_a.place(x=10, y=300)

#entry para el valor a
entry_a = Entry(frame_entrada , width=4, textvariable=A)
entry_a.config(font=("Arial" , 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=250 , y=295)


etiq_b = Label(frame_entrada , text="Introduzca el valor de B = ")
etiq_b.config(bg="light sea green", fg="snow", font=("Arial", 15), anchor = CENTER)
etiq_b.place(x=10 , y=350)

#entry para el valor b
entry_b = Entry(frame_entrada , width=4, textvariable=B)
entry_b.config(font=("Arial" , 20), justify=CENTER)
entry_b.place(x=250 , y=350)

#Etiqueta para valor c

etiq_c=Label(frame_entrada, text="Introduzca el valor de C = ")
etiq_c.config(bg="light sea green", fg="snow", font=("Arial", 15), anchor=CENTER)
etiq_c.place(x=10, y=400)

entry_c=Entry(frame_entrada, width=4, textvariable= C)
entry_c.config(font=("Arial", 20), justify=CENTER)
entry_c.focus_set()
entry_c.place(x=250,y=400)


frame_operaciones = Frame(ventana_principal) 
frame_operaciones.config(bg="cyan2", width=200, height=480)
frame_operaciones.place(x=340,y=10)


 #Button de suma
bt_sum = PhotoImage(file="guia_02/raiz1.png")
bt_sumar=Button(frame_operaciones ,image=bt_sum, width=105 , height=105, command=sumar)
bt_sumar.place(x=40 , y=50)


#button de salir
bt_sal = PhotoImage(file="guia_02/saliva.png")
bt_salir=Button(frame_operaciones ,image=bt_sal, width=105 , height=105, command=salir)
bt_salir.place(x=40 , y=200)


#button de borrar
bt_bor = PhotoImage(file="guia_02/borrar.png")
bt_borrar=Button(frame_operaciones , image=bt_bor, width=105 , height=105 , command=borrar)
bt_borrar.place(x=40 , y=360)


frame_resultados = Frame(ventana_principal) 
frame_resultados.config(bg="orange3", width=260, height=480)
frame_resultados.place(x=550,y=10)
#------------------------------
# Area de texto para resultados 
#------------------------------


t_resultados = Text(frame_resultados , width=14 , height=17)
t_resultados.config(bg="snow3" , fg="black" , font=("Courier" , 20))
t_resultados.pack()


#Se ejecuta el metodo mainloop de la clase Tk a traves de la istancia ventana principal. Este metedo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga, por ejemplo, click en el boton,escribir en caja de texto, ect. Cada acción del usuario se conoce como un evento. El método mainloop es bucle infinito

ventana_principal.mainloop()