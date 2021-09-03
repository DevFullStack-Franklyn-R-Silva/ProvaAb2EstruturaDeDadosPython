class Celula:
    item = None
    tamanho = 0
    def __init__(self,item):
        self.item = item
class Pilha_encadeada:
    topo = None
    tamanho = 0
    def estaVazia(self):
        return True if self.tamanho == 0 else False
    
    def empilhar(self,item):
        aux = self.topo
        self.topo = Celula(item)
        self.topo.proximo = aux
        self.tamanho +=1
    
    def desempilhar(self):
        if self.estaVazia() == False:
            item = self.topo.item
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return item
        else:
            return ""
    
    def verTamanho(self):
        return self.tamanho
    
    def imprimir(self):
        print(aux.item)
        aux = aux.proximo
    

pilha = Pilha_encadeada()

lista = []
cont = 0
print("DIGITE 0 PARA, PARAR E DESEMPILHAR")
print("DIGITE SUA PILHA")
while True:
    a = input()
    cont +=1
    pilha.empilhar(item = a)
    lista.append(a)
    if a == "0":
        for i in range(cont):
            print(pilha.desempilhar())
            
        break
            
                
        
        


    



        
