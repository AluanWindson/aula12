#Classe é onde vai ser gerado o objteto

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

p1 = Pessoa('Andre','Marques','30')
print('Nome:', p1.nome)
print('Sobrenome:', p1.sobrenome)
print('Idade:', p1.idade)
print('-')

p2 = Pessoa('Gilmar', 'Santos', '35')
print('Nome:', p2.nome)
print('Sobrenome:', p2.sobrenome)
print('Idade:', p2.idade)
print('-')