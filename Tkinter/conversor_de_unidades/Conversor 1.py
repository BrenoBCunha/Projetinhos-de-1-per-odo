import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Conversor de Unidades')
root.geometry('300x300')

label = tk.Label(root, text = 'Valor: ').place(x = 50, y = 10)
entry = tk.Entry(root).place(x = 100, y = 10)

label = tk.Label(root, text = 'De: ').place(x = 50, y = 50)
combo_box1 = ttk.Combobox(
    root,
    values = ('mililitros', 'litros', 'metros cubicos', 'centimetros cubicos'),
    state = 'readonly'
).place(x = 100, y = 50)

lael = tk.Label(root, text = 'Para: ').place(x = 50, y = 90)
combo_box2 = ttk.Combobox(
    root,
    values = ('mililitros', 'litros', 'metros cubicos', 'centimetros cubicos'),
    state = 'readonly'
).place(x = 100, y = 90)


converter = tk.Button(root, text = 'Converter', width = 10).place(x = 120, y = 130)


fechar = tk.Button(root, text = 'Fechar', command = root.destroy).place(x = 230, y = 250)

root.mainloop()