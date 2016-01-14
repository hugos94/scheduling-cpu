#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy


class RR(object):
    '''  Algoritmo de escalonamento da CPU Round Robin para atender as requisicoes. '''


    def execute(self, inputs):
        ''' Metodo que executa o algoritmo de escalonamento com a politica "Round Robin". '''

        processes = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        quantum = 2 # Tempo fixo de execucao para cada usuario

        current_time = int(processes[0][0]) # Inicializa o tempo atual com o tempo de chegada da primeira entrada
        return_time = 0.0 # Tempo de retorno
        response_time = 0.0 # Tempo de resposta
        waiting_time = 0.0 # Tempo de espera

        tam_input = len(processes) # Tamanho da lista de entradas

        actives = [] # Lista que contera a posicao dos processos que chegaram no inicio
        round_list = [] # Lista que armazena os processos que ja chegaram na cpu
        for position, process in enumerate(processes): # Iteracao na lista de processos
            if(int(process[0]) <= current_time): # Se o processo chegou no tempo atual
                process.append("F") # Adiciona ao processo uma flag para contar o tempo de resposta
                process.append(int(process[0])) # Adiciona ao processo uma variavel que contera o tempo em que o processo parou
                process.append(0) # Adiciona ao processo uma variavel que contera o tempo de espera
                round_list.append(process) # Adiciona o processo a lista circular
                actives.append(position) # Armazena a posicao do processo para posterior remocao

        actives.reverse() # Inverte a lista de processos a serem removidos da entrada
        for active in actives: # Iteracao na lista de processos
            processes.pop(active) # Remocao dos processos escolhidos

        while processes or round_list: # Executar loop enquanto a lista de entradas e a lista de execucao circular for vazia
            process = round_list.pop(0) # Extrai o primeiro processo da lista dos processos prontos

            if(process[2] == "F"): # Verifica se o processo esta sendo executado pela primeira vez
                response_time += abs(current_time - int(process[0])) # Se for a primeira vez, calcula o tempo de resposta do processo
                process[2] = "T" # Modifica a flag para processo ja executado pela primeira vez

            process[4] += abs(current_time - process[3]) # Calcula o tempo de espera do processo

            process[1] = str(int(process[1]) - quantum) # Subtrai o tempo de execucao do tempo de execucao total do processo

            reduction_quantum = 0 # Reducao quando o tempo de execucao do processo e menor que o quantum
            if (int(process[1]) < 0.0): # Verifica se o tempo de execucao do processo ficou negativo
                reduction_quantum = int(process[1]) # Pega o valor que ficou sobrando do quantum
            current_time += quantum + reduction_quantum # Incrementa o tempo atual com o quantum, mas remove o tempo que ficou restante se houver

            process[3] = current_time # Atualiza a variavel que armazena a ultima vez que o programa executou

            remove_list = [] # Lista que armazena as posicoes dos processos a serem removidos da entrada
            for position, proc in enumerate(processes): # Iteracao nos processos restantes na entrada
                if(int(proc[0]) <= current_time): # Verifica se o processo já chegou na lista de processos
                    proc.append("F") # Adiciona a flag que identifica a primeira execucao
                    proc.append(int(proc[0])) # Adiciona a variavel que indica a ultima vez que o processo executou
                    proc.append(0) # Adiciona a variavel que contera o tempo de espera do processo
                    remove_list.append(position) # Adiciona a posicao do processo na lista de remocao de processos da entrada
                    round_list.append(proc) # Adiciona o processo na lista circular

            remove_list.reverse() # Inverte a lista de remocao
            for remove in remove_list: # Iteracao na lista de remocao
                processes.pop(remove) # Remove o processo ativo da lista de entrada

            if(int(process[1]) <= 0.0): # Verifica se o processo terminou a sua execucao totalmente
                return_time += abs(current_time - int(process[0])) # Calcula o tempo de retorno do processo
                waiting_time += process[4] # Calcula o tempo de espera do processo
            else: # Se nao terminou a execucao completamente
                round_list.append(process) # Coloca o processo no final da lista de processos prontos

        avg_return = (return_time/tam_input) # Refere-se ao tempo transcorrido entre o momento da entrada do processo no sistema e o seu término.
        avg_response = (response_time/tam_input) # Intervalo de tempo entre a chegada do processo e o início de sua execução.
        avg_waiting = (waiting_time/tam_input) # Intervalo de tempo em que o processo fica em estado de espera

        out = "RR " + str(round(avg_return,1)) + " " + str(round(avg_response,1)) + " " + str(round(avg_waiting,1)) # Armazena a resposta do algoritmo

        print(out.replace(".",",")) # Imprime o resultado final trocando os pontos por virgulas
