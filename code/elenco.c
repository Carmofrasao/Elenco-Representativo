// Anderson Aparecido do Carmo Frasão GRR20194069
// Richard Fernando Heise Ferreira GRR20191053

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int v;
    int s;
    int *S;
} ator;

int l, m, n, *atores_escolhidos;

// Inicializa os vetores
void inicializa(ator * E, int tam){
    for (int i = 0; i < tam; i++){
        E[i].S = NULL;
        E[i].s = 0;
        E[i].v = 0;
    }
}

// Calcula o tamanho da parte preenchida do vetor
int tam(ator * E, int tam){
    int len = 0;
    for (int i = 0; i < tam; i++){
        if (E[i].S == NULL){
            break;
        }
        len++;
    }
    return len;
}

// Calcula o ator mais barato
int min(ator * F, int len){
    int resul = F[0].v;
    int index = 0;
    for (int i = 1; i < len; i++){
        if (F[i].v < resul){
            resul = F[i].v;
            index = i;
        }
    }
    return index;
}

// Função limitante dada pelos professores
int B_dada(ator * E, ator * F){
    int len_F = tam(F, m);
    int len_E = tam(E, n);

    int result = 0;

    // Somatorio dos valores dos atores que ja foram escolhidos
    for (int i = 0; i < len_E; i++){
        result += E[i].v;
    }
    int index_min = min(F, len_F);

    // Pega o ator mais barato, multiplica pelo numero de papeis que falta preecher
    // E soma ao valor total dos atores
    result +=  (n - len_E) * F[index_min].v;

    // Preenchendo o vetor de papeis com a parte do ator mais barato
    for (int i = len_E; i < n; i++){
        atores_escolhidos[i] = index_min+1;
        E[i].v = F[index_min].v;
        E[i].s = F[index_min].s;
        E[i].S = (int *)calloc(E[i].s, sizeof(int));
        for (int u = 0; u < E[i].s; u++){
            E[i].S[u] = F[index_min].S[u];
        }
    }
    
    return result;
}


int main(int argc, char * argv[]){
    int f, o, a;
    f = o = a = 0;

    // Indentificando flags para a execução do Branch & Bound
    if (argc > 1){
        for (int i = 1; i < argc; i++){
            if (strcmp(argv[i], "-f") == 0)
                f = 1;
            else if (strcmp(argv[i], "-o") == 0)
                o = 1;
            else if (strcmp(argv[i], "-a") == 0)
                a = 1;
        }
    }
    // -f = desligar os cortes de viabilidade
    // -o = desligar os cortes de otimalidade
    // -a = usar a função limitante dada pelos professores

    // Lendo numero de representações, atores e papeis 
    scanf("%d %d %d", &l, &m, &n);
    //  l = |S|, m = |A| e n = |P| 

    /*
            Dados um conjunto S de grupos, um conjunto A de atores, um conjunto
        P de personagens, e, para cada ator a ∈ A, um conjunto, Sa ⊆ S indicando os
        grupos dos quais a faz parte, devemos encontrar um elenco que tenha um ator
        para cada personagem (todos os atores podem fazer todas as personagens) e
        todos os grupos tenham um representante. Além disso, também temos um
        valor, va, associado com cada ator a ∈ A, e queremos que o custo do elenco
        seja mínimo.
        Ou seja, devemos encontrar um subconjunto X ⊆ A tal que:
        - |X| = |P|;
        - (UNIÃO)(a∈X)Sa = S; e
        - (SOMATÓRIO)(a∈X)va seja mínimo.
    */

    // Vetor com todos os atores disponiveis 
    ator *A = (ator*)calloc(m, sizeof(ator));

    // Vetor com os atores escolhidos
    ator *X = (ator*)calloc(n, sizeof(ator));

    // Vetor indicando quais atores foram escolhidos
    atores_escolhidos = (int *) calloc(n, sizeof(int));
    
    inicializa(A, m);
    inicializa(X, n);

    // Lendo atores e suas caracteristicas 
    for (int i = 0; i < m; i++){
        scanf("%d %d", &A[i].v, &A[i].s);
        A[i].S = (int *)calloc(A[i].s, sizeof(int));
        for (int u = 0; u < A[i].s; u++){
            scanf("%d", &A[i].S[u]);
        } 
    }

    /*----------------------------CODIGO PRINCIPAL AQUI----------------------------*/

    int valor_total = B_dada(X, A);

    // Essa é a saida que esta nos exemplos 
    for (int i = 0; i < n; i++){
        printf("%d ", atores_escolhidos[i]);
    }
    printf("\n%d\n", valor_total);
    
    /*-----------------------------------------------------------------------------*/

    // Liberando memória alocada
    for (int i = 0; i < m; i++){
        free(A[i].S);
    }
    free(A);
    for (int i = 0; i < n; i++){
        free(X[i].S);
    }
    free(X);
}