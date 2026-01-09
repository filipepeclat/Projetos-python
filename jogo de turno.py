import os
import random


def limpar_tela(): #assinatura de função
    os.system('cls')

def tela_inicial():        
    limpar_tela()
    print(' ==========================')
    print('       Lords of sand')
    print(' ==========================')

def opções_iniciais(): 
    print('\n1 - Novo jogo')
    print('2 - Sair')           
    return input('\n> Escolha uma opção: ') #return encerra a função e retorna (entrega) o que é indicado em seguida (no caso a opção)

# CRIAÇÃO DE PERSONAGEM

def transiçao_novo_jogo():
    limpar_tela()
    print('O sol queima a areia.'
    '\nO cheiro de sangue e ferro ainda paira no ar.'
    '\nVocê foi acorrentado, vendido… e jogado aqui.'
    '\nA multidão grita por morte.'
    '\nO imperador observa em silêncio.')
    input('\nO aço será seu juiz. Pressione ENTER para continuar...')

    jogador = criar_personagem()
    inimigo = criar_inimigo()
    return jogador, inimigo

def criar_personagem():
    limpar_tela()
    nome = str(input('digite seu nome: '))
    
    while True:
        limpar_tela()
        print(f'{nome} Escolha sua classe: ')
        print('\n1 - Guerreiro')
        print('2 - Arqueiro')           
        opçao = input('\n> Escolha uma opção: ')
        if opçao == '1':
            return {
                "nome": nome,
                "classe": "Guerreiro",
                "vida": 100,
                "vida_max": 100,
                "ataque": 10,
                "defesa": 5,
                "ouro": 0
                    }

        elif opçao == '2':
            return {
            "nome": nome,
            "classe": "Arqueiro",
            "vida":50,
            "vida_max": 50,
            "ataque": 20,
            "defesa": 3,
            "ouro": 0
            }
    
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione ENTER para tentar novamente.')

# REGRAS DO JOGO
def aplicar_dano (personagem, dano):
    personagem ['vida'] -= dano
    if personagem['vida'] < 0:
        personagem['vida'] = 0

def aplicar_cura (personagem, cura):
    personagem ['vida'] += cura
    if personagem ['vida'] > personagem ['vida_max']:
        personagem['vida'] = personagem['vida_max']

# EVENTOS
def evento_dano (personagem):
    dano = random.randint(1, 20)
    personagem['vida'] -=dano
    print(f'Você sofre {dano} de dano!')
    aplicar_dano(personagem, dano)


def evento_ganhar_ouro (personagem):
    ganho = random.randint(10, 30)
    personagem['ouro'] += ganho
    print(f'Você encontra {ganho} moedas de ouro!')


def evento_recuperar_vida (personagem):
    cura = random.randint(5, 15)
    print(f'Você recupera {cura} de vida.')
    aplicar_cura(personagem, cura)

def evento_fortalecimento(personagem):
    print('A arena o fortalece. Seus atributos aumentam!')
    for atributo in ['ataque', 'defesa']:
        personagem[atributo] += 1

#ação jogador
def escolher_acao_jogador():
    print("\nEscolha sua ação:")
    print('1 - Atacar')
    print('2 - Defender')
    print('3 - Descansar')
    print('4 - Fugir')
    return input("> ")

def aplicar_acao_jogador(jogador, inimigo, escolha):
    if escolha == '1':
        dano = max(0, jogador['ataque'] - inimigo['defesa'])
        aplicar_dano(inimigo, dano)
        print(f"\nVocê atacou {inimigo['nome']} causando {dano} de dano!")
    elif escolha == '2':
        jogador['defesa'] += 5
        print("\nVocê se defendeu! Defesa aumentada neste turno.")
    elif escolha == '3':
        cura = random.randint(10, 20)
        aplicar_cura(jogador, cura)
        print(f"\nVocê descansa e recupera {cura} de vida.")
    elif escolha == '4':
        print("\nVocê fugiu do combate!")
        return 'fugir'
    else:
        print("\nAção inválida! Você perdeu o turno.")

#Sistema de combate 
def criar_inimigo():
    return {
        "nome": "Gladiador",
        "vida": random.randint(50, 100),
        "vida_max": 100,
        "ataque": random.randint(10, 20),
        "defesa": random.randint(3, 8)
    }
def acao_inimigo(inimigo, jogador):
    dano = max(0, inimigo['ataque'] - jogador['defesa'])
    aplicar_dano(jogador, dano)
    print(f"\n{inimigo['nome']} atacou você causando {dano} de dano!")


def mostrar_status(jogador, inimigo):
    print(f"\n--- Status ---")
    print(f"{jogador['nome']} - Vida: {jogador['vida']}/{jogador['vida_max']} | Ataque: {jogador['ataque']} | Defesa: {jogador['defesa']} | Ouro: {jogador['ouro']}")
    print(f"{inimigo['nome']} - Vida: {inimigo['vida']}/{inimigo['vida_max']} | Ataque: {inimigo['ataque']} | Defesa: {inimigo['defesa']}")


def main():
    while True:
        tela_inicial()
        opção = opções_iniciais()
        
        if opção == '1':
            jogador, inimigo = transiçao_novo_jogo()
            limpar_tela()
            print(jogador)
            input('\nPressione ENTER para continuar...')
            limpar_tela()
        
            while jogador['vida'] > 0 and inimigo['vida'] > 0:
                limpar_tela()
                mostrar_status(jogador, inimigo)
                escolha = escolher_acao_jogador()
                
                resultado = aplicar_acao_jogador(jogador, inimigo, escolha)
                if resultado == 'fugir':
                    print("Você fugiu com segurança!")
                    break
                
                if inimigo['vida'] <= 0:
                    print(f"\nVocê derrotou {inimigo['nome']}!")
                    evento_ganhar_ouro(jogador)
                    evento_fortalecimento(jogador)
                    break
                
                acao_inimigo(inimigo, jogador)
                if jogador['vida'] <= 0:
                    print("\nVocê foi derrotado! Fim de jogo.")
                    break
        elif opção == '2':
            print('Saindo do jogo. Até a próxima!')
            break
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar...')

if __name__ == '__main__':
    main()