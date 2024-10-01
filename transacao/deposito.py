from .transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_aceita = conta.depositar(self.valor)

        if transacao_aceita:
            conta.historico.adicionar_transacao(self)