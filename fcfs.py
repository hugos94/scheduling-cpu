#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class FCFS(object):
    '''  Algoritmo de escalonamento da CPU que utiliza a politica "First Come, First Serve" para atender as requisicoes. '''

    def __init__(self):
        ''' Inicializa o algoritmo FCFS. '''
        pass

    def execute(self, inputs):
        ''' Metodo que executa o algoritmo de escalonamento com a politica "First Come, First Serve". '''

        self.inputs = copy.deepcopy(inputs) # Realiza a copia profunda das entradas para uma variavel local

        current_position = 0

        current_time = 0
        return_time = 0.0
        response_time = 0.0
        waiting_time = 0.0

        tam_input = len(self.inputs)

        while self.inputs:
            entry = self.inputs[current_position]

            chegada = int(entry[0])
            duracao = int(entry[1])
            if(chegada > current_time):
                current_time = chegada
            response_time += abs(current_time - chegada) # Calcula o tempo de resposta subtraindo o tempo atual e o tempo de chegada do processo
            current_time += duracao
            return_time += current_time - chegada
            self.inputs.pop(0)


        avg_return = (return_time/tam_input)
        avg_response = (response_time/tam_input)
        avg_waiting = 0# (waiting_time/tam_input)


        print("FCFS " + str(avg_return) + " " + str(avg_response) + " " + str(avg_waiting)) # Imprime o resultado final
