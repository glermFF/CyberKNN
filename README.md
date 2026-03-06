# Classificação e Previsão de Ciberataques com ML

## Sobre
Este projeto de Ciência de Dados tem como objetivo analisar e classificar incidentes cibernéticos globais utilizando a base de dados do EuRepoC (European Repository of Cyber Incidents). Através do algoritmo de Machine Learning K-NN, o modelo é capaz de prever o tipo de um ataque cibernético (ex: *Data theft, Disruption, Hijacking*) com base em suas características de origem, alvo e método de atribuição.

O projeto foi desenvolvido com forte foco em boas práticas de modelagem, prevenção de vazamento de dados e avaliação robusta em bases desbalanceadas. Outros modelos além do K-NN serão testados por aqui.

---

## Pipeline do Projeto (Metodologia)

### 1. Análise Exploratória de Dados (EDA)
Análise temporal do volume global de ciberataques e a evolução das tendências das ameaças (foco no crescimento de ataques como Roubo de Dados e Interrupção de Sistemas na última década).

### 2. Pré-processamento e Limpeza
* Seleção de features relevantes (país atacante, país alvo, setor, etc.).
* Tratamento da variável alvo, removendo nulos e agrupando categorias de ataques raros (ruído estatístico).
* Tratamento de valores ausentes (NaN) nas features preenchendo com a categoria 'Desconhecido'.

### 3. Engenharia de Atributos (One-Hot Encoding)
Conversão de todas as variáveis categóricas em matrizes binárias (0 e 1), permitindo que o modelo matemático K-NN calcule as distâncias entre os incidentes de maneira precisa.

### 4. Treinamento e Otimização (Sem Vazamento de Dados)
* Separação inicial da base (80% Treino / 20% Teste).
* Aplicação do **GridSearchCV** utilizando *apenas os dados de treino* com validação cruzada interna (`cv=5`).

### 5. Avaliação e Validação Cruzada
O modelo campeão foi avaliado através de **Cross-Validation com 5 Folds** em 100% da base de dados, garantindo uma acurácia realista e à prova de viés.

---

## Resultados dos Testes

**Teste 06/03/26**
* Novas colunas de interesse adicionadas para ajudar um pouco na granularidade: 4 >>> 6.
* Incremento na precisão pelo Teste Simples: ~68% >>> ~72%.
* Incremento na precisão por Validação Cruzada: ~65% >>> ~68%.

**Teste 04/03/26**
* Remoção dos tipos de ataques menos recorrentes (Hijacking) deixando a apenas duas mais recorrentes Data theft e Disruption.
* Simplificação das colunas de interesse: 17 >>> 4.
* Incremento na precisão pelo Teste Simples: ~68%.
* Incremento na precisão por Validação Cruzada: ~60% >>> ~65%.

**Teste --/02/26**
* Acurácia Realista: O modelo obteve uma acurácia global consistente (~60%) após a Validação Cruzada.
* Diagnóstico de Desbalanceamento: Através da Matriz de Confusão, foi possível auditar o comportamento do modelo. Ele apresentou alta performance (bons F1-Scores) para as classes majoritárias como Data theft (Roubo de Dados) e Disruption (Interrupção).
* Limitação dos Registros: Devido a forma do pré-processamento aplicada, os registros de Hijacking (Sequestro) o modelo apresentou limitação ao categorizar, priorizando respostas estatisticamente mais prováveis em situações de dúvida.

**!!! O modelo apresentado ainda precisa de outras baterias de testes e definição das colunas de interesse correta para o problema a ser resolvido. Foram bons resultados mas apresentando grande desabalanceamento dos dados classificados !!!**
