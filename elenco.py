#!/usr/bin/python3

# Autores: 
# Anderson Aparecido do Carmo Frasão GRR20204069
# Richard Fernando Heise Ferreira GRR20191053

import sys
import datetime as dt

otimo = {
    'custo': float("inf"),
    'melhores_atores' : []
}

# Numero de grupos (l = |S|)
l = 0
# Numero de atores (m = |A|)
m = 0
# Numero de personagens (n = |P|)
n = 0

# Número de cortes por otimalidade
cortes_otimalidade = 0

# Número de cortes por viabilidade
cortes_viabilidade = 0

# Nodos visitados na árvore
nodos = 0

# Função bound, pode ser a nossa ou a dos professores
bound = 0

# Função que calcula custo de atores
def custo(atores):
    global valores

    sum = 0

    for ator in atores:
        sum += int(valores[ator])

    return sum

# Bound guloso feito por nós
def B_nossa(pos, atores):
    global valores, n
    
    # pega o custo dos atores escolhidos
    result = custo(atores)

    # pega os demais atores possíveis
    candidatos = valores.copy()[pos:]

    # ordena os custos
    candidatos.sort()

    # remove os mais caros
    candidatos = candidatos[:n-len(atores)] 
    
    # retorna o custo dos escolhidos + a soma dos mais baratos
    return result + sum(candidatos)

# Bound fornecido pelos professores
def B_dada(pos, atores):
    global valores, n

    # Custo dos atores escolhidos
    result = custo(atores)

    valores_n_escolhidos = valores.copy()[pos:]

    if (len(valores_n_escolhidos)):
        # indice do ator mais barato no vetor de atores disponiveis
        index_min = valores.index(min(valores_n_escolhidos))
        # Pega o ator mais barato, multiplica pelo numero de papeis que falta preecher
        # E soma ao valor total dos atores
        result +=  (n - len(atores)) * valores[index_min]
    
    return result

# Função que testa viabilidade
def viavel(pos, atores, primeiro):
    global grupos, n

    if (len(grupos) <= pos and len(atores) < n):
        return False

    if (f == 0 or primeiro == 1):
        # Conjunto de grupos representados
        representados = set()
        for ator in atores:
            for grupo in grupos[ator]:
                representados.add(grupo)

        # Conjunto de grupos ainda não representados
        nao_representados = set()
        for ator in range(pos, len(grupos)):
            for grupo in grupos[ator]:
                nao_representados.add(grupo)
        
        # não representamos todos os grupos
        if len(representados.union(nao_representados)) != l:
            return False

        # número de atores escolhidos e grupos restantes não cobrirá número de papeis
        if len(atores)+len(grupos)-pos < n:
            return False

        # escolhi mais que papeis disponíveis
        if len(atores) > n:
            return False
            
    return True

# Resolve melhor elenco
def elenca(pos=0, atores=[], primeiro=1):
    global nodos, n, o, f, cortes_otimalidade, cortes_viabilidade
    
    if (v == 1):
        print("elenca(", pos, ",", atores, ")")
    # Visitamos mais um nodo
    nodos += 1

    # Caso base 1: inviável
    if not viavel(pos, atores, primeiro):
        return

    # Caso base 2: verificamos todos os atores
    if pos == m: 
        custo_local = custo(atores)
        if (custo_local < otimo['custo']):
            otimo['custo'] = custo_local
            otimo['melhores_atores'] = atores
        return
    

    # Se vamos cortar por viabilidade
    if (f == 0):
        
        # Se vamos cortar por otimalidade
        if (o == 0):
            
             # Bound atual
            bound_ignora = bound(pos+1, atores)

            # Bound do próximo nodo
            bound_pega = bound(pos+1, atores+[pos])

            # Se o bound do próximo for menor que o atual, pegamos o próximo
            if bound_pega < bound_ignora:

                # Corte por viabilidade
                if (viavel(pos+1, atores+[pos], 0)):
                    elenca(pos+1, atores+[pos], 0)
                else:
                    cortes_viabilidade += 1

                # Corte de otimalidade
                if bound_ignora < otimo["custo"]:

                    # Corte por viabilidade
                    if (viavel(pos+1, atores, 0)):
                        elenca(pos+1, atores, 0)
                    else:
                        cortes_viabilidade += 1
                else:
                    cortes_otimalidade += 1

                    
            else:
                if (viavel(pos+1, atores, 0)):
                        elenca(pos+1, atores, 0)
                else:
                    cortes_viabilidade += 1

                if bound_pega < otimo["custo"]:
                    if (viavel(pos+1, atores+[pos], 0)):
                        elenca(pos+1, atores+[pos], 0)  
                    else:
                        cortes_viabilidade += 1

                else:
                    cortes_otimalidade += 1

        # Não vamos cortar por otimalidade
        else:

            # Corte por viabilidade
            if (viavel(pos+1, atores, 0)):
                    elenca(pos+1, atores, 0)
            else:
                cortes_viabilidade += 1

            # Corte por viabilidade
            if (viavel(pos+1, atores+[pos], 0)):
                    elenca(pos+1, atores+[pos], 0)  
            else:
                cortes_viabilidade += 1

    # Se não vamos cortar por viabilidade
    else:

        # Se não vamos cortar por otimalidade
        if (o == 0):

             # Bound atual
            bound_ignora = bound(pos+1, atores)

            # Bound do próximo nodo
            bound_pega = bound(pos+1, atores+[pos])
            
            if bound_pega < bound_ignora:
                elenca(pos+1, atores+[pos], 0)
                if bound_ignora < otimo["custo"]:
                    elenca(pos+1, atores, 0)
                else:
                    cortes_otimalidade += 1
                    
            else:
                elenca(pos+1, atores, 0)
                if bound_pega < otimo["custo"]:
                    elenca(pos+1, atores+[pos], 0)  
                else:
                    cortes_otimalidade += 1
        else:

            # Se não vamos cortar por otimalidade nem viabilidade
            elenca(pos+1, atores, 0)
            elenca(pos+1, atores+[pos], 0) 
    
if __name__ == "__main__":
    f = o = a = v = 0

    # Indentificando flags para a execução do Branch & Bound
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == '-f':
                f = 1
            elif sys.argv[i] == '-o':
                o = 1
            elif sys.argv[i] == '-a':
                a = 1
            elif sys.argv[i] == '-v':
                v = 1
    
    # -f = desligar os cortes de viabilidade
    # -o = desligar os cortes de otimalidade
    # -a = usar a função limitante dada pelos professores

    # default é nossa
    bound = B_nossa
    if a == 1:
        # dos professores
        bound = B_dada

    # Lendo numero de representações, atores e papeis 
    entrada = [int(x) for x in sys.stdin.read().split()]
    l = entrada[0] # numero de grupos sociais
    m = entrada[1] # numero de atores
    n = entrada[2] # numero de personagens
    # l = |S|, m = |A| e n = |P| 

    # Leitor de entrada
    indexador = 3
    valores = []
    grupos = []

    # Lendo atores e suas caracteristicas
    for lixo in range(m):
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

    if otimo['custo'] == float("inf"):
        print('Inviavel')
    elif v == 1:
        print('Número de nós visitados na árvore da solução:', nodos, file=sys.stderr)
        print('Tempo de execução:', tempo_total, file=sys.stderr)
        print('Cortes por otimalidade: ', cortes_otimalidade, file=sys.stderr)
        print('Cortes por viabilidade: ', cortes_viabilidade, file=sys.stderr)
        for ator in otimo['melhores_atores'][:-1]:
            print(ator+1, end=' ')
        print(otimo['melhores_atores'][-1]+1)
        print(otimo['custo'])
    else:
        print(nodos, file=sys.stderr)
        print(tempo_total, file=sys.stderr)
        for ator in otimo['melhores_atores'][:-1]:
            print(ator+1, end=' ')
        print(otimo['melhores_atores'][-1]+1)
        print(otimo['custo'])

    # ----------------------------------------------------------------------------