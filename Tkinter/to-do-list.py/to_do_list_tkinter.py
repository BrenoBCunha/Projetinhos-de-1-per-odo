import customtkinter as ctk

root = ctk.CTk()
root.geometry('500x600')
root.resizable(width = False, height = False)
root.title('To Do List')

lbl_tarefas = ctk.CTkLabel(root, text = 'Tarefas', font = ('Arial', 16))
lbl_tarefas.place(x = 50, y = 50)

root.mainloop()