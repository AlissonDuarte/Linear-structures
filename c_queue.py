import numpy as np

class CircularQueue:
    def __init__(self, size):
        """A fila não apaga valores e sim sobrescreve na prática"""
        self.size = size
        self.start = 0
        self.end = -1
        self.elements = 0
        self.values = np.empty(self.size, dtype=int)

    def __empty(self):
        return self.elements == 0
    
    def __is_full(self):
        return self.elements == self.size
    
    def enqueue(self, value):
        if self.__is_full():
            print('The queue is full')
            return
        else:
            #verificamos em qual lado está o start e o end
            if self.end == self.size - 1:
                #[6, 2, 3, 4, 5]
                #neste caso o indice do ultimo elemento (5) é igual a 4, logo o if compara
                #se o indice final 4 é igual ao tamanho total -1: 4 == 5-1
                #atendida esta condição quer dizer que linearmente a fila foi preenchida e não está cheia
                #logo há posições vazias no inicio da fila
                #desta forma o indice indicado para o proximo elemento se torna -1
                self.end = -1
                
            self.end +=1 # nesta linha somamos -1 +1 para indicar o indice 0 da fila, ou seja, o inicio dela
            self.values[self.end] = value # Adiciona o valor à fila
            self.elements +=1 # Atualiza o número de elementos
    
    def dequeue(self):
        if self.__empty():
            print('The queue is already empty')
            return 
        tmp = self.values[self.start] # Armazena temporariamente o valor do elemento a ser removido
        self.start +=1 # Incrementa o índice start para apontar para o próximo elemento
        if self.start == self.size -1:
            self.start = 0 # Se start estiver no final do array, ajusta para 0 (fila circular)
        self.elements -= 1 # Atualiza o número de elementos
        return tmp # retorna o valor removido
    
    def first(self):
        if self.__empty():
            return -1
        return self.values[self.start]

queue = CircularQueue(5)
print(queue.first())

queue.enqueue(1)
print(queue.first())

queue.enqueue(2)
print(queue.first())

queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
queue.enqueue(5)
queue.enqueue(6)
print(queue.first())
