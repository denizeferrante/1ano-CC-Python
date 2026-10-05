endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0])

# Verificando se é SUCESSO

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(eh_sucesso(401))

# FUNÇÃO que verifica se tem codigos de req com erros seguidos em UM endpoint
# [201, 500, 502, 201, 500] => lista_status
def tem_erro_seguido(lista_status):
    for i in range(len(lista_status) - 1):
        codigo_atual = lista_status[i]
        prox_codigo = lista_status[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True

    return False

# print(tem_erro_seguido(status[2]))

# ANALISAR COMPLETAMENTE UM ENDPOINT
# [201, 500, 502, 201, 500] => lista_status
def analisar_endpoint(lista_status):
    qtd_sucessos = 0

    for codigo in lista_status:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_requisicoes = len(lista_status)
    qtd_erros = qtd_requisicoes - qtd_sucessos

    percentual_sucesso = (qtd_sucessos / qtd_requisicoes) * 100

    tem_erros_seguidos = tem_erro_seguido(lista_status)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (
        qtd_sucessos, qtd_erros, percentual_sucesso, classificacao
    )

# PERCORRENDO A MATRIZ...
maior_qtd_erros = -1
endpoint_mais_erros = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    status_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(status_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Códigos HTTP: {status_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual:.1f}%")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_mais_erros = nome_endpoint

print(f"Endpoint com mais erros: {endpoint_mais_erros} ({maior_qtd_erros})")

