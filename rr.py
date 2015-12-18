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
            best_choice = -1 # Variavel que armazena a melhor escolha
            best_time = float("inf") # Variavel que armazena o melhor tempo inicializada com infinito
            chegada_escolhido = 0  # Variavel que armazena o tempo de chegada do menor processo

            for entry in self.inputs: # Iteracao entre as entradas
                chegada = int(entry[0]) # Converte o primeiro campo da entrada em int
                duracao = int(entry[1]) # Converte o segundo campo da entrada em int

                if (chegada <= current_time): # Verifica se o tempo de chegada é menor ou igual ao tempo atual
                    if(duracao < best_time): # Verifica se o tempo da entrada atual, é melhor que a menor entrada
                        chegada_escolhido = chegada
                        best_time = duracao
                        best_choice = entry

            response_time += abs(current_time - chegada_escolhido) # Calcula o tempo de resposta subtraindo o tempo atual e o tempo de chegada do processo
            current_time += best_time # Atualiza o tempo atual como a soma do tempo atual e o do melhor tempo
            return_time += abs(current_time - chegada_escolhido) # Calcula o tempo de terorno subtraindo o tempo atual pelo tempo de chegada do processo
            self.inputs.remove(best_choice) # Remove o processo da lista de processos

        avg_return = (return_time/tam_input) # Refere-se ao tempo transcorrido entre o momento da entrada do processo no sistema e o seu término.
        avg_response = (response_time/tam_input) # Intervalo de tempo entre a chegada do processo e o início de sua execução.
        avg_waiting = avg_response # Soma dos períodos em que um processo estava no seu estado pronto. (No algoritmo FCFS o tempo medio de resposta e igual ao tempo medio de espera)

        print("RR " + str(round(avg_return,1)) + " " + str(avg_response) + " " + str(avg_waiting)) # Imprime o resultado final
