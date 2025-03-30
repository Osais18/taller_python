# Formulario usando el lamba
import tkinter as tk
import time
from tkinter import messagebox

class Formulario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Formulario para registro de Vehículos")

        self.registro_vehiculos = []

        self.ingresar_datos()
        self.mostrar_datos()

    def ingresar_datos(self):
        frame_formulario = tk.Frame(self.ventana)
        frame_formulario.pack(pady=10)

        self.label_placa = tk.Label(frame_formulario, text="Ingrese la Placa:")
        self.entry_placa = tk.Entry(frame_formulario)
        self.label_placa.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        self.label_marca = tk.Label(frame_formulario, text="Ingrese la Marca:")
        self.entry_marca = tk.Entry(frame_formulario)
        self.label_marca.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_marca.grid(row=1, column=1, padx=5, pady=5)

        self.label_color = tk.Label(frame_formulario, text="Ingrese el Color:")
        self.entry_color = tk.Entry(frame_formulario)
        self.label_color.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_color.grid(row=2, column=1, padx=5, pady=5)

        self.label_tipo = tk.Label(frame_formulario, text="¿Qué Tipo es? (Residente/Visitante):")
        self.entry_tipo = tk.Entry(frame_formulario)
        self.label_tipo.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_tipo.grid(row=3, column=1, padx=5, pady=5)

        self.boton_guardar = tk.Button(self.ventana, text="Guardar Datos", command=lambda: self.procesar_datos())
        self.boton_guardar.pack(pady=10)

        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar Campos", command=lambda: self.limpiar_campos())
        self.boton_limpiar.pack(pady=5)

    def procesar_datos(self):
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        color = self.entry_color.get()
        tipo = self.entry_tipo.get()

        if placa and marca and color and tipo:
            vehiculo = {
                "Placa": placa,
                "Marca": marca,
                "Color": color,
                "Tipo": tipo,
                "Hora de ingreso": time.strftime("%H:%M:%S")
            }
            self.registro_vehiculos.append(vehiculo)
            self.limpiar_campos()
            self.label_validacion.config(text="")
            messagebox.showinfo("Registro Exitoso", "Vehículo registrado correctamente.")
        else:
            self.label_validacion.config(text="Todos los campos son requeridos", fg="red")

    def mostrar_datos(self):
        self.label_validacion = tk.Label(self.ventana, text="")
        self.label_validacion.pack()

        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar Registros", command=lambda: self.mostrar_registro())
        self.boton_mostrar.pack(pady=5)

    def mostrar_registro(self):
        if self.registro_vehiculos:
            registros = "\n".join([f"{v['Placa']} - {v['Marca']} - {v['Color']} - {v['Tipo']} - {v['Hora de ingreso']}" for v in self.registro_vehiculos])
            messagebox.showinfo("Registros Guardados exitosamente ", registros)
        else:
            messagebox.showwarning("Sin Registros", "No hay vehículos registrados.")

    def limpiar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_color.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.label_validacion.config(text="")

ventana_principal = tk.Tk()
app = Formulario(ventana_principal)
ventana_principal.mainloop()
