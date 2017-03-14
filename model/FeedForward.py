from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection

'''
Rede FeedFoward utilizando 2 entradas, 3 neuronios na camada oculta e 2 saídas
A criação desta rede leva em consideração e referência a documentação oficial do PyBrain.
A rede que implementa FeedForward em seu treinamento tem como característica a passagem contínua pelos neurônios,
ajustando os pesos sinápticos e sem retropropagação, ou seja, não voltará ajustando os valores dada sua saída.
'''


class FeedFoward:
    def __init__(self, network, camada_entrada, camada_oculta, camada_saida):
        self.network = network
        self.network = FeedForwardNetwork()
        self.camada_entrada = camada_entrada
        self.camada_oculta = camada_oculta
        self.camada_saida = camada_saida
        self.ligacao_entrada_oculta = None
        self.ligacao_oculta_saida = None
        self.defineArquitetura()

    def defineArquitetura(self):
        self.camada_entrada = LinearLayer(2, name="in")
        self.camada_oculta = SigmoidLayer(3, name="hidden")
        self.camada_saida = LinearLayer(1, name="out")
        self.adicionaEstrutura()

    def adicionaEstrutura(self):
        self.network.addInputModule(self.camada_entrada)
        self.network.addModule(self.camada_oculta)
        self.network.addOutputModule(self.camada_saida)
        self.adicionaConexoes()

    def adicionaConexoes(self):
        self.ligacao_entrada_oculta = FullConnection(self.camada_entrada, self.camada_oculta)
        self.ligacao_oculta_saida = FullConnection(self.camada_oculta, self.camada_saida)
        self.network.addConnection(self.ligacao_oculta_saida)
        self.network.addConnection(self.ligacao_entrada_oculta)
        self.iniciaRede()

    def visualizaPesosSinapticos(self):
        print('peso camada_entrada_oculta',
              self.ligacao_entrada_oculta.params)  # mostra os pesos das conexões de entrada para camada oculta, todas interligadas entre sí. 2x3 = 6 pesos sinpaticos
        print('peso camada_oculta_saida',
              self.ligacao_oculta_saida.params)  # mostra os pesos das conexões da camada oculta para a camada de saída. Todas interligadas entre sí. 3x1 = 3 pesos sinapticos
        print('pesos rede', self.network.params)

    def iniciaRede(self):
        self.network.sortModules()


network = None
rna = FeedFoward(network, 2, 3, 2)
print('-------------------------------------------')
rna.network.activate([2, 1])
rna.visualizaPesosSinapticos()
print('-------------------------------------------')
rna.network.activate([2, 2])
rna.visualizaPesosSinapticos()
