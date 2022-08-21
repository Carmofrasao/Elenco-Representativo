# Anderson Aparecido do Carmo Frasão (GRR20204069)
# Richard Fernando Heise Ferreira (GRR20191053)

CFLAGS  = -Wall -g
CC = gcc 

#-----------------------------------------------------------------------------#
all : elenco

run: elenco
	./elenco < teste1.txt

elenco: elenco.o


#-----------------------------------------------------------------------------#

clean :
	$(RM) *.o

#-----------------------------------------------------------------------------#

purge:
	$(RM) elenco *.o