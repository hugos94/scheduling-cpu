#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy


class FCFS(object):
    '''  Algoritmo de escalonamento da CPU que utiliza a politica "First Come, First Serve" para atender as requisicoes. '''


    def execute(self, inputs):
        ''' Metodo que executa o algoritmo de escalonamento com a politica "First Come, First Serve". '''

        processes = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        current_time = 0 # Tempo atual
        return_time = 0.0 # Tempo de retorno
        response_time = 0.0 # Tempo de resposta
        waiting_time = 0.0 # Tempo de espera

        tam_input = len(processes) # Tamanho da lista de entradas

        while processes: # Enquanto a lista nao for vazia, execute
            entry = processes[0] # Armazena em entry a primeira entrada

            chegada = int(entry[0]) # Converte o primeiro campo da entrada em int
            duracao = int(entry[1]) # Converte o segundo campo da entrada em int

            if(chegada > current_time): # Se o tempo de chegada for maior que o tempo atual
                current_time = chegada # O tempo atual sera o tempo de chegada

            response_time += abs(current_time - chegada) # Calcula o tempo de resposta subtraindo o tempo atual e o tempo de chegada do processo
            current_time += duracao # Tempo atual e somado com a duracao do processo
            return_time += current_time - chegada # Tempo de retorno e subtraido do tempo de chegada

            processes.pop(0) # Remove o primeiro elemento da entrada

        avg_return = (return_time/tam_input) # Refere-se ao tempo transcorrido entre o momento da entrada do processo no sistema e o seu término.
        avg_response = (response_time/tam_input) # Intervalo de tempo entre a chegada do processo e o início de sua execução.
        avg_waiting = avg_response # Soma dos períodos em que um processo estava no seu estado pronto. (No algoritmo FCFS o tempo medio de resposta e igual ao tempo medio de espera)

        out = "FCFS " + str(round(avg_return,1)) + " " + str(round(avg_response,1)) + " " + str(round(avg_waiting,1)) # Armazena o resultado final

        print(out.replace(".", ",")) # Imprime o resultado final trocando os pontos por virgulas
