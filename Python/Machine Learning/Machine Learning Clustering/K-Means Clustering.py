# K-Means clustering is modeling around a centroid of a data cluster.  
# Centroids are initialized at random, but they are weighted, so cluster traps are minimized

# In this example we are predicting the cluster of mall customers with certain features

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
# We can only visualize two features of clusters (x and y axis) so we can only choose two features to analyze (income and spending score - columns 3 and 4)
dataset = pd.read_csv('Machine Learning Clustering\Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values

# Use the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
# trying 1-10 clusters is standard, random state 42 is random
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# The WCSS equation determines that the optimal number of clusters is 5, random state 42 is random
# Train the K-means model on the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

# Visualize the Clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()