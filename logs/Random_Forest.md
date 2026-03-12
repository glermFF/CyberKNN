# Sobre

Conjunto dos resultados obtidos após ajustes e testes feitos no modelo Random Forest buscando a melhor eficiência possível para analisar a base de dados.

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

**TESTE 1**

#---> Utilizando 7 colunas de interesse | 4 ataques principais:

Melhores parâmetros: 'max_depth': None, 'n_estimators': 100

Acurácia no Teste Simples: **0.68035191**

=======================================

=== RESULTADOS DO RANDOM FOREST ===

-> Acurácia na Validação Cruzada: **0.62844575**

Relatório de Classificação Detalhado:

| Incident Type            | Precision | Recall | F1-score | Support |
| ------------------------ | --------- | ------ | -------- | ------- |
| Data Theft               | 0.67      | 0.73   | 0.70     | 1675    |
| Disruption               | 0.62      | 0.61   | 0.61     | 1212    |
| Hijacking with Misuse    | 0.25      | 0.14   | 0.18     | 197     |
| Hijacking without Misuse | 0.56      | 0.47   | 0.51     | 326     |

| ---          | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| accuracy     | -         | -      | 0.63     | 3410    |
| macro avg    | 0.52      | 0.49   | 0.50     | 3410    |
| weighted avg | 0.62      | 0.63   | 0.62     | 3410    |