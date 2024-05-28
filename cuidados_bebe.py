import tkinter as tk
from abc import ABC, abstractmethod

class Bebe:
    def __init__(self, nome, data_nascimento, peso, altura, grupo_sanguineo):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura
        self.grupo_sanguineo = grupo_sanguineo

class Registro(ABC):
    @abstractmethod
    def __init__(self, data_hora):
        self.data_hora = data_hora

    @abstractmethod
    def detalhes(self):
        pass

class Alimentacao(Registro):
    def __init__(self, data_hora, tipo, quantidade):
        super().__init__(data_hora)
        self.tipo = tipo
        self.quantidade = quantidade

    def detalhes(self):
        return f"Alimentação: {self.data_hora}, Tipo: {self.tipo}, Quantidade: {self.quantidade} ml"

class TrocaDeFralda(Registro):
    def __init__(self, data_hora, tipo, observacoes):
        super().__init__(data_hora)
        self.tipo = tipo
        self.observacoes = observacoes

    def detalhes(self):
        return f"Troca de Fralda: {self.data_hora}, Tipo: {self.tipo}, Observações: {self.observacoes}"

class Sono(Registro):
    def __init__(self, data_hora_inicio, data_hora_fim, qualidade):
        super().__init__(data_hora_inicio)
        self.data_hora_fim = data_hora_fim
        self.qualidade = qualidade

    def detalhes(self):
        return f"Sono: Início: {self.data_hora}, Fim: {self.data_hora_fim}, Qualidade: {self.qualidade}"

class ConsultaMedica(Registro):
    def __init__(self, data_hora, medico, motivo, observacoes):
        super().__init__(data_hora)
        self.medico = medico
        self.motivo = motivo
        self.observacoes = observacoes

    def detalhes(self):
        return f"Consulta Médica: {self.data_hora}, Médico: {self.medico}, Motivo: {self.motivo}, Observações: {self.observacoes}"

class RegistrosCuidados:
    def __init__(self):
        self.registros = []

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def visualizar_registros(self):
        for registro in self.registros:
            print(registro.detalhes())

class TestaAplicacao:
    def __init__(self):
        self.bebe = None
        self.registros = RegistrosCuidados()
        self.init_interface()

    def criar_bebe(self, nome, data_nascimento, peso, altura, grupo_sanguineo):
        self.bebe = Bebe(nome, data_nascimento, peso, altura, grupo_sanguineo)

    def adicionar_registro(self, registro):
        self.registros.adicionar_registro(registro)

    def visualizar_registros(self):
        if self.bebe:
            print("Perfil do Bebê:")
            print(f"Nome: {self.bebe.nome}")
            print(f"Data de Nascimento: {self.bebe.data_nascimento}")
            print(f"Peso: {self.bebe.peso} kg")
            print(f"Altura: {self.bebe.altura} cm")
            print(f"Grupo Sanguíneo: {self.bebe.grupo_sanguineo}")

        self.registros.visualizar_registros()

    def init_interface(self):
        self.root = tk.Tk()
        self.root.title("Gut Gut - Cuidados com o Bebê")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.lbl_nome = tk.Label(self.frame, text="Nome:")
        self.lbl_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1)

        self.lbl_data_nascimento = tk.Label(self.frame, text="Data de Nascimento:")
        self.lbl_data_nascimento.grid(row=1, column=0)
        self.entry_data_nascimento = tk.Entry(self.frame)
        self.entry_data_nascimento.grid(row=1, column=1)

        self.lbl_peso = tk.Label(self.frame, text="Peso (kg):")
        self.lbl_peso.grid(row=2, column=0)
        self.entry_peso = tk.Entry(self.frame)
        self.entry_peso.grid(row=2, column=1)

        self.lbl_altura = tk.Label(self.frame, text="Altura (cm):")
        self.lbl_altura.grid(row=3, column=0)
        self.entry_altura = tk.Entry(self.frame)
        self.entry_altura.grid(row=3, column=1)

        self.lbl_grupo_sanguineo = tk.Label(self.frame, text="Grupo Sanguíneo:")
        self.lbl_grupo_sanguineo.grid(row=4, column=0)
        self.entry_grupo_sanguineo = tk.Entry(self.frame)
        self.entry_grupo_sanguineo.grid(row=4, column=1)

        self.btn_criar_bebe = tk.Button(self.frame, text="Criar Bebê", command=self.handle_criar_bebe)
        self.btn_criar_bebe.grid(row=5, column=0, columnspan=2)

        self.lbl_tipo_registro = tk.Label(self.frame, text="Tipo de Registro:")
        self.lbl_tipo_registro.grid(row=6, column=0)
        self.tipo_registro = tk.StringVar(value="alimentacao")
        self.options_tipo_registro = ["alimentacao", "sono", "troca_de_fralda", "consulta_medica"]
        self.optionmenu_tipo_registro = tk.OptionMenu(self.frame, self.tipo_registro, *self.options_tipo_registro)
        self.optionmenu_tipo_registro.grid(row=6, column=1)

        self.lbl_data_hora = tk.Label(self.frame, text="Data e Hora:")
        self.lbl_data_hora.grid(row=7, column=0)
        self.entry_data_hora = tk.Entry(self.frame)
        self.entry_data_hora.grid(row=7, column=1)

        self.lbl_detalhes_1 = tk.Label(self.frame, text="Detalhe 1:")
        self.lbl_detalhes_1.grid(row=8, column=0)
        self.entry_detalhes_1 = tk.Entry(self.frame)
        self.entry_detalhes_1.grid(row=8, column=1)

        self.lbl_detalhes_2 = tk.Label(self.frame, text="Detalhe 2:")
        self.lbl_detalhes_2.grid(row=9, column=0)
        self.entry_detalhes_2 = tk.Entry(self.frame)
        self.entry_detalhes_2.grid(row=9, column=1)

        self.lbl_detalhes_3 = tk.Label(self.frame, text="Detalhe 3:")
        self.lbl_detalhes_3.grid(row=10, column=0)
        self.entry_detalhes_3 = tk.Entry(self.frame)
        self.entry_detalhes_3.grid(row=10, column=1)

        self.btn_adicionar_registro = tk.Button(self.frame, text="Adicionar Registro", command=self.handle_adicionar_registro)
        self.btn_adicionar_registro.grid(row=11, column=0, columnspan=2)

        self.btn_visualizar_registros = tk.Button(self.frame, text="Visualizar Registros", command=self.visualizar_registros)
        self.btn_visualizar_registros.grid(row=12, column=0, columnspan=2)

        self.root.mainloop()

    def handle_criar_bebe(self):
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())
        grupo_sanguineo = self.entry_grupo_sanguineo.get()
        self.criar_bebe(nome, data_nascimento, peso, altura, grupo_sanguineo)

    def handle_adicionar_registro(self):
        tipo = self.tipo_registro.get()
        data_hora = self.entry_data_hora.get()
        detalhe1 = self.entry_detalhes_1.get()
        detalhe2 = self.entry_detalhes_2.get()
        detalhe3 = self.entry_detalhes_3.get()

        if tipo == 'alimentacao':
            registro = Alimentacao(data_hora, detalhe1, int(detalhe2))
        elif tipo == 'sono':
            registro = Sono(data_hora, detalhe2, detalhe3)
        elif tipo == 'troca_de_fralda':
            registro = TrocaDeFralda(data_hora, detalhe1, detalhe2)
        elif tipo == 'consulta_medica':
            registro = ConsultaMedica(data_hora, detalhe1, detalhe2, detalhe3)

        self.adicionar_registro(registro)

if __name__ == "__main__":
    TestaAplicacao()
