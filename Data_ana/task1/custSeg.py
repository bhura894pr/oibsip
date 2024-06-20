import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv('ifood_df.csv')

print("Dataset Information:")
print(df.info())

df = df.dropna()

print("\nSummary Statistics:")
print(df.describe())

print("\nPerforming Exploratory Data Analysis (EDA)...")
sns.pairplot(df)
plt.show()

plt.figure(figsize=(15, 12))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

features = [
    'Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits',
    'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
    'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
    'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp4',
    'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Age',
    'Customer_Days', 'marital_Divorced', 'marital_Married', 'marital_Single',
    'marital_Together', 'marital_Widow', 'education_2n Cycle', 'education_Basic',
    'education_Graduation', 'education_Master', 'education_PhD', 'MntTotal',
    'MntRegularProds', 'AcceptedCmpOverall'
]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

kmeans = KMeans(n_clusters=5, random_state=42)  
clusters = kmeans.fit_predict(scaled_features)

df['Cluster'] = clusters

silhouette_avg = silhouette_score(scaled_features, clusters)
print(f'Silhouette Score: {silhouette_avg}')

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Income', y='MntTotal', hue='Cluster', palette='viridis', s=100)
plt.title('Customer Segments')
plt.xlabel('Income')
plt.ylabel('Total Amount Spent')
plt.legend(title='Cluster')
plt.show()

print("\nCluster Characteristics:")
cluster_summary = df.groupby('Cluster').mean()
print(cluster_summary)

