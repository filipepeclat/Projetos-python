def gatilho_novo_pedido():
    
    print('=== NOVO PEDIDO ===')
    
    pedido = {
        'nome': input('\nNome do cliente: ').strip(),
        'produto': input('Produto: ').strip(),
        'valor': input('Valor do pedido: ').strip() #vem como string
    }
    return pedido

def validar_pedido(pedido):
    
    erros = []

    if not pedido.get('nome'):
        erros.append('Nome do cliente não informado')

    if not pedido.get('produto'):
        erros.append('Produto não informado')

    valor = pedido.get('valor')
    if not valor:
        erros.append('Valor não informado')
    else:
        try:
            pedido['valor'] = float(valor)
            if pedido['valor'] <= 0:
                erros.append('Valor deve ser maior que zero')
        except (ValueError):
            erros.append('Valor inválido')

    return erros

def classificar_pedido(pedido):
    
    valor = pedido['valor']
    
    if valor >= 1000:
        return "ALTO VALOR"
    elif valor >= 300:
        return "MÉDIO VALOR"
    else:
        return "BAIXO VALOR"


def resposta_erro(erros):
   
    print("\n❌ ERROS NO PEDIDO:")
    for erro in erros:
        print(f"- {erro}")

def resposta_sucesso(pedido, classificacao):
    return {
        'status': 'sucesso',
        'cliente': pedido['nome'],
        'produto': pedido['produto'],
        'valor': pedido['valor'],
        'classificacao': classificacao
    }

def executar_fluxo():
    pedido = gatilho_novo_pedido() # 1. Gatilho
    
    erros = validar_pedido(pedido) # 2. Validação

    if erros: # 3. Decisão de fluxo
        resposta_erro(erros)
        return

    classificacao = classificar_pedido(pedido) # 4. Classificação
    
    
    resultado = resposta_sucesso(pedido, classificacao) # 5. Resultado

    print("\n✅ PEDIDO PROCESSADO COM SUCESSO")
    for chave, valor in resultado.items():
        if chave == 'valor':
            print(f"{chave.capitalize()}: R$ {valor:.2f}")
        else:
            print(f"{chave.capitalize()}: {valor}")

if __name__ == "__main__":
    executar_fluxo()
