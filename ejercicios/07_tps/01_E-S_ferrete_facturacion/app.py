import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        producto_1=float(self.txt_importe_1.get())
        producto_2=float(self.txt_importe_2.get())
        producto_3=float(self.txt_importe_3.get())

        suma_de_productos=producto_1 + producto_2 + producto_3

        resultado_str=str(suma_de_productos)

        alert(title="Pago total", message="El monto total de los productos es: " +resultado_str)
    

    def btn_promedio_on_click(self):
        producto_1=float(self.txt_importe_1.get())
        producto_2=float(self.txt_importe_2.get())
        producto_3=float(self.txt_importe_3.get())

        suma_de_productos=producto_1 + producto_2 + producto_3
        promedio_de_producto= suma_de_productos / 3
        promedio_str=str(promedio_de_producto)

        alert(title="Factura", message="El ticket promedio es de : " +promedio_str)

        

    def btn_total_iva_on_click(self):
        producto_1=float(self.txt_importe_1.get())
        producto_2=float(self.txt_importe_2.get())
        producto_3=float(self.txt_importe_3.get())

        suma_de_los_productos=producto_1 + producto_2 + producto_3
        incremento_iva= suma_de_los_productos * (21 / 100 )
        nuevo_precio_iva=suma_de_los_productos + incremento_iva
        iva_str=str(nuevo_precio_iva)
        
        
        alert(title="Factura", message="El valor de los productos es {0} con el iva 21% le queda en {1}".format(suma_de_los_productos, iva_str))

      
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()