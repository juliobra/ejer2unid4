import tkinter as tk

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculo del IVA")
        
        self.label_precio_base = tk.Label(self.ventana, text="Precio Base:")
        self.label_precio_base.pack()
        
        self.entry_precio_base = tk.Entry(self.ventana)
        self.entry_precio_base.pack()
        
        self.label_porcentaje_iva = tk.Label(self.ventana, text="Porcentaje de IVA:")
        self.label_porcentaje_iva.pack()
        
        self.combo_porcentaje_iva = tk.ttk.Combobox(self.ventana, values=["10.5%", "21%"])
        self.combo_porcentaje_iva.pack()
        
        self.btn_calcular_iva = tk.Button(self.ventana, text="Calcular IVA", command=self.calcular_iva)
        self.btn_calcular_iva.pack()
        
        self.label_resultado = tk.Label(self.ventana, text="")
        self.label_resultado.pack()
    
    def calcular_iva(self):
        try:
            precio_base = float(self.entry_precio_base.get())
            porcentaje_iva = float(self.combo_porcentaje_iva.get().replace("%", ""))
            iva = precio_base * porcentaje_iva / 100
            total = precio_base + iva
            self.label_resultado.config(text=f"IVA: {iva:.2f} - Total: {total:.2f}")
        except ValueError:
            self.label_resultado.config(text="Ingrese un valor numérico válido")
        

app = App()
app.ventana.mainloop()