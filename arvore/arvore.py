from no import No

def inserir(raiz: No, valor: int) -> No:
    if raiz is None:
        return No(valor)
    
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    elif valor > raiz.valor:
        raiz.direita = inserir(raiz.direita, valor)

    return raiz

def buscar(raiz: No, valor: int) -> No:
    if raiz is None or raiz.valor == valor:
        return raiz
    if valor < raiz.valor:
        return buscar(raiz.esquerda, valor)
    else:
        return buscar(raiz.direita, valor)
    
def imprimir_arvore(raiz: No, espaco: int = 0) -> None:
    if raiz is not None:
        imprimir_arvore(raiz.direita, espaco + 10)

        print(' ' * espaco + str(raiz.valor))
        print('')

        imprimir_arvore(raiz.esquerda, espaco + 10)

def tamanho(raiz: No) -> int:
    if raiz is None:
        return 0
    return 1 + tamanho(raiz.esquerda) + tamanho(raiz.direita)

def numero_folhas(raiz: No) -> int:
    if raiz is None:
        return 0

    if raiz.esquerda is None and raiz.direita is None:
        return 1
    
    return numero_folhas(raiz.esquerda) + numero_folhas(raiz.direita)

if __name__ == "__main__":
    raiz = None

    n_valores = int(input('Informe a quantidade de valores a ser digitada:'))
    for _ in range(n_valores):
        valor = int(input('Informe o valor: '))
        raiz = inserir(raiz, valor)

    print("Impressão em ordem da árvore binária:")
    imprimir_arvore(raiz)

    valor_buscado = int(input('Informe um valor para a busca:'))
    no_buscado = buscar(raiz, valor_buscado)
    if no_buscado:
        print(f"\nValor {valor_buscado} encontrado!")
    else:
        print(f"\nValor {valor_buscado} não encontrado!")
    
    print('Número de Nós: ', tamanho(raiz))
    print('Número de folhas: ',numero_folhas(raiz))
