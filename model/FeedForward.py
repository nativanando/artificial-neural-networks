from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer

'''
MLP utilizando 3 entradas, 4 neuronios na camada oculta e 1 saídas
A criação desta rede leva em consideração e referência a documentação oficial do PyBrain.
A rede, que é caracterizada por um modelo FeedFoward, neste caso, teve um treinamento utilizando o algoritmo backpropagation,
com as camadas ocultas utilizando a função de ativação sigmoide nos neurônios da camada oculta
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
        self.camada_entrada = LinearLayer(self.camada_entrada, name="in")
        self.camada_oculta = SigmoidLayer(self.camada_oculta, name="hidden")
        self.camada_saida = LinearLayer(self.camada_saida, name="out")
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


dataset = SupervisedDataSet(3, 1)
dataset.addSample([1, 1, 1], [1])
dataset.addSample([1, 0, 0], [0])
dataset.addSample([0, 1, 1], [1])
dataset.addSample([0, 0, 1], [0])
dataset.addSample([0, 0, 0], [0])

network = None
rna = FeedFoward(network, 3, 4, 1)
print('-------------------------------------------')
rna.network.activate([2, 1, 3])
rna.visualizaPesosSinapticos()
print('-------------------------------------------')
rna.network.activate([2, 2, 3])
rna.visualizaPesosSinapticos()

trainer = BackpropTrainer(rna.network, dataset, learningrate=0.01, momentum=0.99)
for epoch in range(0, 10000):  # treina por 1000 iterações para ajuste de pesos
    trainer.train()

test_data = SupervisedDataSet(3, 1)
test_data.addSample([0, 1, 0], [0])
test_data.addSample([1, 1, 0], [1])
test_data.addSample([1, 0, 0], [0])
test_data.addSample([0, 1, 1], [1])
trainer.testOnData(test_data, verbose=True) # verbose=True indica que deve ser impressas mensagens

