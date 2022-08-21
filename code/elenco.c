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
    
    int l, m, n;

    scanf("%d %d %d", &l, &m, &n);

    ator *A = (ator*)calloc(m, sizeof(ator));

    for (int i = 0; i < m; i++){
        scanf("%d %d", &A[i].v, &A[i].s);
        A[i].S = (int *)calloc(A[i].s, sizeof(int));
        for (int u = 0; u < A[i].s; u++){
            scanf("%d", &A[i].S[u]);
        } 
    }

    
}