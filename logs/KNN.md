# Sobre

Conjunto dos resultados obtidos após ajustes e testes feitos no modelo KNN buscando amelhor eficiência possível para analisar a base de dados.

## Informações Gerais 

Colunas: 85
Colunas de Interesse Atuais: 7

- incident_type - String (coluna alvo)
- receiver_region - String
- receiver_category - String
- initiator_category - String
- impact_indicator_score - Numérico 
- mitre_initial_access - String
- user_interaction - String (adicionada)

-------------------------------

## Testes e Resultados do Modelo:

### KNN

**TESTE 1**
#---> Utilizando 17 colunas de interesse | 4 ataques principais:
**Perdi os dados**

| Incident Type            | Precision | Recall | F1-score | Support |
| ------------------------ | --------- | ------ | -------- | ------- |
| Data Theft               | -         | -      | -        | 1675    |
| Disruption               | -         | -      | -        | 1212    |
| Hijacking with Misuse    | -         | -      | -        | 197     |
| Hijacking without Misuse | -         | -      | -        | 326     |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | -        | 3410    |
| macro avg    | -         | -      | -        | 3410    |
| weighted avg | -         | -      | -        | 3410    |

**TESTE 2**
#---> Utilizando 4 colunas de interesse | 4 ataques principais:

=======================================

O melhor número de vizinhos (K) é: 11

O melhor sistema de pesos é: *uniform*

-> Acurácia no Teste Simples: **0.56891496**

=== RESULTADOS DO MODELO OTIMIZADO ===

Acurácia na Validação Cruzada: **0.53519062**

Relatório de Classificação Detalhado:

| Incident Type            | Precision | Recall | F1-score | Support |
| ------------------------ | --------- | ------ | -------- | ------- |
| Data Theft               | 0.57      | 0.70   | 0.63     | 1675    |
| Disruption               | 0.55      | 0.50   | 0.52     | 1212    |
| Hijacking with Misuse    | 0.11      | 0.08   | 0.09     | 197     |
| Hijacking without Misuse | 0.27      | 0.10   | 0.14     | 326     |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | 0.54     | 3410    |
| macro avg    | 0.38      | 0.34   | 0.35     | 3410    |
| weighted avg | 0.51      | 0.54   | 0.51     | 3410    |

**TESTE 3**
#---> Utilizando 4 colunas de interesse | 2 ataques principais:

=======================================

O melhor número de vizinhos (K) é: 7

O melhor sistema de pesos é: *distance*

-> Acurácia no Teste Simples: **0.68858131**

=== RESULTADOS DO MODELO OTIMIZADO ===

Acurácia na Validação Cruzada: **0.65327329**

Relatório de Classificação Detalhado:

| Incident Type | Precision | Recall | F1-score | Support |
| ------------- | --------- | ------ | -------- | ------- |
| Data Theft    | 0.69      | 0.73   | 0.71     | 1675    |
| Disruption    | 0.60      | 0.54   | 0.57     | 1212    |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | 0.65     | 2887    |
| macro avg    | 0.64      | 0.64   | 0.64     | 2887    |
| weighted avg | 0.65      | 0.65   | 0.65     | 2887    |

**TESTE 4**
#---> Utilizando 6 colunas de interesse | 2 ataques principais:

=======================================

O melhor número de vizinhos (K) é: 9

O melhor sistema de pesos é: *distance*

-> Acurácia no Teste Simples: **0.72318339**


=== RESULTADOS DO MODELO OTIMIZADO ===

Acurácia na Validação Cruzada: **0.68340838**

Relatório de Classificação Detalhado:

| Incident Type | Precision | Recall | F1-score | Support |
| ------------- | --------- | ------ | -------- | ------- |
| Data Theft    | 0.72      | 0.74   | 0.73     | 1675    |
| Disruption    | 0.63      | 0.60   | 0.61     | 1212    |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | 0.68     | 2887    |
| macro avg    | 0.67      | 0.67   | 0.67     | 2887    |
| weighted avg | 0.68      | 0.68   | 0.68     | 2887    |

**TESTE 5 - Base Desbalanceada**
#---> Utilizando 7 colunas de interesse | 4 ataques principais:

=======================================

O melhor número de vizinhos (K) é: 7

O melhor sistema de pesos é: *uniform*

-> Acurácia no Teste Simples: **0.63049853**


=== RESULTADOS DO MODELO OTIMIZADO ===

Acurácia na Validação Cruzada: **0.60263930**

Relatório de Classificação Detalhado:

| Incident Type            | Precision | Recall | F1-score | Support |
| ------------------------ | --------- | ------ | -------- | ------- |
| Data Theft               | 0.64      | 0.73   | 0.68     | 1675    |
| Disruption               | 0.60      | 0.54   | 0.56     | 1212    |
| Hijacking with Misuse    | 0.23      | 0.16   | 0.19     | 197     |
| Hijacking without Misuse | 0.55      | 0.45   | 0.50     | 326     |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | 0.60     | 3410    |
| macro avg    | 0.50      | 0.47   | 0.48     | 3410    |
| weighted avg | 0.59      | 0.60   | 0.59     | 3410    |

**TESTE 6 - Aplicando SMOTE**
#---> Utilizando 7 colunas de interesse | 4 ataques principais:

=======================================

O melhor número de vizinhos (K) é: 9

O melhor sistema de pesos é: *distance*

-> Acurácia no Teste Simples: **0.45601173**

=== RESULTADOS DO MODELO OTIMIZADO ===

Acurácia na Validação Cruzada: **0.60293255**

Relatório de Classificação Detalhado:

| Incident Type            | Precision | Recall | F1-score | Support |
| ------------------------ | --------- | ------ | -------- | ------- |
| Data Theft               | 0.64      | 0.73   | 0.68     | 1675    |
| Disruption               | 0.60      | 0.54   | 0.56     | 1212    |
| Hijacking with Misuse    | 0.23      | 0.16   | 0.19     | 197     |
| Hijacking without Misuse | 0.55      | 0.45   | 0.50     | 326     |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | 0.60     | 3410    |
| macro avg    | 0.50      | 0.47   | 0.48     | 3410    |
| weighted avg | 0.59      | 0.60   | 0.59     | 3410    |