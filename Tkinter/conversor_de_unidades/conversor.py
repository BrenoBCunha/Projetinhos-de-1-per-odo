import tkinter as tk
from tkinter import ttk


def convert():
    valor = float(entrada.get())
    opc1 = de.get()
    opc2 = para.get()
    if opc1 == 'Kelvin':
        if opc2 != 'Celcius' or opc2 != 'Farenheit':
            res['text'] = 'Opção inválida'
        if opc2 == 'Celcius':
            ans = valor - 273
            res['text'] = f'{ans:.2f}°C'
        elif opc2 == 'Farenheit':
            ans = (valor - 273) * (9 / 5) + 32
            res['text'] = f'{ans:.2f}°F'
    if opc1 == 'Celcius':
        if opc2 != 'Kelvin' or opc2 != 'Farenheit':
            res['text'] = 'Opção inválida'
        if opc2 == 'Kelvin':
            ans = valor + 273
            res['text'] = f'{ans:.2f} K'
        elif opc2 == 'Farenheit':
            ans = valor * (9 / 5) + 32
            res['text'] = f'{ans:.2f}°F'
    if opc1 == 'Farenheit':
        if opc2 != 'Kelvin' or opc2 != 'Celcius':
            res['text'] = 'Opção inválida'
        if opc2 == 'Kelvin':
            ans = (valor - 32) * 5 / 9 + 273
            res['text'] = f'{ans:.2f} K'
        elif opc2 == 'Celcius':
            ans = (valor - 32) * 5 / 9
            res['text'] = f'{ans:.2f}°C'


# Interface Tkinter

root = tk.Tk()
root.title('Conversor de unidades')
root.geometry('300x300')
tk.Button(root, text = 'Fechar', width = 7, command = root.destroy).place(x = 220, y = 250)


# Entrada do valor

tk.Label(root, text = 'Valor: ').place(x = 40, y = 50)
entrada = tk.Entry(root)
entrada.place(x = 90, y = 50)

#Caixas de seleção de conversão

tk.Label(root, text = 'De: ').place(x = 40, y = 90)
de = ttk.Combobox(
    root, 
    values = ['Kelvin', 'Farenheit', 'Celcius'], 
     state = 'readonly')
de.place(x = 90, y = 90)

tk.Label(root, text = 'Para: ').place(x = 40, y = 130)
para = ttk.Combobox(
    root, 
    values = ['Kelvin', 'Farenheit', 'Celcius'], 
     state = 'readonly')
para.place(x = 90, y = 130)

#Botão de conversão

conv = tk.Button(root, text = 'Converter', command = convert)
conv.place(x = 120, y = 170)

#Mostrador de resposta

res = tk.Label(root, text = '0')
res.place(x = 120, y = 220)

root.mainloop()