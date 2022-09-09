#!/usr/bin/python3

import sys
import datetime as dt

otimo = {
    'custo': int(99999),
    'melhores_atores' : []
}

# Vetor com todos os atores disponiveis
Atores_disponiveis = []

# Vetor com os atores escolhidos
Atores_escolhidos = []

# Numero de grupos (l = |S|)
l = 0
# Numero de atores (m = |A|)
m = 0
# Numero de personagens (n = |P|)
n = 0

# Nodos visitados na árvore
nodos = 0

# Função bound, pode ser a nossa ou a dos professores
bound = 0

def custo(atores):

    global valores

    sum = 0

    for ator in atores:
        sum += int(valores[ator])

    return sum


def B_dada(pos, atores):

    global valores

    result = custo(atores)

    # indice do ator mais barato no vetor de atores disponiveis
    index_min = valores.index(min(valores))

    # Pega o ator mais barato, multiplica pelo numero de papeis que falta preecher
    # E soma ao valor total dos atores
    result +=  (n - len(atores)) * valores[index_min]
    
    return result


def viavel(pos, atores):
    global grupos, n

    # print("escolhidos: ", E, "disponiveis: ", F)
    representados = set()
    for ator in atores:
        for grupo in grupos[ator]:
            representados.add(grupo)

    # print("representados: ", representados)

    nao_representados = set()
    for ator in range(i, len(grupos)):
        for grupo in grupos[ator]:
            nao_representados.add(grupo)
    
    # print("nao representados: ", nao_representados)

    if len(representados.union(nao_representados)) != l and f == 0:
        print("1: ", len(representados.union(nao_representados)))
        return False

    # REVISAR
    if len(atores)+len(grupos)-pos < n:
        return False

    if len(atores) > n:
        return False

    return True

def elenca(pos=0, atores=[]):
    global nodos, n
    
    # Visitamos mais um nodo
    nodos += 1

    # Caso base 1: inviável
    if not viavel(pos, atores):
        return

    # Caso base 2: se preenchemos o vetor de escolhidos e é viável
    if len(atores) == n: 
        custo_local = custo(atores)
        if (custo_local < otimo['custo']) and o == 0:
            otimo['custo'] = custo_local
            otimo['melhores_atores'] = atores
        return
    
    bound_prox = bound(pos+1, atores)
    bound_atual = bound(pos+1, atores+[pos])
    if min(bound_atual, bound_prox) >= otimo["custo"]:
        return
    if bound_atual < bound_prox:
        elenca(pos+1, atores+[pos])
        if bound_prox < otimo["custo"]:
            elenca(pos+1, atores)
    else:
        elenca(pos+1, atores)
        if bound_atual < otimo["custo"]:
            elenca(pos+1, atores+[pos])   

    
if __name__ == "__main__":
    f = o = a = 0

    # Indentificando flags para a execução do Branch & Bound
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == '-f':
                f = 1
            elif sys.argv[i] == '-o':
                o = 1
            elif sys.argv[i] == '-a':
                a = 1
    
    # -f = desligar os cortes de viabilidade
    # -o = desligar os cortes de otimalidade
    # -a = usar a função limitante dada pelos professores

    # bound = B_nossa
    if a == 1:
        bound = B_dada

    # Lendo numero de representações, atores e papeis 
    entrada = [int(x) for x in sys.stdin.read().split()]
    l = entrada[0] # numero de grupos sociais
    m = entrada[1] # numero de atores
    n = entrada[2] # numero de personagens
    # l = |S|, m = |A| e n = |P| 

    indexador = 3

    valores = []
    grupos = []
    # Lendo atores e suas caracteristicas
    for _ in range(m):
        valores.append(entrada[indexador])
        n_grupos = entrada[indexador+1]
        gps = []

        for i in range(n_grupos):
            gps.append(entrada[indexador+2+i])
        grupos.append(gps)
        indexador += n_grupos+2

    # ------------------------CODIGO PRINCIPAL AQUI-------------------------------

    tempo_inicio = dt.datetime.now()
    elenca()
    tempo_total = dt.datetime.now() - tempo_inicio

    if otimo['custo'] == int(99999):
        print('Inviavel')
    else:
        print('Número de nós na árvore da solução:', nodos, file=sys.stderr)
        print('Tempo de execução:', tempo_total, file=sys.stderr)
        for ator in otimo['melhores_atores'][:-1]:
            print(ator+1, end=' ')
        print(otimo['melhores_atores'][-1]+1)
        print(otimo['custo'])

    # ----------------------------------------------------------------------------