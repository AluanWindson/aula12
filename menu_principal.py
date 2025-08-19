import runpy

def menu():
    while True:  
        print('\n - Menu de Opções:')
        print('1 - Converter metros para centímetros')
        print('2 - Calcuar area do Círculo')
        print('3 - Calcular área do Quadrado')
        print('0 - Sair')

        opcao = input('\n Escolha uma opção: ')

        if opcao == '1': 
            #runpy.run_path("5.py")
            exec(open("5.py").read())
            print("-")
            """Runpy e o exec cumprem a mesma função, porém, o runpy não executa treads.
            Logo roda com menos problemas e necessidades de manutenção."""

        elif opcao == '2':
            #runpy.run_path("6.py")
            exec(open("6.py").read())
            print("-")
            
        elif opcao == '3':
            #runpy.run_path("7.py")
            exec(open("7.py").read())
            print("-")
            
        elif opcao == '0':
            print("-")
            break
        else:
            print("Opção inválida. Tente novamente.")
            print("-")

#Iniciar Menu
if __name__ == '__main__':
 menu()