import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
online_retail_data = pd.read_csv('OnlineRetail-test1.csv')
online_retail_data.dropna(inplace=True)
X = online_retail_data[['Quantity', 'UnitPrice']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
inertia = []
for n_clusters in range(1, 11):
   kmeans = KMeans(n_clusters=n_clusters, random_state=42)
   kmeans.fit(X_pca)
   inertia.append(kmeans.inertia_)
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.show()