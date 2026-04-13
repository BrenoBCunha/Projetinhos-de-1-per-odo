import customtkinter as ctk

contatos = list()
info = dict()
count = 0


def add():
    global info
    global contatos
    info['nome'] = etr_nome.get().strip()
    info['sobrenome'] = etr_sobrenome.get().strip()
    info['email'] = etr_email.get().strip()
    info['telefone'] = etr_telefone.get().strip()
    info['endereco'] = etr_endereco.get().strip()
    contatos.append(info.copy())
    botton()
    cancel()

def cancel():
    global info
    global contatos
    etr_nome.delete(0, 'end')
    etr_sobrenome.delete(0, 'end')
    etr_email.delete(0, 'end')
    etr_telefone.delete(0, 'end')
    etr_endereco.delete(0, 'end')

def search():
    global info
    global contatos
    resp = False
    busca = etr_buscar.get()
    print(contatos)
    txt_detalhes.delete('0.0', 'end')
    for e in contatos:
        for k, v in e.items():
            print(k)
            print(v)
            if busca == v:
                txt_detalhes.insert('0.0', f'Nome: {e['nome']}\n\n' + f'Sobrenome: {e['sobrenome']}\n\n' + f'E-mail: {e['email']}\n\n' + 
                        f'Telefone: {e['telefone']}\n\n' + f'Endereço: {e['endereco']}\n\n')
                resp = True
                break
    if resp == False:
        txt_detalhes.insert('0.0', 'Contato não encontrado')
        
def botton():
    global count
    global btn_contato
    nome = info['nome']
    sobrenome = info['sobrenome']
    btn_contato = ctk.CTkButton(frm_nome, text = f'{nome} {sobrenome}', anchor = 'w', font = ('San Francisco', 12, 'bold'), width = 230, height = 30, border_width = 2,  fg_color = "#2B2B2B", corner_radius = 10, hover_color = "#4D4D4D", border_color ="#494949", command = lambda n = info['nome']: click)
    if count == 0:
        btn_contato.pack(pady = (10, 3))
        count += 1
    else:
        btn_contato.pack(pady = 3)
    

def click(n):
    global btn_contato
    if btn_contato.cget('fg_color') == "#2B2B2B":
        btn_contato.configure(fg_color = "#4D4D4D", width = 200)
    elif btn_contato.cget('fg_color') == "#4D4D4D":
        btn_contato.configure(fg_color = "#2B2B2B", width = 230)

   
def exclui():
    btn_contato.destroy()
    

def clear():
    txt_detalhes.delete('0.0', 'end')

def enter_press(event):
    if contatos == []:
        add()
    else:
        search()


### Interface Tkinter ###

root = ctk.CTk()
root.geometry('780x600')
root.title('Contatos')
ctk.set_appearance_mode("system")
root.resizable(width = False, height = False)
root.bind('<Return>', enter_press)

lbl_nome = ctk.CTkLabel(root, text = 'Primeiro nome: ', font = ('Arial', 15))
lbl_nome.place(x = 30, y = 20)

etr_nome = ctk.CTkEntry(root, width = 320)
etr_nome.place(x = 150, y = 20)

lbl_sobrenome = ctk.CTkLabel(root, text = 'Sobrenome: ', font = ('Arial', 15))
lbl_sobrenome.place(x= 30, y = 60)

etr_sobrenome = ctk.CTkEntry(root, width = 320)
etr_sobrenome.place(x = 150, y = 60)

lbl_email = ctk.CTkLabel(root, text = 'E-mail: ', font = ('Arial', 15))
lbl_email.place(x = 30, y = 100)

etr_email = ctk.CTkEntry(root, width = 320)
etr_email.place(x = 150, y = 100)

lbl_telefone = ctk.CTkLabel(root, text = 'Celular: ', font = ('Arial', 15))
lbl_telefone.place(x = 30, y = 140)

etr_telefone = ctk.CTkEntry(root, width = 320)
etr_telefone.place(x = 150, y = 140)

lbl_endereco = ctk.CTkLabel(root, text = 'Endereço: ', font = ('Arial', 15))
lbl_endereco.place(x = 30, y = 180)

etr_endereco = ctk.CTkEntry(root, width = 320)
etr_endereco.place(x = 150, y = 180)

lbl_buscar = ctk.CTkLabel(root, text = 'Buscar: ', font = ('Arial', 15))
lbl_buscar.place(x = 30, y = 280)

etr_buscar = ctk.CTkEntry(root, width = 250)
etr_buscar.place(x = 150, y = 280)

lbl_detalhes = ctk.CTkLabel(root, text = 'Detalhes: ', font = ('Arial', 15))
lbl_detalhes.place(x = 30, y = 400)

txt_detalhes = ctk.CTkTextbox(root, width = 320, height = 200, border_width = 3)
txt_detalhes.place(x = 150, y = 320)

### botões ###

btn_adicionar = ctk.CTkButton(root, text = 'Adicionar', width = 150, command = add)
btn_adicionar.place(x = 150, y = 220)

btn_cancelar = ctk.CTkButton(root, text = 'Cancelar', width = 150, command = cancel)
btn_cancelar.place(x = 320, y = 220)

btn_limpar = ctk.CTkButton(root, text = 'Limpar', width = 320, command = clear)
btn_limpar.place(x = 150, y = 540)

btn_buscar = ctk.CTkButton(root, text = 'Buscar', width = 60, command = search)
btn_buscar.place(x = 410, y = 280)

### Lista de contatos ###

frm_nome = ctk.CTkFrame(root, width = 250, height = 500, border_width = 3, corner_radius = 10)
frm_nome.place(x = 500, y = 20)
frm_nome.pack_propagate(False)

btn_editar = ctk.CTkButton(root, text = 'Editar', width = 120)
btn_editar.place(x = 500, y = 540)

btn_detalhes = ctk.CTkButton(root, text = 'Detalhes', width = 120)
btn_detalhes.place(x = 630, y = 540)

btn_contato = ctk.CTkButton(frm_nome)


root.mainloop()