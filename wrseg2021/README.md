# Overview

Neste trabalho, apresentamos a realização da reprodução dos 3 níveis de corte de permissões SigPID, implementação e avaliação dos principais métodos de aprendizagem do SigPID, utilizando um conjunto de dados publicamente disponível. Nós comparamos as permissões em cada nível de corte com as 32 permissões identificadas como mais recorrentes; as 113 do conjunto de dados público escolhido e as 22 permissões (contidas no conjunto de dados), consideradas perigosas pela Google. Nosso estudo inicial indica que o número de permissões impacta o tempo de treinamento e execução, bem como a acurácia dos modelos. Entretanto, o tempo de execução pode não ser significativo a ponto de justificar um número menor de permissões para detecção de malwares.


##  Tecnologias utilizadas
- Jupyter Notebook (IPython 7.12.0, Python 3.7.6 (default, Jan 8 2020)
- Google Chrome Versão 91.0.4472.124 (Versão oficial) 64 bits
- Weka versão 3.8.5
##  Bibliotecas utilizadas
- Pandas versão 1.2.4
- Matplotlib 3.4.0
- Numpy 1.20.1
- Scikit-learn versão 0.22.1
- Apyori 1.1.2
- Mlxtend 0.19.0

## **Algoritmos de Machine Learning**
- Random forest
- Decision tree
- Support vector machines (SVM)
- Functional Trees
Os hiper-parâmetros são variáveis que controlam o próprio processo de treinamento e foram definidos como **padrão** referente a versão 0.22.1 da biblioteca Scikit-learn. Por exemplo:

|    Algoritmos  |hiper-parâmetros             |
|----------------|-----------------------------|
|Random forest   |_n_estimators=100_, _*_, _criterion='gini'_, _max_depth=None_, _min_samples_split=2_, _min_samples_leaf=1_, _min_weight_fraction_leaf=0.0_, _max_features='auto'_, _max_leaf_nodes=None_, _min_impurity_decrease=0.0_, _min_impurity_split=None_, _bootstrap=True_, _oob_score=False_, _n_jobs=None_, _random_state=None_, _verbose=0_, _warm_start=False_, _class_weight=None_, _ccp_alpha=0.0_, _max_samples=None_           |
|Decision tree         |_criterion='gini'_, _splitter='best'_, _max_depth=None_, _min_samples_split=2_, _min_samples_leaf=1_, _min_weight_fraction_leaf=0.0_, _max_features=None_, _random_state=None_, _max_leaf_nodes=None_, _min_impurity_decrease=0.0_, _min_impurity_split=None_, _class_weight=None_, _ccp_alpha=0.0_ |
|SVM|_C=1.0_, _kernel='linear'_, _degree=3_, _gamma='scale'_, _coef0=0.0_, _shrinking=True_, _probability=False_, _tol=0.001_, _cache_size=200_, _class_weight=None_, _verbose=False_, _max_iter=- 1_, _decision_function_shape='ovr'_, _break_ties=False_, _random_state=None_|
**Obs:** Functional Tree  foi implementado utilizando a proposta de [Gama-2004](https://link.springer.com/content/pdf/10.1023/B:MACH.0000027782.67192.13.pdf) utilizando a ferramenta Weka versão 3.8.5, pois não possui biblioteca em Scikit-learn.

##  Ambientes de execução
Para execução foi utilizado um notebook com processador Intel Celeron 1007U (1.5GHz, Dual Core, 2MB L2), 4GB DDR3 1.600MHz, disco rígido de 320GB (SATA - 5.400rpm), Windows 10 Home Single Language, compilação 19042.1110.