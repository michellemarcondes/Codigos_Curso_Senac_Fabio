class funcionario:
    salario_base = 1000.00

    def __init__(self, nome, cargo, salario, lotacao):
        self._nome = nome
        self._cargo = cargo
        self._salario = funcionario.salario_base
        self._lotacao = lotacao

    def set_nome(self, nome):
        self._nome = nome

    def set_cargo(self, cargo):
        self._cargo = cargo

    def set_lotacao (self, lotacao):
        self._lotacao = lotacao

    def set_salario(self, salario):
        self._salario = salario

    def ver_salario(self):
        return self._salario
    
    def ver_lotacao(self):
        return self._lotacao
    
    def pedir_aumento(self):
        return "Solicitação realizada com sucesso!"
    

class gerente(funcionario):
    def __init__(self, nome, lotacao):
        super().__init__(nome, "gerente", lotacao)

        self._salario = funcionario.salario_base * 2 

    def demitir_func(self, funcionario):
        return f"O funcionario {funcionario get_name()} foi demitido"

    def contratar_func(self, nome, cargo, lotacao):
        return funcionario (nome, cargo, lotacao)
    
    def altera_lotacao (self, funcionario, novalotacao):
        return funcionario.set_lotacao(novalotacao)
    

class diretor(funcionario):
    def __init__(self, nome, lotacao):
        super().__init__(nome, "diretor", lotacao)

        self._salario = funcionario.salario_base * 3
    
    def contratar_fun(self, nome, cargo, lotacao):
        if cargo.lower() == "gerente":
            return funcionario(nome, cargo, lotacao)
        else:
            return "Diretor só contrata gerente"
        
    def aumetar_salario(self, funcionario, aumento):
        novo_salario = funcionario.set_salario + aumento
        funcionario.set_salario(novo_salario)    
        return f"O funcionario {funcionario.get_nome()} teve seu salario aumentado para {novo_salario}"
    


