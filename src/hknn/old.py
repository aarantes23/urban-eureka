
for k in k_:
    print("k: ",k)
    for dataSet in dataSetNames:
        print("db: ",dataSet)
        dataSet = [] # Lista que receberá o arquivo carregado 
            

        dataSet = loadDataset('dbs/'+db_name+'.arff') # Carrega o arquivo
        dataSet = strToFloat(dataSet) # Converte algumas strings para float
        dataSet = cross_validation_split(dataSet,folds) # Divide a base em folds partes

        trainingSet = [] # Lista para base de treinamento
        testSet = [] # Lista para base de teste
        finalNeighbors = [] # Lista dos vizinhos finais (hknn)
        predictions = [] # Lista de predições
        oldPredictions = [] # Lista de antigas predições
    
        accuracy_,hp_,hr_,hf_ = 0,0,0,0 # Metricas médias de availação

        # A cada vez uma parte é alocada para teste e as outras para treinamento
        for test in range(len(dataSet)):
            db_test_num = test # Copia o número do teste para facilitar salvar no arquivo
            testSet = [] # Lista do conjunto de testes atual 
            trainingSet = [] # Lista do conjunto de treinamento atual
            predictions = [] # Redundante, potencial erro, nome de variável já existe
    
            print("Teste fold: ",test+1,"/",len(dataSet)) # Exibe qual a parte esta sendo usada para teste no momento    
    
            # Retira uma k parte para teste e as outras partes para treinamento
            for j in range(len(dataSet)): # Para o tamanho do dataSet  
                if (j == test): # Se a parte atual for a de teste
                    for n in range(len(dataSet[j])): # Para cada instância dessa base 
                        testSet.append(dataSet[j][n]) # Será adicionada uma nova instância a lista do conjunto de teste atual             
                # Se não for o conjunto de teste, a parte será adicionada para o conjunto de treinamento
                else: 
                    for n in range(len(dataSet[j])):
                        trainingSet.append(dataSet[j][n])
            
            test_len = len(testSet)
            train_len = len(trainingSet)
        
            # Depois de ter dividido os conjuntos de treinamento e teste
            if trainingSet and testSet: # Verifica se nenhuma das listas estão vazias
                # Se não estão, prosegue com o procedimento de teste normalmente
                for x in range(len(testSet)): # Para cada instância de teste
                    neighbors = getNeighbors(trainingSet, testSet[x], k) # Encontra seus vizinhos 
                    finalNeighbors = hknn(neighbors,1) # Executa o método hknn
                    predictions.append(finalNeighbors) # Adiciona a lista das predições             
                if oldPredictions: # Se já existem predições, tenta melhorá-las
                    for x in range(len(predictions)):
                        # Se a distancia for menor, acreditasse que é um melhor vizinho
                        if (predictions[x][0][1] < oldPredictions[x][0][1]): 
                            predictions[x] = finalNeighbors
                else: # Se ainda não exisitem predições, define que as atuais são as melhores
                    oldPredictions = [] # Limpa a lista anterior
                    oldPredictions = predictions # Atribui a nova a atual
    
            predictions_len = len(predictions)        
            
            # Metricas de avaliação
            accuracy = getAccuracy(testSet=dataSet[test], predictions=predictions)# Verifica a acurácia para a parte de testes atual
            hp = getHp(testSet=dataSet[test], predictions=predictions) # hierarchical precision
            hr = getHr(testSet=dataSet[test], predictions=predictions) # hierarchical recall
            hf = getHf(testSet=dataSet[test], predictions=predictions) # hierarchical f-mesure
        
            # Soma os valores obtidos aos anteriores
            accuracy_ += accuracy
            hp_ += hp
            hr_ += hr
            hf_ += hf
        
            #showResults(metrics=[str(k), str(hf), str(hr), str(hp), str(accuracy)])
            # Depois de executar todas as [fold] vezes
            if (test == (len(dataSet)-1)):
            
                # Extrai a media dos valores obtidos 
                accuracy_ = accuracy_ / folds 
                hp_ = hp_ / folds
                hr_ = hr_ / folds
                hf_ = hf_ / folds
            
                strings_ = [str(db_name),str(db_test_num),str(split_method),str(random_seed),str(k),str(folds),str(test_len),str(train_len),str(predictions_len)]
                metrics_ = [str(k), str(hf_), str(hr_), str(hp_), str(accuracy_)]
            
                # Salva os resultados das medias das metricas de avaliação
                writeResultsMetrics(file_path_="results/",metrics=metrics_,strings=strings_)
            
                # Salva os resultados, se necessário        
                #writeResultsFile(file_path_="results/",strings=strings_,dataSet=dataSet,trainingSet=trainingSet,testSet=testSet,predictions=predictions)
                
                # Por fim, exibe os resultados conseguidos
                showResults(metrics=metrics_)
            #if test == False: break # Debug de teste para executar somente uma vez
        winsound.Beep(frequency, duration)

