import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import kagglehub

#Buscamos el dataset que se encuentra en Kaggle llamado CPUs and GPUs
path = kagglehub.dataset_download("ghost5612/novel-covid-19-dataset")

#Nos aseguramos que la ruta que obtuvimos si nos llevara al archivo correcto
print("Ruta del dataset: ", path)

#Una vez que encontramos la ruta vemos que si hallamos encontrado el archivo que necesitamos
files = os.listdir(path)

#Seleccionamos unicamente el archivo 'covid_19_data.csv'
csv_file = os.path.join(path, "covid_19_data.csv")

#Ahora leeremos el CSV y utilizaremos df.head y df.tail en la siguiente seccion para ver si encontramos los primeros y ultimos 5 datos
df = pd.read_csv(csv_file)
df.head()