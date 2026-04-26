info = dict()
contatos = list()
count = 40

# ==== Configurações janela de contato ===
def abrir_novo_contato(frame):
    import customtkinter as ctk
    add_contato = ctk.CTkToplevel()
    add_contato.title("Novo Contato")
    add_contato.geometry("350x260")
    add_contato.grab_set()
    add_contato.focus_force()

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

    btn_add = ctk.CTkButton(add_contato, text='Adicionar', command= lambda: adicionar(etr_nome, etr_numero, etr_email, etr_endereco, add_contato, frame))
    btn_add.place(x = 180, y=200)

    btn_cancel = ctk.CTkButton(add_contato, text='Cancelar', fg_color="#F33939", command= add_contato.destroy)
    btn_cancel.place(x=20, y=200)

def adicionar(*etr):
    global info
    global contatos
    print(etr)
    info['nome'] = etr[0].get().strip()
    info['telefone'] = etr[1].get().strip()
    info['email'] = etr[2].get().strip()
    info['endereco'] = etr[3].get().strip()
    contatos.append(info.copy())
    info.clear()
    criar_contato(etr[5])
    etr[4].destroy()
    print(contatos)

def criar_contato(janela):
    import customtkinter as ctk
    global contatos
    global count
    contato = ctk.CTkButton(janela, text = contatos[-1]['nome'], fg_color="#414141", hover_color="#666666", width=450, anchor= 'w', command= lambda n=contatos.index(contatos[-1]): press(n, janela))
    contato.grid(row=1, column=0, padx=15, pady= count, sticky="nw")
    count += 35

def press(n, janela):
    global contatos
    import customtkinter as ctk
    add_contato = ctk.CTkToplevel()
    add_contato.title("Novo Contato")
    add_contato.geometry("350x260")
    add_contato.grab_set()
    add_contato.focus_force()
    

    lbl_nome = ctk.CTkLabel(add_contato, text = 'Nome: ', font=('Arial', 14))
    lbl_nome.place(x = 20, y = 20)

    etr_nome = ctk.CTkEntry(add_contato, width=230)
    etr_nome.place(x = 90, y = 20)
    etr_nome.insert(0, contatos[n]['nome'])
    etr_nome.configure(state= 'readonly')

    lbl_numero = ctk.CTkLabel(add_contato, text='Telefone: ', font=('Arial', 14))
    lbl_numero.place(x = 20, y = 60)

    etr_numero = ctk.CTkEntry(add_contato, width=230)
    etr_numero.place(x = 90, y = 60)
    etr_numero.insert(0, contatos[n]['telefone'])
    etr_numero.configure(state= 'readonly')

    lbl_email = ctk.CTkLabel(add_contato, text='E-mail: ', font=('Arial', 14))
    lbl_email.place(x = 20, y = 100)

    etr_email = ctk.CTkEntry(add_contato, width = 230)
    etr_email.place(x = 90, y = 100)
    etr_email.insert(0, contatos[n]['email'])
    etr_email.configure(state= 'readonly')

    lbl_endereco = ctk.CTkLabel(add_contato, text='Endereço: ', font=('Arial', 14))
    lbl_endereco.place(x = 20, y = 140)

    etr_endereco = ctk.CTkEntry(add_contato, width=230)
    etr_endereco.place(x=90, y = 140)
    etr_endereco.insert(0, contatos[n]['endereco'])
    etr_endereco.configure(state= 'readonly')

    # Botão Adicionar e Cancelar

    btn_editar = ctk.CTkButton(add_contato, text='Editar', command= lambda: editar(etr_nome, etr_numero, etr_email, etr_endereco, add_contato))
    btn_editar.place(x = 180, y=200)

    btn_Excluir = ctk.CTkButton(add_contato, text='Excluir', fg_color="#F33939", command= add_contato.destroy)
    btn_Excluir.place(x=20, y=200)

def editar(*etr):
    etr[0].configure(state='normal')
    etr[1].configure(state='normal')
    etr[2].configure(state='normal')
    etr[3].configure(state='normal')

def excluir(contato):
    contato.destroy()


    



        
