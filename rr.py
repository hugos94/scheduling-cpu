#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class RR(object):
    '''  Algoritmo de escalonamento da CPU Round Robin para atender as requisicoes. '''

    def __init__(self):
        ''' Inicializa o algoritmo Round Robin. '''
        pass

    def execute(self, inputs):
        ''' Metodo que executa o algoritmo de escalonamento com a politica "Round Robin". '''

        self.inputs = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        quantum = 2 # Tempo fixo de execucao para cada usuario

        current_time = int(self.inputs[0][0]) # Inicializa o tempo atual com o tempo de chegada da primeira entrada
        return_time = 0.0 # Tempo de retorno
        response_time = 0.0 # Tempo de resposta
        waiting_time = 0.0 # Tempo de espera

        tam_input = len(self.inputs) # Tamanho da lista de entradas

        while self.inputs: # Enquanto a lista nao for vazia, execute
            active_list = []
            for position,i in enumerate(self.inputs):
                if (int(i[0]) <= current_time):
                    active_list.append(position)

            remove_list = []
            for i in active_list:
                i = int(i)
                self.inputs[i][1] = str(int(self.inputs[i][1]) - quantum)
                current_time += quantum
                if (int(self.inputs[i][1]) <= 0):
                    return_time += abs(int(self.inputs[i][1])-current_time)
                    remove_list.append(self.inputs.index(self.inputs[i]))

            remove_list.reverse()
            for i in remove_list:
                self.inputs.pop(i)

        avg_return = (return_time/tam_input) # Refere-se ao tempo transcorrido entre o momento da entrada do processo no sistema e o seu término.
        avg_response = 0#(response_time/tam_input) # Intervalo de tempo entre a chegada do processo e o início de sua execução.
        avg_waiting = 0#avg_response # Soma dos períodos em que um processo estava no seu estado pronto. (No algoritmo FCFS o tempo medio de resposta e igual ao tempo medio de espera)

        out = "RR " + str(round(avg_return,1)) + " " + str(round(avg_response,1)) + " " + str(round(avg_waiting,1)) # Armazena a resposta do algoritmo

        print(out.replace(".",",")) # Imprime o resultado final trocando os pontos por virgulas
