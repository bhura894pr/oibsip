import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv('WineQT.csv')
print("Dataset Information:")
print(df.info())

df = df.dropna()
print("\nSummary Statistics:")
print(df.describe())

print("\nPerforming Exploratory Data Analysis (EDA)...")
sns.pairplot(df, hue='quality')
plt.show()

plt.figure(figsize=(15, 12))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

X = df.drop(['quality', 'Id'], axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nRandom Forest Classifier:")
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf)}")
print(classification_report(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))

print("\nStochastic Gradient Descent Classifier:")
sgd = SGDClassifier(random_state=42)
sgd.fit(X_train_scaled, y_train)
y_pred_sgd = sgd.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred_sgd)}")
print(classification_report(y_test, y_pred_sgd))
print(confusion_matrix(y_test, y_pred_sgd))

print("\nSupport Vector Classifier:")
svc = SVC(random_state=42)
svc.fit(X_train_scaled, y_train)
y_pred_svc = svc.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred_svc)}")
print(classification_report(y_test, y_pred_svc))
print(confusion_matrix(y_test, y_pred_svc))

models = ['Random Forest', 'SGD', 'SVC']
accuracies = [accuracy_score(y_test, y_pred_rf), accuracy_score(y_test, y_pred_sgd), accuracy_score(y_test, y_pred_svc)]

plt.figure(figsize=(10, 6))
sns.barplot(x=models, y=accuracies)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()
