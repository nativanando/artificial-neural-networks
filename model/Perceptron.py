from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
import time

# cria-se um conjunto de dados (dataset) para treinamento
# os valores esperados para o treinamento supervisionado
dataset = SupervisedDataSet(2, 1)

# tabela verdade do XOR
dataset.addSample([1, 1], [0])
dataset.addSample([1, 0], [1])
dataset.addSample([0, 1], [1])
dataset.addSample([0, 0], [0])

'''
Construir a rede utilizando a função buildNetwork
dataset.indim é o tamanho da camada de entrada
4 é a quantidade de camadas intermediárias
dataset.outdim é o tamanho da camada de saída
"bias" para permitir uma melhor adaptação por parte da rede neural ao conhecimento à ela fornecido
'''
network = buildNetwork(dataset.indim, 4, dataset.outdim, bias=True)

'''
Backpropagation como algoritmo de treinamento
É pasada a rede, o conjunto de dados (dataset), "learningrate" é a taxa de aprendizado,
"momentum" tem por objetivo aumentar a velocidade de treinamento da rede neural e
diminuir o perigo da instabilidade.
'''
trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.99)

inicio = time.time()  # tempo de execução do treinamento

for epoch in range(0, 1000):  # treina por 1000 iterações para ajuste de pesos
    trainer.train()

fim = time.time()
print('tempo de treinamento', fim - inicio)
'''
Outras formas de treinar:
    trainer.trainEpochs(1000)
    treinar até a convergência: trainer.trainUntilConvergence()
'''

# Agora iremos testar a rede com um conjunto de dados
# testando com os mesmos dados
test_data = SupervisedDataSet(2, 1)
test_data.addSample([1, 1], [0])
test_data.addSample([1, 0], [1])
test_data.addSample([0, 1], [1])
test_data.addSample([0, 0], [0])
# verbose=True indica que deve ser impressas mensagens
trainer.testOnData(test_data, verbose=True)

# testando com dados arbitrários para avaliar a capacidade de ajuste aos padrões
print('testando segunda lista de parametros')
test_data2 = SupervisedDataSet(2, 1)
test_data2.addSample([0, 1], [0])  # saida 1 //erro //correct é a sequencia colocada e out e a saída da rede
test_data2.addSample([0, 1], [1])  # saida 1 //ok
test_data2.addSample([0, 0], [1])  # saida 0 //erro
test_data2.addSample([1, 1], [0])  # saida 0 /ok
resultado = trainer.testOnData(test_data2, verbose=True)

'''
Testing on data2:
('out:    ', '[1     ]')
('correct:', '[0     ]')
error:  0.50000000
('out:    ', '[1     ]')
('correct:', '[1     ]')
error:  0.00000000
('out:    ', '[0     ]')
('correct:', '[1     ]')
error:  0.50000000
('out:    ', '[-0    ]')
('correct:', '[0     ]')
error:  0.00000000
('All errors:', [0.49999999800449013, 1.9910298175559249e-18, 0.49999999874645429, 9.1022975298697453e-21])
('Average error:', 0.2499999991877361)
('Max error:', 0.49999999874645429, 'Median error:', 0.49999999800449013)
'''
