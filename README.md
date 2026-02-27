# Classificação e Previsão de Ciberataques com IA (K-NN)

## Sobre
Este projeto de Ciência de Dados tem como objetivo analisar e classificar incidentes cibernéticos globais utilizando a base de dados do EuRepoC (European Repository of Cyber Incidents). Através do algoritmo de Machine Learning K-NN, o modelo é capaz de prever o tipo de um ataque cibernético (ex: *Data theft, Disruption, Hijacking*) com base em suas características de origem, alvo e método de atribuição.

O projeto foi desenvolvido com forte foco em boas práticas de modelagem, prevenção de vazamento de dados (*Data Leakage*) e avaliação robusta em bases desbalanceadas.

---

## Pipeline do Projeto (Metodologia)

### 1. Análise Exploratória de Dados (EDA)
Análise temporal do volume global de ciberataques e a evolução das tendências das ameaças (foco no crescimento de ataques como Roubo de Dados e Interrupção de Sistemas na última década).

### 2. Pré-processamento e Limpeza
* Seleção de features relevantes (país atacante, país alvo, setor, etc.).
* Tratamento da variável alvo, removendo nulos e agrupando categorias de ataques raros (ruído estatístico).
* Tratamento de valores ausentes (NaN) nas features preenchendo com a categoria 'Desconhecido'.

### 3. Engenharia de Atributos (One-Hot Encoding)
Conversão de todas as variáveis categóricas em matrizes binárias (0 e 1) utilizando `pd.get_dummies()`, permitindo que o modelo matemático K-NN calcule as distâncias entre os incidentes perfeitamente.

### 4. Treinamento e Otimização (Sem Vazamento de Dados)
* Separação inicial da base (80% Treino / 20% Teste).
* Aplicação do **GridSearchCV** utilizando *apenas os dados de treino* com validação cruzada interna (`cv=5`). Isso garantiu a descoberta do melhor hiperparâmetro (K) sem que o modelo "roubasse" olhando o gabarito dos dados de teste.

### 5. Avaliação e Validação Cruzada
O modelo campeão foi avaliado através de **Cross-Validation com 5 Folds** em 100% da base de dados, garantindo uma acurácia realista e à prova de viés.

### 6. Exportação para Produção
O "cérebro" do modelo otimizado e a estrutura exata de colunas do pré-processamento foram exportados em arquivos `.pkl` usando a biblioteca `joblib`, prontos para serem integrados a outros sistemas ou APIs.

---

## Principais Resultados e Insights

* Acurácia Realista: O modelo obteve uma acurácia global consistente (~60%) após a Validação Cruzada em toda a base.
* Diagnóstico de Desbalanceamento: Através da Matriz de Confusão, foi possível auditar o comportamento da IA. O modelo apresentou alta performance (bons F1-Scores) para as classes majoritárias como Data theft (Roubo de Dados) e Disruption (Interrupção). 
* Limitações do Mundo Real: Como a base possui pouquíssimos registros de Hijacking (Sequestro), o modelo reflete essa limitação do mundo real, priorizando respostas estatisticamente mais prováveis em situações de dúvida.

**!!! O modelo apresentado ainda precisa de outras baterias de testes e definição das colunas de interesse correta para o problema a ser resolvido. Foram bons resultados mas apresentando grande desabalanceamento dos dados classificados !!!**

---

## Como rodar este projeto na sua máquina

1. Clone este repositório:
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
