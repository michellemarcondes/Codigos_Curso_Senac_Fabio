#enum - Significa fazer a numeração de alguma coisa;
from enum import Enum

class TipoVeiculo(Enum):
    SEDAN = 1
    HATCH = 2
    SUV = 3
    PICKUP = 4

class Status (Enum):
    DISPONIVEL = 1
    LOCADO = 2
    MANUTENCAO = 3
    RESERVADO = 4

class Veiculo:
    def __init__(self, modelo, tipo, status=Status.DISPONIVEL):
        self._modelo = modelo
        self._tipo = tipo
        self._status = status

    def mudaStatus(self, novo_status):
        if isinstance(novo_status,Status):
            self._status = novo_status
        else:
            return ValueError("Status invalido")
        
    def __str__(self):
        return f"veiculo: {self._modelo} Tipo: {self._tipo} Status: {self._status}"
    
veiculo1 =Veiculo ("Uno", TipoVeiculo.HATCH)
print(veiculo1._status)

veiculo1.mudaStatus(Status.RESERVADO)