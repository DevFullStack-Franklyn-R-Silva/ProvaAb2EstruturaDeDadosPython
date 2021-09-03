class Pilha:
    topo = None
    tamanho = None
    itens = None
    
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.topo = 0
        self.itens = [None] * tamanho
    
    def estaVazia(self):
        return True if self.topo == 0 else False
    def estaCheia(self):
        return True if self.topo == self.tamanho else False
    
    def empilhar(self,item):
        if not self.estaCheia():
            self.itens[self.topo] = item
            self.topo +=1
        else:
            print("esta cheia")
    def desempilhar(self):
        if not self.estaVazia():
            self.topo -=1
            return self.itens[self.topo]
        else:
            print("esta Vazia")
    def contemItem(self,item):
        for i in reversed(self.itens[self.topo]):
            if item == i:
                return True
        return False
    def imprimir(self):
        [print(item)for item in reversed(self.itens[:self.topo])]
        print("----")
                    



