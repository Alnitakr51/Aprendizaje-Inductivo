# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:36:35 2023

@author: Gadiel Jimenez
"""


#Arboles de decisión ID3

"""El árbol de decisión ID3 (Iterative Dichotomiser 3) es un algoritmo utilizado en el campo
de la inteligencia artificial y el aprendizaje automático para construir árboles de deci-
sión a partir de un conjunto de datos de entrenamiento. Fue propuesto por J. Ross Quinlan
en 1986.

El algoritmo ID3 se utiliza en problemas de clasificación, donde el objetivo es asignar
una etiqueta o clase a una instancia basándose en sus características. El árbol de deci
sión construido por el algoritmo ID3 representa una secuencia de decisiones que se toman
 en función de las características del dato de entrada, hasta llegar a una decisión final."""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#Carga el conjunto de datos de ejemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Divide el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Crea un clasificador de árbol de decisión
clf = DecisionTreeClassifier()

#Entrena el clasificador
clf.fit(X_train, y_train)

#Realiza predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

#Calcula la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador:", accuracy)