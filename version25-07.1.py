class Funcionario:
    def __init__(self, nome, senha, cargo, salario, lotacao):
        self.__nome = nome
        self.__senha = senha
        self.__cargo = cargo
        self.__salario = salario
        self.__lotacao = lotacao

    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

    def get_cargo(self):
        return self.__cargo

    def get_salario(self):
        return self.__salario

    def get_lotacao(self):
        return self.__lotacao

    def solicitar_aumento(self):
        print(f"{self.__nome} solicitou um aumento.")

    def detalhes(self):
        return f"Nome: {self.__nome}, Cargo: {self.__cargo}, Salário: {self.__salario}, Lotação: {self.__lotacao}"


class Gerente(Funcionario):
    def __init__(self, nome, senha, cargo, salario, lotacao):
        super().__init__(nome, senha, cargo, salario * 2, lotacao)
        self.funcionarios = []

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.get_nome()} foi contratado(a) como {funcionario.get_cargo()}.")

    def demitir(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f"{funcionario.get_nome()} foi demitido(a).")
        else:
            print(f"{funcionario.get_nome()} não está na lista de funcionários.")

    def alterar_lotacao(self, funcionario, nova_lotacao):
        funcionario._Funcionario__lotacao = nova_lotacao
        print(f"A lotação de {funcionario.get_nome()} foi alterada para {nova_lotacao}.")


class Diretor(Gerente):
    def __init__(self, nome, senha, cargo, salario, lotacao):
        super().__init__(nome, senha, cargo, salario * 3, lotacao)
        self.gerentes = []

    def contratar(self, gerente):
        self.gerentes.append(gerente)
        print(f"{gerente.get_nome()} foi contratado(a) como {gerente.get_cargo()}.")

    def demitir(self, gerente):
        if gerente in self.gerentes:
            self.gerentes.remove(gerente)
            print(f"{gerente.get_nome()} foi demitido(a).")
        else:
            print(f"{gerente.get_nome()} não está na lista de gerentes.")

    def aprovar_aumento(self, funcionario, percentual):
        novo_salario = funcionario.get_salario() * (1 + percentual / 100)
        print(f"Aumento aprovado para {funcionario.get_nome()}. Novo salário: {novo_salario}.")
        funcionario._Funcionario__salario = novo_salario

    def mudar_salario(self, funcionario, novo_salario):
        funcionario._Funcionario__salario = novo_salario
        print(f"O salário de {funcionario.get_nome()} foi alterado para {novo_salario}.")


def menu_funcionario(funcionario):
    while True:
        print("\nMenu Funcionario")
        print("1. Consultar Salário")
        print("2. Consultar Lotação")
        print("3. Solicitar Aumento")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Salário: {funcionario.get_salario()}")
        elif escolha == "2":
            print(f"Lotação: {funcionario.get_lotacao()}")
        elif escolha == "3":
            funcionario.solicitar_aumento()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_gerente(gerente):
    while True:
        print("\nMenu Gerente")
        print("1. Consultar Salário")
        print("2. Consultar Lotação")
        print("3. Solicitar Aumento")
        print("4. Demitir Funcionário")
        print("5. Contratar Funcionário")
        print("6. Alterar Lotação")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Salário: {gerente.get_salario()}")
        elif escolha == "2":
            print(f"Lotação: {gerente.get_lotacao()}")
        elif escolha == "3":
            gerente.solicitar_aumento()
        elif escolha == "4":
            nome_funcionario = input("Nome do funcionário a demitir: ")
            funcionario = next((f for f in gerente.funcionarios if f.get_nome() == nome_funcionario), None)
            if funcionario:
                gerente.demitir(funcionario)
            else:
                print("Funcionário não encontrado.")
        elif escolha == "5":
            nome_funcionario = input("Nome do novo funcionário: ")
            senha_funcionario = input("Senha do novo funcionário: ")
            cargo_funcionario = input("Cargo do novo funcionário: ")
            salario_funcionario = float(input("Salário do novo funcionário: "))
            lotacao_funcionario = input("Lotação do novo funcionário: ")
            novo_funcionario = Funcionario(nome_funcionario, senha_funcionario, cargo_funcionario, salario_funcionario, lotacao_funcionario)
            gerente.contratar(novo_funcionario)
        elif escolha == "6":
            nome_funcionario = input("Nome do funcionário: ")
            nova_lotacao = input("Nova lotação: ")
            funcionario = next((f for f in gerente.funcionarios if f.get_nome() == nome_funcionario), None)
            if funcionario:
                gerente.alterar_lotacao(funcionario, nova_lotacao)
            else:
                print("Funcionário não encontrado.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_diretor(diretor):
    while True:
        print("\nMenu Diretor")
        print("1. Consultar Salário")
        print("2. Consultar Lotação")
        print("3. Aprovar Aumento")
        print("4. Demitir Gerente")
        print("5. Contratar Gerente")
        print("6. Mudar Salário")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Salário: {diretor.get_salario()}")
        elif escolha == "2":
            print(f"Lotação: {diretor.get_lotacao()}")
        elif escolha == "3":
            nome_funcionario = input("Nome do funcionário: ")
            percentual = float(input("Percentual de aumento: "))
            funcionario = next((f for f in diretor.funcionarios if f.get_nome() == nome_funcionario), None)
            if funcionario:
                diretor.aprovar_aumento(funcionario, percentual)
            else:
                print("Funcionário não encontrado.")
        elif escolha == "4":
            nome_gerente = input("Nome do gerente a demitir: ")
            gerente = next((g for g in diretor.gerentes if g.get_nome() == nome_gerente), None)
            if gerente:
                diretor.demitir(gerente)
            else:
                print("Gerente não encontrado.")
        elif escolha == "5":
            nome_gerente = input("Nome do novo gerente: ")
            senha_gerente = input("Senha do novo gerente: ")
            salario_gerente = float(input("Salário do novo gerente: "))
            lotacao_gerente = input("Lotação do novo gerente: ")
            novo_gerente = Gerente(nome_gerente, senha_gerente, "Gerente", salario_gerente, lotacao_gerente)
            diretor.contratar(novo_gerente)
        elif escolha == "6":
            nome_funcionario = input("Nome do funcionário: ")
            novo_salario = float(input("Novo salário: "))
            funcionario = next((f for f in diretor.funcionarios if f.get_nome() == nome_funcionario), None)
            if funcionario:
                diretor.mudar_salario(funcionario, novo_salario)
            else:
                print("Funcionário não encontrado.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def login(usuarios):
    nome = input("Nome: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.get_nome() == nome and usuario.get_senha() == senha:
            return usuario
    return None


def main():
    # Criação dos funcionários
    funcionario1 = Funcionario("Ana", "12345", "Estagiária", 3000, "Financeiro")
    funcionario2 = Funcionario("Maria", "54321", "Contadora", 3000, "Contábil")
    funcionario3 = Funcionario("João", "67890", "Suporte", 3000, "TI")

    # Criação dos gerentes
    gerente1 = Gerente("Rebeca", "09876", "Gerente Geral", 3000, "Financeiro")
    gerente2 = Gerente("Thiago", "senha", "Gerente", 3000, "TI")

    # Criação do diretor
    diretor = Diretor("Michelle", "senha2", "Diretora Geral", 3000, "Administrativo")

    usuarios = [funcionario1, funcionario2, funcionario3, gerente1, gerente2, diretor]

    while True:
        print("\nSistema de Gestão de Funcionários")
        usuario = login(usuarios)
        if usuario:
            if isinstance(usuario, Diretor):
                menu_diretor(usuario)
            elif isinstance(usuario, Gerente):
                menu_gerente(usuario)
            else:
                menu_funcionario(usuario)
        else:
            print("Login ou senha inválidos. Tente novamente.")


if __name__ == "__main__":
    main()
