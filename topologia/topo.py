"""Criação da Topologia"""
from abc import ABC, abstractmethod

from canal import Canal
from no import No


class Topologia(ABC):
    def __init__(self, dados_rede):
        self.rede = dict()

    def gerar_topologia(self):
        pass

    def gerar_nos(self, nos):
        """

        :param nos: um iteravel contendo dados para criar cada nó
        :type nos: tuple, list, etc
        :return:
        :rtype:
        """
        for no in nos:
            pass

    def gerar_canais(self, canais):
        pass


if __name__ == "__main__":
    teste = {
        "no": {
            "A": {"num_qubits": 2, "sistema": "supercondutor", "tipo": "processador"},
            "B": {"num_qubits": 2},
        },
        "canal": {"classico": {("A", "B"): None}, "quantico": {("A", "B"): None}},
    }

    """
    Estruturas:
        - Topologia -> criação da estrutura de conexão entre nós da rede
        - Física -> inserção dos componentes físicos dentro de uma determinada rede
        - Aplicação -> 
    """
