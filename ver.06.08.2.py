from enum import Enum

class TipoQuarto(Enum):
    PRESIDENCIAL = 1
    SUITE = 2
    DUPLA = 3
    SIMPLES = 4

class Status (Enum):
    DISPONIVEL = 1
    RESERVADO = 2
    LIMPEZA = 3
    OCUPADO = 4

class Reserva:
    def __init__(self, tipo, status=Status.DISPONIVEL):
        self._tipo = tipo
        self._status = status

    def mudaStatus(self, novo_status):
        try:
            if self._status == Status.DISPONIVEL:
                self._status = Status.DISPONIVEL
                print(f"O quarto {TipoQuarto} teve seu status mudado para {novo_status}")
                self._status = novo_status
            else:
                print(f"O quarto {TipoQuarto} está {self._status}")
            
        except ValueError as e:
            print(f"Info: {e}")
            return None
        
        finally:
            print("Fim da execução!")

quarto1 = Reserva("Presidencial", Status.DISPONIVEL)
print(quarto1._status)
print("Ola mundo")
quarto1.mudaStatus(Status.LIMPEZA)
print(quarto1._status)