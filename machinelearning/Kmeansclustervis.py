# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # Take only the first two features for visualization
y = iris.target

# Create a KMeans classifier
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the classifier
kmeans.fit(X)

# Predict cluster labels for the data points
y_kmeans = kmeans.predict(X)

# Visualize the clusters and centroids
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap=ListedColormap(('red', 'green', 'blue')), edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='yellow', marker='X', edgecolor='k')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("K-means Clustering (Iris Dataset)")
plt.show()
