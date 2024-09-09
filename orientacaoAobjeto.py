import hashlib
# encapsulamento
class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = self.hash_senha(senha)
        self.__ativo = False

    def hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_email(self, email):
        self.__email = email
    
    def get_mail(self):
        return self.__email
    
    def alterar_senha(self, senha_antiga, senha_nova):
        if self.verifica_senha(senha_antiga):
            self.__senha = self.hash_senha(senha_nova)
            print(f"sua senha foi alterada")
    
    def verifica_senha(self, senha):
        return self.__senha == self.hash_senha(senha)
    
    def get_senha(self):
        return self.__senha
    
    def ativar(self):
        self.__ativo = True
        print(f"Usúario {self.__nome} foi ativado")
    
    def desativar(self):
        self.__ativo = False
        print(f"Usúario {self.__nome} foi desativado")
    
    def get_ativo(self):
        return self.__ativo
    
    def detalhes_usuario(self):
        print(f'nome: {self.__nome}')
        print(f'email: {self.__email}')
        print(f'ativo: {self.__ativo}')
        print(f'senha: {self.__senha}')

user1 = Usuario("Terebentina Teles", "tere@mail.com.br", "123456")

try:
    print(user1.__nome)

except AttributeError as e: 
    print(f'Erro: {e}')

print(user1.get_nome())
print(user1.get_senha())
print(user1.get_mail())