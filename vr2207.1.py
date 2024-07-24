import hashlib

#funcionario--Atributos: Nome; Cargo; Salario; Lotação.--Ações: Consultar salario; Consultar lotação e solicitar aumento
class funcionario:
        def __init__(self, nome, cargo, salario, lotacao):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__lotacao = lotacao

        def set_nome(self, nome):#Define o nome
            self.__nome = nome

        def set_nome(self, cargo):#Define o cargo
            self.__cargo = cargo

        def set_nome(self, salario):#Define o salario
            self.__salario = salario
        
        def set_nome(self, lotacao):#Define a lotação
            self.__lotacao = lotacao

        def get_salario(self):#retorna o salario quando solicitado
            return self.__salario

        def get_lotacao(self):#retorna a lotação quando solicitado
            return self.__lotacao

        def set_aumento(self):#Solicitação de aumento
             #escrever aqui dps
        
#Classe gerente