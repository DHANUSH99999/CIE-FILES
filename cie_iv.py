# -*- coding: utf-8 -*-
"""CIE IV

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j6p1Etv6kl516Smc-M2Ww6ADZcyRPqZV
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('/content/Mall_Customers.csv')

print("first five data :",df.head())
print('Shape of the dataset :',df.shape)
print('nature of data :',df.info())
print('Summary :',df.describe())
print('Checking null values :',df.isnull().sum())

x=df[['CustomerID','Annual Income (k$)','Age']]

sum_squared_distances=[]
k_values=range(1,11)

for k in k_values:
  kmeans=KMeans(n_clusters=k,random_state=42)
  kmeans.fit(x)
  sum_squared_distances.append(kmeans.inertia_)

#Visualization  of Clusters
plt.plot(k_values,sum_squared_distances,marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Sum squared distances")
plt.title("K_means clustering")
plt.show()