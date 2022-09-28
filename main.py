from __future__ import annotations
from typing import Any
#Essa biblioteca serve para auxiliar na tipagem das variaveis

EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

#cria a classe de erro e faz ela herdar atributos da Exception para auxiliar no tratamento de exceções.
class EmptyQueueError(Exception):
    ...

#declara a classe do tipo Node
class Node:
    #O metodo construtor recebe o value, que é do tipo any (qualquer)
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = Node#o next vai receber outro objeto do tipo Node

    #repr serve para representar o objeto, como o toString do Java
    def __repr__(self) -> str:
        return f'{self.value}'

    #metodo bool foi implementado para retornar FALSE caso o no esteja vazio e False caso o node esteja vazio
    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)

#declara a classe do tipo queue
class Queue:
    #o metodo construtor cria variaveis flag para o primeiro e o ultimo elemento da fila
    #quando se instancia uma lista, ela sempre comeca apontando para NULL
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE) #o primeiro começa como vazio porque uma lista começa apontando para NULL
        self.last: Node = Node(EMPTY_NODE_VALUE) #o ultimo tambem comeca com o node vazio, ja que nao ha nada na lista        
        self._count = 0 #variavel flag para armazenar quantos elementos tem na fila

    #funcao para inserir elementos na lista
    def push(self, nodeValue: Any) -> None:
        #instancia um objeto do tipo node
        newNode = Node(nodeValue)

        #checa se o primeiro node é NULL ou nao
        if not self.first:
            #caso seja o primeiro node NULL (primeira chamada da lista) a variavel first passa a apontar para o no inserido
            self.first = newNode

        if not self.last:
            #caso seja o last node NULL (primeira chamada da lista) a variavel last passa a apontar para o no inserido 
            self.last = newNode

        #caso a lista ja esteja preenchida, o last passa a apontar para o node que foi inserido
        else:
            self.last.next = newNode
            self.last = newNode        

        #acrescenta mais um na variavel no count
        self._count +=1

    def pop(self) -> Node:
        if not self.first:
            #tratamento de excecao personalizada
            raise EmptyQueueError("Empty Queue")

        first = self.first

        #o metodo hasattr retorna TRUE se tal objeto tem o atributo dado ou retorna FALSE se tal objeto nao tem o atributo
        #se existir o next nesse first 
        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.firts = Node(EMPTY_NODE_VALUE)

        self._count -= 1
        return first

    #funcao para mostrar o primeiro elemento da lista
    def peek(self) -> Node:
        return self.first

    #funcao para retornar o tamanho da lista
    def __len__(self) -> int:
        return self._count

    #funcao que retorna TRUE se a lista estiver populada e FALSE se ela estiver vazia.
    def __bool__(self) -> bool:
        return bool(self._count)

    def __iter__(self) -> Queue:
        return self

    def __next__(self) -> Any:
        try:
           next_value = self.pop()
           return next_value
        except EmptyQueueError:
            raise StopIteration

    def __repr__(self) -> str:
        if not self.first:
            return 'Queue()'
        return f'Queue({self.first},{self.last})'        

if __name__ == '__main__':
    queue = Queue()
    queue.push('A')
    queue.push('B')
    queue.push('C')
    
    
             






        