import customtkinter as ctk

class AppContatos(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ============ CONFIGURAÇÕES DA JANELA ============
        self.title("Lista de Contatos - CRUD")
        self.geometry("750x500")
        
        # Define o tema escuro e a cor de destaque
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configuração do Grid principal (2 colunas, 1 linha)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ============ FRAME LATERAL (MENU DE BOTÕES) ============
        self.frame_menu = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")
        self.frame_menu.grid_rowconfigure(6, weight=1) # Espaçador para empurrar conteúdo para cima

        self.label_titulo = ctk.CTkLabel(self.frame_menu, text="Menu de Opções", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botões de Ação do CRUD
        self.btn_adicionar = ctk.CTkButton(self.frame_menu, text="Adicionar Contato")
        self.btn_adicionar.grid(row=1, column=0, padx=20, pady=10)

        self.btn_editar = ctk.CTkButton(self.frame_menu, text="Editar Contato")
        self.btn_editar.grid(row=2, column=0, padx=20, pady=10)

        self.btn_visualizar = ctk.CTkButton(self.frame_menu, text="Visualizar Contato")
        self.btn_visualizar.grid(row=3, column=0, padx=20, pady=10)

        self.btn_excluir = ctk.CTkButton(self.frame_menu, text="Excluir Contato", fg_color="#C0392B", hover_color="#922B21")
        self.btn_excluir.grid(row=4, column=0, padx=20, pady=10)

        # ============ FRAME PRINCIPAL (PESQUISA E LISTA) ============
        self.frame_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1) # Permite que a lista expanda

        # 1. Sub-frame da Barra de Pesquisa
        self.frame_pesquisa = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_pesquisa.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        self.frame_pesquisa.grid_columnconfigure(0, weight=1)

        self.entry_pesquisa = ctk.CTkEntry(self.frame_pesquisa, placeholder_text="Pesquisar por nome ou número...")
        self.entry_pesquisa.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.btn_pesquisar = ctk.CTkButton(self.frame_pesquisa, text="Pesquisar", width=100)
        self.btn_pesquisar.grid(row=0, column=1)

        # 2. Área da Lista de Contatos (Frame com Scroll)
        self.frame_lista = ctk.CTkScrollableFrame(self.frame_principal, label_text="Meus Contatos")
        self.frame_lista.grid(row=1, column=0, sticky="nsew")

        # Mockup: Popula a lista com contatos falsos apenas para visualização
        for i in range(1, 11):
            lbl_contato = ctk.CTkLabel(self.frame_lista, text=f"👤 Contato Fictício {i}  |  (82) 90000-000{i-1}", anchor="w")
            lbl_contato.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

if __name__ == "__main__":
    app = AppContatos()
    app.mainloop()