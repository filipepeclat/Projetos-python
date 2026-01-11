import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#gastos = []

gastos = [
    {"nome": "Aluguel", "valor": 1200},
    {"nome": "Internet", "valor": 100},
    {"nome": "Luz", "valor": 200}
]

def opçoes_iniciais():
    limpar_tela()

    print ('===Controlando o orçamento mensal===')

    print ('\n1. adicionar novo gasto')
    print ('2. remover gasto')
    print ('3. listar gastos')
    print ('4. calcular orçamento')
    print ('5. sair')

    opção = input('\nselecione opção desejada: ')
    return opção

def adicionar():
    while True:
        limpar_tela()
        print ('===Adicionar novo gasto===')
        
        nome = input('\nDigite o nome do gasto: ').strip()
        if not nome:
            print('Nome inválido.')
            input('\nPressione Enter para tentar novamente...')
            continue
        
        try:                
            valor = float(input('Digite seu custo R$ '))
            if valor <=0:
                print('Valor inválido.')
                input('\nPressione Enter para tentar novamente...')
                continue
        except ValueError:
            print('Valor inválido.')
            input('\nPressione Enter para tentar novamente...')
            continue
        
        gastos.append({"nome": nome, "valor": valor})
        print(f"\nRegistrado {nome} com valor de R$ {valor:.2f}")
        input("\nPressione Enter para retornar...")
        break
        
def remover():
    limpar_tela()   
    print ('===Remover gasto===\n')

    if not gastos:
        print ('Não há gastos cadastrados')
        input("\nPressione Enter para continuar...")
        return
    
    for i, gasto in enumerate(gastos, 1):
        print(f'{i}. {gasto["nome"]} - R$ {gasto["valor"]:.2f}')
    
    try:
        indice = int(input('\nQual deseja remover: '))

        if 1 <= indice <= len(gastos):
            removido = gastos.pop(indice -1)
            print(f"\nGasto '{removido['nome']}' removido com sucesso!")

        else:
            print("Índice inválido!")   
            
    except ValueError:
        print('Entrada invalida')
    input("\nPressione Enter para continuar...")

def listar():
    limpar_tela()   
    
    print ('===Lista de gastos===\n')
    if not gastos:
        print ('Não há gastos cadastrados')
        input("\nPressione Enter para retornar...")
        return
    
    for i, gasto in enumerate(gastos, 1):
        print(f'{i}. {gasto["nome"]} - R$ {gasto["valor"]:.2f}')
    input("\nPressione Enter para retornar...")

def calcular():
    limpar_tela()   
    
    print ('===calcular gastos===\n')
    if not gastos:
        print ('Não há gastos cadastrados')
        input("\nPressione Enter para retornar...")
        return
    
    for i, gasto in enumerate(gastos, 1):
        print(f'{i}. {gasto["nome"]} - R$ {gasto["valor"]:.2f}')
    
    try:
        gasto_total = float(input('\nDefina o gasto total pretendido em R$: '))
        if gasto_total <= 0:
            raise ValueError
    except ValueError:
        print('Valor inválido!')
        input("\nPressione Enter para retornar...")
        return

    total_gastos = sum(gasto["valor"] for gasto in gastos)
    valor_restante = gasto_total - total_gastos

    print(f"\nTotal gasto: R$ {total_gastos:.2f}")
    print(f"Orçamento definido: R$ {gasto_total:.2f}")

    if valor_restante >= 0:
        print('Seus gastos estão dentro da margem estipulada')
        print(f'Sobra: R$ {valor_restante:.2f}')
    else:
        print('Seus gastos superam o estipulado')
        print(f'Excesso: R$ {abs(valor_restante):.2f}')

    input("\nPressione Enter para continuar...")

def main():
    while True:
        opcao = opçoes_iniciais()
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            remover()
        elif opcao == '3':
            listar()
        elif opcao == '4':
            calcular()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            input("\nPressione Enter para continuar...")


if __name__ == '__main__':
    main()       
