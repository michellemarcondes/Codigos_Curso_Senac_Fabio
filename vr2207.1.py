import hashlib


# Classe Funcionario
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


    def detalhes(self):
        print(f'Nome: {self.__nome}')
        print(f'Cargo: {self.__cargo}')
        print(f'Salário: {self.__salario}')
        print(f'Lotação: {self.__lotacao}')


    def solicitar_aumento(self, gerente, percentual):
        gerente.processar_pedido_aumento(self, percentual)


    def set_aumento(self, percentual):
        self.__salario += self.__salario * (percentual / 100)
        print(f"O salário de {self.__nome} foi aumentado para {self.__salario}.")


# Classe Gerente
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


    def detalhes(self):
        super().detalhes()
        print(f'Número de funcionários: {len(self.funcionarios)}')


    def processar_pedido_aumento(self, funcionario, percentual):
        if funcionario in self.funcionarios:
            funcionario.set_aumento(percentual)
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


print("Detalhes do gerente:")
gerente1.detalhes()


# Funcionário solicitando aumento
funcionario2.solicitar_aumento(gerente1, 10)
funcionario2.detalhes()



#ideia: criar menu com senha, ou seja, Menu: nome, cargo e senha; conferir se a senha bate e então acessar o menu correspondente. Funcionarios o menu tem: Consultar salario, consultar lotação e solicitar aumento.
# No menu de gerente tem as funções: consultar salario, consulatr lotação, solicitar aumento, demitir e contratar.
#No menu de diretor tem as funções: consultar salario, consultar lotação, Aprovar o aumento de salario, demitir e contratar gerente