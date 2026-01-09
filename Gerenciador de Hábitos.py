import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')#usado dessa forma caso seja rodado no mac onde ao inves de cls é clear

class Habito:
    def __init__(self, nome): #essenciais para o objeto existir, variam de um objeto para outro, definem a identidade inicial do objeto
        self.nome = nome #varia de um objeto para outro, self.nome→ atributo de instância, que é uma variavel que pertence a um objeto/ nome→ uma variável local (variavel que só existe dentro do metodo)/ metodo = função dentro de uma classe.
        self.concluido = False # define o estado por isso f ou v (sempre deve começar igual)

    def concluir(self): #define a ação de concluir
        self.concluido = True #sua função vai ser alterar o estado do concluido

    def __str__(self): #sem o str seriam mostrados apenas codigos
        status = 'V' if self.concluido else 'X' #operador ternário
        return f'{status} {self.nome}'
#Quando uma classe representa dados que precisam ser exibidos para humanos, é necessário definir uma forma explícita de conversão para string (__str__), pois o print por padrão apenas exibe a representação técnica do objeto.

'''
 É equivalente a:
    def __str__(self):
        if self.concluido:
            status = 'V'
        else:
            status = 'X

x = True #funcionamento do verdadeiro e falso, por natureza o if é verdaderiro. 
print('v' if x else 'x') 

--teste 1 --
h1 = Habito("fumar")
print(h1)              # esperado: X Estudar Python

h1.concluir()
print(h1)              # esperado: V Estudar Python
'''

class GerenciadorHabitos:
    def __init__(self): # Aqui é criado um atributo de instância chamado habitos, que referencia uma lista vazia, destinada a armazenar objetos da classe Habito.
        self.habitos = [] #atributo de instância é uma variável que pertence a um objeto específico, não à classe inteira.

    def adicionar(self, nome):
        habito = Habito(nome)# o item da lista abito vai se chamar habito(nome), ou seja (nome)
        self.habitos.append(habito)# self.habitos, ou seja a lista apeend (adiciona) habito, que é (nome)

    def listar(self):
        if not self.habitos: #not iverte o valor logico, ou seja se a lista for falsa ele segue, e o python interpreta lista vazia como falso
            print("Nenhum hábito cadastrado.")
            return #função é encerrar o metodo forçando voltar a pagina incial.
        
        for i, habito in enumerate(self.habitos):   
            print(f'{i + 1}. {habito}')

    def concluir_habito(self, indice):
        self.habitos[indice].concluir()
''' 
i indica a posição que é iniciada por 0, e o enumerete apresenta o número + item.
o i serve mais para o print onde é inficado que seria i+1 a sequencia
'''

'''
--teste 1 --
ger = GerenciadorHabitos()

ger.adicionar("Estudar Python")
ger.adicionar("Beber água")

ger.listar()

ger.habitos[0].concluir()

print("\nDepois de concluir:\n")
ger.listar()
'''
ger = GerenciadorHabitos()

while True:
    limpar_tela()

    print("\n1 - Adicionar hábito")
    print("2 - Listar hábitos")
    print("3 - Concluir hábito")
    print("0 - Sair")

    opçao = input('\nEscolha uma opção: ')

    if opçao == '1':
       nome = input('Nome do habito: ') 
       ger.adicionar(nome)

    elif opçao == '2':      
        ger.listar()
        input("\nPressione ENTER para voltar ao menu...") 

    elif opçao == '3':      
        if not ger.habitos:
            print("Nenhum hábito para concluir.")
            input("\nPressione ENTER para voltar ao menu...") 
            continue #Volta para o início do loop, mantendo a função ativa. mas seria equivalente ao return. pula o resto do loop while e volta para o início, mostrando o menu novamente.

        ger.listar()

        try:
            num = int(input("Número do hábito concluído: ")) #pede ao usuário o número do hábito a concluir.
        except ValueError: #Ma se o usuário digitar algo que não é número, ocorre um ValueError. ex: letras
            print("Digite um número válido.")
            input("\nPressione ENTER para voltar ao menu...") 
            continue

        if 1 <= num <= len(ger.habitos): #É uma forma compacta de verificar duas condições ao mesmo tempo. equivale a: if num >= 1 and num <= len(ger.habitos):
            ger.concluir_habito(num - 1)
            print(f"Hábito {num} concluído!")
            input("\nPressione ENTER para voltar ao menu...")
        #len tem como função indicar quantidade, de listas ou letras em uma string por ex. 
        #ger = GerenciadorHabitos()+habitos = []
        #“Verifique se o número digitado pelo usuário (num) está entre 1 e a quantidade de hábitos cadastrados.”
        #“Se o número estiver correto, chame o método concluir_habito do objeto ger, passando o índice correto da lista, ajustando para o índice do Python com num - 1.”
        else:
            print("Número fora do intervalo.")
            input("\nPressione ENTER para voltar ao menu...")            
        
    elif opçao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida")
        input("\nPressione ENTER para voltar ao menu...")


