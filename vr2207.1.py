import hashlib

#funcionario--Atributos: Nome; Cargo; Salario; Lotação.--Ações: Consultar salario; Consultar lotação e solicitar aumento
class funcionario:
        def __init__(self, nome, cargo, salario, lotacao):
            self.__nome = nome
            self.__cargo = cargo
            self.__salario = salario
            self.__lotacao = lotacao

        def get_salario(self):#retorna o salario quando solicitado
            return self.__salario

        def get_lotacao(self):#retorna a lotação quando solicitado
            return self.__lotacao

        def set_aumento(self):#Solicitação de aumento
             #escrever aqui dps
        
#Classe gerente
class gerente(funcionario):
     def __init__(self, nome, cargo, salario, lotacao):
          super().__init__(self, nome, cargo, salario*2, lotacao)
          self.funcionarios = []
     
     def contratar(self, funcionario):
          self.funcionarios.append(funcionario)
          print(f"{funcionario.nome} foi contratado(a) como {funcionario.cargo}.")

    def demitir(self, funcionario):
     if funcionario in self.funcionarios:
          print(f"{funcionario.nome} foi demitido(a) do cargo de {funcionario.cargo}.")
        else:
          print(f"{funcionario.nome} não esta na lista de funcionarios.")


funcionario1 = funcionario("João", "Analista", 3000, "financeiro")
funcionario2 = funcionario("ana", "assistente", 3000, "Recursos humanos")
gerente1 = gerente ("Maria", "gerente", 3000, "financeiro")

gerente.contratar(funcionario1)
gerente.contratar(funcionario2)
print(gerente.funcionarios)

