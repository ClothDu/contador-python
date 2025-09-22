class Contador:
    def __init__(self, pontoContadores=None, nomeContador=None):
        self.pontoContadores = pontoContadores if pontoContadores is not None else [0, 0]
        self.nomeContador = nomeContador if nomeContador is not None else ["jogador 1", "jogador 2"]
        
    def adicionarContador(self, nome):
        self.pontoContadores.append(0)
        self.nomeContador.append(nome)
        
    def adicionarPonto(self, numContador, num):
        self.pontoContadores[numContador] += num
        
    def removerPonto(self, numContador, num):
        self.pontoContadores[numContador] -= num
        
    def modificarNome(self, pos, nomeContador):
        self.nomeContador[pos] = nomeContador
        
    def getContador(self, pos):
        return self.pontoContadores[pos]
    
    def getNomeContador(self, pos):
        return self.nomeContador[pos]