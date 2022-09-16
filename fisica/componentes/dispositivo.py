class Processador:
    def __init__(self, nome, tempo_resposta):
        self.nome = nome
        self.tempo_resposta = tempo_resposta


class Memoria:
    def __init__(self, nome, tempo_armazenamento):
        self.nome = nome
        self.tempo_armazenamento = tempo_armazenamento


class Interface:
    pass


class ProcessadorSupercondutor(Processador):
    def __init__(self, nome):
        tempo_resposta = 1e-8
        super().__init__(nome=nome, tempo_resposta=tempo_resposta)


class MemoriaSupercondutor(Memoria):
    def __init__(self, nome):
        tempo_armazenamento = 1e-1
        super().__init__(nome=nome, tempo_armazenamento=tempo_armazenamento)
