#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from file_manager import *
from fcfs import *
from sjf import *
from rr import *

def main():

    filename = sys.argv[-1] # Recebe o nome do arquivo do console

    if(filename == sys.argv[0]): # Verifica se algum arquivo foi recebido
        print("Arquivo não informado!")

    else:
        fm = FileManager() # Inicializa o gerenciador de arquivos

        inputs = fm.read_input(filename) # Le o arquivo e retorna em forma de lista

        for i in inputs:
            for j in i:
                print(j)

        fcfs = FCFS() # Inicializa o algoritmo FCFS
        #fcfs.execute(inputs) # Executa o algoritmo FCFS
        #
        # sstf = SSTF(sectors, initial_sector) # Inicializa o algoritmo SSTF
        # sstf.execute(inputs) # Executa o algoritmo SSTF
        #
        # elevador = Elevador(sectors, initial_sector) # Inicializa o algoritmo Elevador
        # elevador.execute(inputs) # Executa o algoritmo Elevador


if __name__ == '__main__':
    main()
