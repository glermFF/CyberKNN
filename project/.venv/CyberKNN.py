import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV, cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import classification_report, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split


try:
  dataset = pd.read_csv('./eurepoc_global_dataset_1_3.csv')
  print(f"Tamanho original da base: {dataset.shape}")
  print(dataset.head())
except Exception as e:
  print(f'Error reading file "{dataset}": {e}')

colunas_de_interesse = [
  'incident_type',
  'receiver_regions',
  'receiver_category',
  'initiator_category',
  'mitre_initial_access',
  'impact_indicator_score',
  'user_interaction'
]

df_modelo = dataset[colunas_de_interesse].copy()
df_modelo.head()

df_modelo = df_modelo.dropna(subset=['incident_type'])
df_modelo = df_modelo[df_modelo['incident_type'] != 'Not available']

df_modelo['impact_indicator_score'] = df_modelo['impact_indicator_score'].fillna(0)

print(df_modelo['incident_type'])

# Simplificando as classes
for coluna in ['incident_type', 'receiver_category', 'mitre_initial_access']:
  df_modelo[coluna] = df_modelo[coluna].apply(lambda x: str(x).split(';')[0].strip())
  df_modelo[coluna] = df_modelo[coluna].apply(lambda x: str(x).split('&')[0].strip())

df_modelo['receiver_category'] = df_modelo['receiver_category'].apply(lambda x: str(x).split(';')[0].strip())
df_modelo['receiver_category'] = df_modelo['receiver_category'].apply(lambda x: str(x).split('/')[0].strip())

# Remover classes raras
contagem_classes = df_modelo['incident_type'].value_counts()
classes_frequentes = contagem_classes[contagem_classes >= 5].index
df_modelo = df_modelo[df_modelo['incident_type'].isin(classes_frequentes)]

print("Distribuição das novas classes simplificadas:")
print(df_modelo['incident_type'].value_counts())

X = df_modelo.drop(columns=['incident_type'])
y = df_modelo['incident_type']

X = X.fillna('Desconhecido').replace('Not available', 'Desconhecido')
X = X.astype(str)

X_codificado = pd.get_dummies(X, drop_first=True)
X_codificado = X_codificado.fillna(0) 


print(f"Tamanho após pré-processamento (X): {X_codificado.shape}")

X_treino, X_teste, y_treino, y_teste = train_test_split(X_codificado, y, test_size=0.2, random_state=42)

print("Iniciando o GridSearch... Treinando múltiplos modelos...\n")

# Para o KNN
parametros_knn = {
    'n_neighbors': [1, 3, 5, 7, 9],
    'weights': ['uniform', 'distance']
}

# Para o Random Forest
parametros_rf = {
    'n_estimators': [100, 200],
    'max_depth': [None],
}

folds = 5

def knn_model_base(X_train, y_train, X_teste, y_teste):
    knn_base = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    knn_base.fit(X_train, y_train)
    y_pred_teste_base = knn_base.predict(X_teste)
    print("=" * 50)   
    print("\n=== RESULTADOS DO MODELO BASE ===")
    print(f"Vizinhos: {knn_base.get_params()['n_neighbors']}")
    print(f"Acurácia no Teste Simples: {accuracy_score(y_teste, y_pred_teste_base):.8f}")
    print("=" * 50)

def knn_model_cv(X_train, y_train, X_teste, y_teste):
    global y_pred_cross_val, melhor_modelo

    knn_base = KNeighborsClassifier()

    grid_search = GridSearchCV(
        estimator= knn_base,
        param_grid= parametros_knn,
        cv=5,
        scoring='accuracy',
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)

    # Resultados do melhor vizinho
    melhor_vizinho = grid_search.best_params_['n_neighbors']
    melhor_peso = grid_search.best_params_['weights']

    melhor_modelo = grid_search.best_estimator_

    y_pred_teste_simples = melhor_modelo.predict(X_teste)

    print("=" * 50)
    print(f"O melhor número de vizinhos (K) é: {melhor_vizinho}")
    print(f"O melhor sistema de pesos é: {melhor_peso}")
    print(f"Acurácia no Teste Simples: {accuracy_score(y_teste, y_pred_teste_simples):.8f}")
    print("=" * 50)

    print("\n")

    # Cross Validation
    y_pred_cross_val = cross_val_predict(melhor_modelo, X_codificado, y, cv=5)

    # Avaliação Final do KNN
    print("=== RESULTADOS DO MODELO OTIMIZADO ===")
    print(f"Acurácia na Validação Cruzada: {accuracy_score(y, y_pred_cross_val):.8f}")
    print("\nRelatório de Classificação Detalhado:\n")
    print(classification_report(y, y_pred_cross_val))

def random_forest(X_treino, X_teste, y_treino, y_teste, folds):
    rf_base = RandomForestClassifier(random_state=42, n_jobs=-1)

    grid_search = GridSearchCV(
        estimator=rf_base,
        param_grid=parametros_rf,
        cv=folds,
        scoring='accuracy',
        n_jobs=-1
    )
    
    grid_search.fit(X_treino, y_treino)

    # Resultados
    melhor_modelo_rf = grid_search.best_estimator_
    y_pred_teste = melhor_modelo_rf.predict(X_teste)

    print(f"Melhores parâmetros: {grid_search.best_params_}")
    print(f"Acurácia no Teste Simples: {accuracy_score(y_teste, y_pred_teste):.8f}")
    print("-" * 50)

    # Validação cruzada (Agora usando o RF)
    y_pred_cross_val = cross_val_predict(melhor_modelo_rf, X_codificado, y, cv=folds)

    print("\n=== RESULTADOS DO RANDOM FOREST ===")
    print(f"Acurácia na Validação Cruzada: {accuracy_score(y, y_pred_cross_val):.8f}")
    print("\nRelatório de Classificação Detalhado:\n")
    print(classification_report(y, y_pred_cross_val))

random_forest(X_treino, X_teste, y_treino, y_teste, folds)

knn_model_cv(X_treino, y_treino, X_teste, y_teste)

matriz_confusao = confusion_matrix(y, y_pred_cross_val)

nomes_das_classes = melhor_modelo.classes_

plt.figure(figsize=(10, 7))

sns.heatmap(matriz_confusao, annot=True, fmt='d', cmap='Blues', xticklabels=nomes_das_classes, yticklabels=nomes_das_classes)
plt.title('Matriz de Confusão (Cross-Validation) - Base Completa', fontsize=16, pad=20)
plt.xlabel('O que o Modelo Previu', fontsize=12, labelpad=10)
plt.ylabel('O Ataque que Realmente Aconteceu', fontsize=12, labelpad=10)

plt.tight_layout()
plt.show()