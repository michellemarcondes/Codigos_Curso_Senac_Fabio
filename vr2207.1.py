import hashlib

# funcionario--Atributos: Nome; Cargo; Salario; Lotação.--Ações: Consultar salario; Consultar lotação e solicitar aumento
class Funcionario:
    def __init__(self, nome, cargo, salario, lotacao):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__lotacao = lotacao

    def get_salario(self):  # retorna o salario quando solicitado
        return self.__salario

    def get_lotacao(self):  # retorna a lotação quando solicitado
        return self.__lotacao

    def get_nome(self):  # retorna o nome quando solicitado
        return self.__nome

    def get_cargo(self):  # retorna o cargo quando solicitado
        return self.__cargo
    
    def detalhes_funcionario(self):
        print(f'nome: {self.__nome}')
        print(f'Cargo: {self.__cargo}')
        print(f'Salario: {self.__salario}')
        print(f'Lotação: {self.__lotacao}')

    def set_aumento(self):  # Solicitação de aumento
        pass  # escrever aqui dps

# Classe gerente
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, lotacao):
        super().__init__(nome, cargo, salario * 2, lotacao)
        self.funcionarios = []

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.get_nome()} foi contratado(a) como {funcionario.get_cargo()}.")

    def demitir(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f"{funcionario.get_nome()} foi demitido(a) do cargo de {funcionario.get_cargo()}.")
        else:
            print(f"{funcionario.get_nome()} não está na lista de funcionários.")

# Exemplo de uso
funcionario1 = Funcionario("João", "Analista", 3000, "Financeiro")
funcionario2 = Funcionario("Ana", "Assistente", 2000, "Recursos Humanos")
gerente1 = Gerente("Maria", "Gerente", 3000, "Financeiro")

gerente1.contratar(funcionario1)
gerente1.contratar(funcionario2)
print([f"{f.get_nome()} ({f.get_cargo()})" for f in gerente1.funcionarios])

gerente1.demitir(funcionario1)
print([f"{f.get_nome()} ({f.get_cargo()})" for f in gerente1.funcionarios])

print(funcionario1.detalhes_funcionario())
