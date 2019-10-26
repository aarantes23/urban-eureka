import math
import operator

# Antes de comecar, remova via notepad++ os caracteres que foram adicionados por erro:
# ]] , \n, \

# Som para avisar acabar de executar o codigo
import winsound
frequency = 2500  # Define a  frequencia em 2500 Hertz
duration = 1000  # Define a duracao em 1000 ms == 1 segundo

dataSetNames = ["cellcycle_FUN.full.arff", "church_FUN.full.arff", "derisi_FUN.full.arff",
                "eisen_FUN.full.arff", "expr_FUN.full.arff", "gasch1_FUN.full.arff",
                "gasch2_FUN.full.arff", "hom_FUN.full.arff", "pheno_FUN.full.arff",
                "seq_FUN.full.arff", "spo_FUN.full.arff", "struc_FUN.full.arff"]
dataSetNames = ["cellcycle_FUN.full.arff", "church_FUN.full.arff", "derisi_FUN.full.arff",
                "eisen_FUN.full.arff", "expr_FUN.full.arff", "gasch1_FUN.full.arff",
                "gasch2_FUN.full.arff",  "pheno_FUN.full.arff",
                "seq_FUN.full.arff", "spo_FUN.full.arff"]
_type = [".test.", ".train."]
_eof = [".arff"]
# Path for the crossValidation
pathCrossValidation = "../../datasets/crossValidation/"
#pathCrossValidation = "../../datasets/testes/"
# Path for the results
pathResults = "../../results/"


#k_ = [3,5,7,10,15,20,25,30,35,40,45,50,55,60,150,300,450,600,750,900] # Número de vizinhos usados no knn
k_ = [5]
# Número de partes desejada da divisão da validação cruzada
folds = [0,1]
#folds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def getHf(testSet, predictions):
    hp = getHp(testSet, predictions)
    hr = getHr(testSet, predictions)
    return ((2*hp*hr)/(hp+hr))


def getHr(testSet, predictions):
    hr = 0.0
    for m in range(len(testSet)):
        classe = testSet[m][-1].split("/")
        prediction = predictions[m][0][0].split("/")
        #print("classe : ", classe)
        #print("prediction : ", prediction)
        num, den = 0, 0
        i_lvl = 0  # Comeca pelo nível da Raiz da predição
        for i in prediction:
            if not (i == 'R'):  # O nível da raiz não entra na medida
                j_lvl = 0  # Começa pelo nível da Raiz a classe.
                # Valor definido aqui, porque sempre que voltar ao looping de predições recomeçará do zero o contador da classe
                # Tentei melhorar, porém sempre dava um erro logico diferente
                for j in classe:  # Percorre todo o vetor da classe
                    if (i_lvl == j_lvl):  # Verifica se a predição e a classe estão no mesmo nível
                        if not (j == 'R'):  # Ignora se for a raiz
                            if (i == j):  # Se os dois valores são iguais
                                # Incrementa o contador da variável do numerador da equação (num)
                                num += 1
                    j_lvl += 1  # Antes de terminar o looping da classe, adiciona 1 ao nível da mesma
                    # Diferença entre o hp está aonde o denominador é incrementado
                    # Incrementa o contador da variável do denumerador da equação (den)
                    den += 1
            i_lvl += 1  # Antes de terminar o looping da predição, adiciona 1 ao nível da mesma
        hr += num/den
    return hr/1000


def getHp(testSet, predictions):
    hp = 0.0
    for m in range(len(testSet)):
        classe = testSet[m][-1].split("/")
        prediction = predictions[m][0][0].split("/")
        num, den = 0, 0
        i_lvl = 0  # Comeca pelo nível da Raiz da predição
        for i in prediction:
            if not (i == 'R'):  # O nível da raiz não entra na medida
                j_lvl = 0  # Começa pelo nível da Raiz a classe.
                # Valor definido aqui, porque sempre que voltar ao looping de predições recomeçará do zero o contador da classe
                # Tentei melhorar, porém sempre dava um erro logico diferente
                for j in classe:  # Percorre todo o vetor da classe
                    if (i_lvl == j_lvl):  # Verifica se a predição e a classe estão no mesmo nível
                        if not (j == 'R'):  # Ignora se for a raiz
                            if (i == j):  # Se os dois valores são iguais
                                # Incrementa o contador da variável do numerador da equação (num)
                                num += 1
                    j_lvl += 1  # Antes de terminar o looping da classe, adiciona 1 ao nível da mesma
                # Incrementa o contador da variável do denumerador da equação (den)
                den += 1
            i_lvl += 1  # Antes de terminar o looping da predição, adiciona 1 ao nível da mesma
        hp += num/den
    return hp/1000


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if (testSet[x][-1] == predictions[x][0][0]):
            correct += 1
    return (correct/float(len(testSet))) * 100.0


def getAccuracyPrints(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        print("[getAccuracy] testeSet:    ", testSet[x][-1])
        print("[getAccuracy] predictions: ", predictions[x][0][0])
        if (testSet[x][-1] == predictions[x][0][0]):
            correct += 1
            print("Correct!")
        print("--------------------------------------------------")
    return (correct/float(len(testSet))) * 100.0


def showResults(metrics):
    k, hf, hr, hp, accuracy = metrics
    print("Resultados: ")
    print('Hf : ', hf, '%')
    print('Hr : ', hr, '%')
    print('Hp : ', hp, '%')
    print('Acurácia : ', accuracy, '%')
    print("----------------------------")


def writeResultsMetrics(file_path_, metrics, strings):
    db_name, db_test_num = strings
    k, hf, hr, hp, accuracy = metrics
    output_file = open(file_path_ +db_name+"_db_test_"+db_test_num+"_ResultsMetrics_for_k="+k+'.txt', 'w')
    output_file.write("@ db_name: "+db_name+"\n\n")    
    output_file.write("@ k\n")
    output_file.write("@ hf\n")
    output_file.write("@ hr\n")
    output_file.write("@ hp\n")
    output_file.write("@ accuracy\n\n")
    output_file.write("@ DATA\n")    
    output_file.write(k + "\n")
    output_file.write(hf + "\n")
    output_file.write(hr + "\n")
    output_file.write(hp + "\n")
    output_file.write(accuracy)

def euclideanDistance(instance1, instance2, length):
    distance = 0  # Inicializar variável da distância
    #print("Instance1 (test): ",instance1)
    #print("Instance2 (train) : ",instance2)
    for x in range(length):  # Para a instância inicial até o tamanho informado inicialmente
        # Calculará a distancia entre a instâcia 1 e a instâcia 2
        # [pow] método para potenciação ex: pow((equação),expoente)
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testSet, k):
    #print("trainingSet len : ", trainingSet)
    #print("testSet len : ",testSet)
    distances = []  # Lista de distâncias
    # Até o penultimo atributo, assim excluirá o atributo classe
    length = len(testSet) - 1
    for x in range(len(trainingSet)):  # Para cada instância x da base de treinamento
        # Calculará a distância euclidiana entre os elementos de uma lista e outra
        dist = euclideanDistance(testSet, trainingSet[x], length)
        #print("Distancia : ", dist)
        # Adiciona as distâncias a uma tupla
        distances.append((trainingSet[x][-1], dist))
    # Ordena os vizinhos pela menor distância
    distances.sort(key=operator.itemgetter(1))

    neighbors = []  # Cria uma nova lista de vizinhos
    for x in range(k):
        # Preenche a nova lista dos vizinhos com os k mais próximos
        neighbors.append(distances[x])
    # Novamente, ordena os vizinhos pela distancia, talvez desnecessário
    neighbors.sort(key=operator.itemgetter(1))
    return neighbors


def hknn(neighbors, l):
    classVotes = {}  # Dicionario para realizar a contagem dos votos
    candList = []    # Lista temporaria dos candidatos do nivel "l"
    resultList = []  # Lista dos resultados
    c2Neighbors = []  # Lista dos candidatos ao Criterio 2

    # Criterio 1
    # Conta quantas ocorrrencias iguais existem no nivel "l"
    for i in range(len(neighbors)):
        # Divide a string para verificar o nivel atual
        response = neighbors[i][0].split("/")
        if response[l] in classVotes:
            classVotes[response[l]] += 1
        else:
            classVotes[response[l]] = 1

    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(
        1), reverse=True)    # Ordena os votos

    # Remove da lista os candidatos com menor frenquencia
    bigger = 0
    for n in sortedVotes:
        if n[1] not in resultList:
            if n[1] >= bigger:
                bigger = n[1]
                candList.append(n)

    # Criar uma nova lista com os candidatos para o Criterio 2
    for i in range(len(neighbors)):
        response = neighbors[i][0].split("/")
        for j in range(len(candList)):
            if response[l] == candList[j][0]:
                c2Neighbors.append(neighbors[i])

    # Criterio 2
    # Entre os possiveis candidatos definidos no criterio 1, verificar os que tem a menor distancia
    # No caso de um empate, o "random" será a primeira ocorrencia aleatoria.
    if ((len(c2Neighbors)) > 1):
        resultList = [c2Neighbors[0]]

    """
    # Se ainda nao houver somente um cadidato, 
    # recomeca com o primeiro criterio para os novos candidatos, 
    # analisando agora em um novo nivel da hierarquia
    if len(resultList) != 1:
        hknn(resultList,l+1)
    """
    return resultList

# Main
for k in k_:
    print("k: ", k)
    for dataSet in dataSetNames:
        print("dataSet : ",dataSet)
        dataSetTrain = []  # Dados de treinamento
        dataSetTest = []  # Dados de teste
        oldPredictions = []  # Predicoes anteriores
        dataTrain = []
        dataTest = []
        accuracy_ = 0
        hp_ = 0
        hr_ = 0
        hf_ = 0

        # open datasets train and test for the current db
        for i in folds:
            # Train
            file_ = open(pathCrossValidation +
                         str(dataSet)+str(_type[1])+str(i)+str(_eof[0]), "r")
            data = file_.readlines()
            for line in data:
                line_ = line.strip().split(",")
                dataTrain.append(line_)
            dataSetTrain.append(dataTrain)
            data = []
            file_.close()
            # Test
            file_ = open(pathCrossValidation +
                         str(dataSet)+str(_type[0])+str(i)+str(_eof[0]), "r")
            data = file_.readlines()
            for line in data:
                line_ = line.strip().split(",")
                dataTest.append(line_)
            dataSetTest.append(dataTest)
            data = []
            file_.close()

        for fold in range(len(folds)):            
            neighbors = []
            finalNeighbors = []
            predictions = []
            # Depois de ter carregado os conjuntos de treinamento e teste
            # Para cada instância de teste        
            for i in range(len(dataSetTest[fold])):                 
                # Encontra seus vizinhos                
                neighbors = getNeighbors(
                    dataSetTrain[fold], dataSetTest[fold][i], k)
                finalNeighbors = hknn(neighbors, 0)  # Executa o método hknn
                # Adiciona a lista das predições
                predictions.append(finalNeighbors)
                """
                if oldPredictions:  # Se já existem predições, tenta melhorá-las
                    for x in range(len(predictions)):
                        # Se a distancia for menor, acreditasse que é um melhor vizinho
                        if (predictions[x][0][1] < oldPredictions[x][0][1]):
                            predictions[x] = finalNeighbors
                else:  # Se ainda não exisitem predições, define que as atuais são as melhores
                    oldPredictions = []  # Limpa a lista anterior
                    oldPredictions = predictions  # Atribui a nova a atual
                """
            predictions_len = len(predictions)

            # Metricas de avaliação
            # Verifica a acurácia para a parte de testes atual
            accuracy = getAccuracy(
                testSet=dataSetTest[fold], predictions=predictions)
            # hierarchical precision
            hp = getHp(testSet=dataSetTest[fold], predictions=predictions)
            # hierarchical recall
            hr = getHr(testSet=dataSetTest[fold], predictions=predictions)
            # hierarchical f-mesure
            hf = getHf(testSet=dataSetTest[fold], predictions=predictions)

            # Soma os valores obtidos aos anteriores
            accuracy_ += accuracy
            hp_ += hp
            hr_ += hr
            hf_ += hf

            showResults(metrics=[str(k), str(hf),
                                str(hr), str(hp), str(accuracy)])
            # Depois de executar todas as [fold] vezes
            if (fold == (len(folds)-1)):

                # Extrai a media dos valores obtidos
                accuracy_ = accuracy_ / len(folds)
                hp_ = hp_ / len(folds)
                hr_ = hr_ / len(folds)
                hf_ = hf_ / len(folds)

                strings_ = [str(dataSet), str(fold)]
                metrics_ = [str(k), str(hf_), str(
                    hr_), str(hp_), str(accuracy_)]

                # Salva os resultados das medias das metricas de avaliação
                writeResultsMetrics(file_path_=pathResults,
                                    metrics=metrics_, strings=strings_)
                            
                # Por fim, exibe os resultados conseguidos
                showResults(metrics=metrics_)
            # if test == False: break  # Debug de teste para executar somente uma vez

            winsound.Beep(frequency, duration)

print("\nWork complete")