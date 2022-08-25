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

int l, m, n;

int min(ator * F, int len){
    int resul = F[0].v;
    for (int i = 1; i < len; i++){
        if (F[i].v < resul){
            resul = F[i].v;
        }
    }
    return resul;
}

int B_dada(ator * E, ator * F){
    int len_F = 0;
    int len_E = 0;
    for (int i = 0; i < m; i++){
        if (F[i].v == 0){
            break;
        }
        len_F++;
    }
    for (int i = 0; i < n; i++){
        if (E[i].v == 0){
            break;
        }
        len_E++;
    }
    int result = 0;
    for (int i = 0; i < len_E; i++){
        result += E[i].v + (n - len_E) * min(F, len_F);
    }
    return result;
}


int main(int argc, char * argv[]){
    int f, o, a;
    f = o = a = 0;
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

    ator *A = NULL;
    ator *X = NULL;
    A = (ator*)calloc(m, sizeof(ator));
    X = (ator*)calloc(n, sizeof(ator));

    for (int i = 0; i < m; i++){
        scanf("%d %d", &A[i].v, &A[i].s);
        A[i].S = (int *)calloc(A[i].s, sizeof(int));
        for (int u = 0; u < A[i].s; u++){
            scanf("%d", &A[i].S[u]);
        } 
    }
    // for (int i = 0; i < m; i++){
    //     printf("%d %d\n", A[i].v, A[i].s);
    //     for (int u = 0; u < A[i].s; u++){
    //         printf("%d\n", A[i].S[u]);
    //     }
    // }

    printf("valor total: %d\n",B_dada(X, A));
    
    for (int i = 0; i < m; i++){
        free(A[i].S);
    }
    free(A);
    free(X);
}