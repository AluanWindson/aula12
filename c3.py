#Criando classe

class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def comer(self):
     print(f'{self.nome} está comendo...')

a1 = Animal('Gato','5kg','2 anos')
print('Nome:', a1.nome)
print('Peso:', a1.peso)
print('Idade:', a1.idade)
print('-')

a2 = Animal('Cachorro', '20kg', '5 anos')

print('Nome:', a2.nome)
print('Peso:', a2.peso)
print('Idade:', a2.idade)
print('-')

a3 = Animal('Rato','1kg','8 meses')

print('Nome:', a3.nome)
print('Peso:', a3.peso)
print('Idade:', a3.idade)
print('-')
