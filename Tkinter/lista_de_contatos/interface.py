import customtkinter as ctk

# ==== Configurações de interface ====
root = ctk.CTk()
root.title('Lista de Contatos')
root.geometry('500x600')
ctk.set_appearance_mode("system")
root.resizable(width = False, height = False)

# ==== Configurações janela de contato ===

add_contato = ctk.CTkToplevel()
add_contato.title("Novo Contato")
add_contato.geometry("350x260")

lbl_nome = ctk.CTkLabel(add_contato, text = 'Nome: ', font=('Arial', 14))
lbl_nome.place(x = 20, y = 20)

etr_nome = ctk.CTkEntry(add_contato, width=230)
etr_nome.place(x = 90, y = 20)

lbl_numero = ctk.CTkLabel(add_contato, text='Telefone: ', font=('Arial', 14))
lbl_numero.place(x = 20, y = 60)

etr_numero = ctk.CTkEntry(add_contato, width=230)
etr_numero.place(x = 90, y = 60)

lbl_email = ctk.CTkLabel(add_contato, text='E-mail: ', font=('Arial', 14))
lbl_email.place(x = 20, y = 100)

etr_email = ctk.CTkEntry(add_contato, width = 230)
etr_email.place(x = 90, y = 100)

lbl_endereco = ctk.CTkLabel(add_contato, text='Endereço: ', font=('Arial', 14))
lbl_endereco.place(x = 20, y = 140)

etr_endereco = ctk.CTkEntry(add_contato, width=230)
etr_endereco.place(x=90, y = 140)

# Botão Adicionar e Cancelar

btn_add = ctk.CTkButton(add_contato, text='Adicionar')
btn_add.place(x = 180, y=200)

btn_cancel = ctk.CTkButton(add_contato, text='Cancelar', fg_color="#F33939")
btn_cancel.place(x=20, y=200)

# Configuração do Grid principal (2 colunas, 1 linha)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# ==== Frame pincipal (pesquisa e lista) ====
frame_principal = ctk.CTkFrame(root, fg_color="transparent")
frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1) # Permite que a lista expanda

# 1. Sub-frame da Barra de Pesquisa
frame_pesquisa = ctk.CTkFrame(frame_principal, fg_color="transparent")
frame_pesquisa.grid(row=0, column=0, sticky="ew", pady=(0, 20))
frame_pesquisa.grid_columnconfigure(0, weight=1)

entry_pesquisa = ctk.CTkEntry(frame_pesquisa, placeholder_text="Pesquisar por nome ou número...")
entry_pesquisa.grid(row=0, column=0, sticky="ew", padx=(0, 10))

btn_pesquisar = ctk.CTkButton(frame_pesquisa, text="Pesquisar", width=100)
btn_pesquisar.grid(row=0, column=1)

# 2. Área da Lista de Contatos (Frame com Scroll)
frame_lista = ctk.CTkScrollableFrame(frame_principal, label_text="Meus Contatos")
frame_lista.grid(row=1, column=0, sticky="nsew")

root.mainloop()