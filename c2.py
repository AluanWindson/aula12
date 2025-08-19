class Carro:
    def __init__(self, modelo, ano, placa, montadora):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.montadora = montadora
    
    def acelerar(self):
     print(f'{self.modelo} está acelerando...')
     print('-')

# Criando os objetos fora da classe
c1 = Carro('Honda Civic', '2021', 'PCX-205H', 'Hyundai')
print('Modelo:', c1.modelo)
print('Ano:', c1.ano)
print('Placa:', c1.placa)
print('Montadora:', c1.montadora)
print('-')

c2 = Carro('Sandero', '2014', 'LLO-3475', 'Renault')
print('Modelo:', c2.modelo)
print('Ano:', c2.ano)
print('Placa:', c2.placa)
print('Montadora:', c2.montadora)
print('-')

# Criando mais carros
fusca = Carro('Fusca', '1984', 'AAA-1234', 'Volkswagen')
print("Modelo: ", fusca.modelo)
fusca.acelerar()

byd = Carro('BYD Dolphin', '2024', 'BYD-5678', 'BYD')
print("Modelo: ", byd.modelo)
byd.acelerar()
