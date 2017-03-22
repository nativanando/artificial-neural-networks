class PCV:
    def __init__(self, VERTICES, INFINITO):
        self.VERTICES = VERTICES
        self.INFINITO = INFINITO
        self.solucao_temporaria = []
        self.melhor_solucao = []
        self.visitados = []
        self.valor_melhor_solucao = self.INFINITO
        self.valor_solucao_atual = 0
        self.populacao = [[2, 5, 3, 10, 8, 6,100, 23],
                          [9, 15, 7, 180, 12, 11,90, 55],
                          [1, 17, 18, 20, 24, 27,29, 56],
                          [92, 68, 70, 48, 25, 32,34, 57],
                          [93, 95, 97, 64, 73, 75,77, 58],
                          [132, 112, 115, 118, 120, 86,88, 35],
                          [114,113,119,61,86,26,30,91],
                          [4, 5, 6, 13,15, 31, 33, 52]]

        for i in range(self.VERTICES):
            self.solucao_temporaria.append(i)
            self.solucao_temporaria[i] = -1
            self.melhor_solucao.append(i)
            self.melhor_solucao[i] = -1
            self.visitados.append(i)
            self.visitados[i] = False

    def caixeiroViajanteAux(self, inicio):

        if self.valor_solucao_atual > self.valor_melhor_solucao:
            return

        if inicio == self.VERTICES:
            distancia = self.populacao[self.solucao_temporaria[inicio - 1]][self.solucao_temporaria[0]]
            # se a distancia for menor q o inf e valor_solucao_atual + a distancia encontrada for menor que o valor_melhor_solucao
            if distancia < self.INFINITO and self.valor_solucao_atual + distancia < self.valor_melhor_solucao:
                self.valor_melhor_solucao = self.valor_solucao_atual + distancia  # valor melhot solucao passa a ser a solucao_atual + a distancia
                # copiatodo o vetor de solução temporária para o vetor de melhor solução encontrada
                for i in range(self.VERTICES):
                    self.melhor_solucao[i] = self.solucao_temporaria[i]

                print ("melhor caminho - valor do caminho", self.melhor_solucao, self.valor_melhor_solucao);

            return

        ultimo = self.solucao_temporaria[inicio - 1]  # Ultimo recebe o número do último vértice que se encontra na solução temporária

        # For que percorre todas as colunas da matriz na linha do último vértice do vetor solução temporária
        for i in range(self.VERTICES):
            if self.visitados[i] == False and self.populacao[ultimo][i] < self.INFINITO:
                self.visitados[i] = True  # marca como visitado
                self.solucao_temporaria[
                    inicio] = i  # carrega o vertice que esta passando no vetor de solução temporário
                self.valor_solucao_atual += self.populacao[ultimo][
                    i]  # Incrementa o valor da matriz na variável que guarda o total do caminho percorrido
                self.caixeiroViajanteAux(inicio + 1)  # Chama recursivamente para o próximo vértice
                self.valor_solucao_atual -= self.populacao[ultimo][
                    i]  # Se ainda não terminou, diminuí o valor da váriavel que guarda o total da solução atual
                self.visitados[i] = False  # Seta como false a posição para poder ser utilizado por outro vértice

    def caixeiroViajante(self, inicial):
        self.visitados[inicial] = True
        self.solucao_temporaria[0] = inicial
        self.caixeiroViajanteAux(1)


if __name__ == '__main__':
    ag = PCV(8, 429496729)

    ag.caixeiroViajante(5)

    print('caminho mínimo', ag.valor_melhor_solucao)

    for i in range(ag.VERTICES):
        print('cidade', ag.melhor_solucao[i])

    print("---------- FIM -----------")


