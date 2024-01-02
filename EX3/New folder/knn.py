import pandas as pd
from collections import Counter

def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (point1[i] - point2[i]) ** 2
    return round((squared_distance ** 0.5), 2)

def knn(X_train, y_train, X_test, k):
    distances_file = open("distances.txt", "w")
    result_file = open("result.txt", "w")
    y_pred = []
    for test_point in X_test:
        distances = [euclidean_distance(train_point, test_point) for train_point in X_train]
        sorted_indices = sorted(range(len(distances)), key=lambda k: distances[k])[:k]
        distances_file.write("================================================================================================\n")
        distances_file.write(f"Test point: {list(test_point)}\n")
        distances_file.write(f"All distances: {str(distances)}\n")
        distances_file.write(f"{k} nearest distances: {sorted_indices[:k]}\n")
        distances_file.write("================================================================================================\n")
        k_nearest_labels = [y_train[i] for i in sorted_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        prediction = most_common[0][0]
        y_pred.append(prediction)
        result_file.write(f"Class 0: {most_common[0][0]} Neighbour Points || Class 1: {most_common[0][1]} Neighbour Points || ")
        result_file.write(f"Predicted Class: {prediction}\n")
    distances_file.close()
    result_file.close()
    return y_pred

data = pd.read_csv("./diabetes.csv")
target_column = "Outcome"
feature_columns = [col for col in data.columns if col != target_column]
X = data[feature_columns].values
y = data[target_column].values
split_ratio = 0.7
split_index = int(len(X) * split_ratio)
X_train = X[:split_index]
y_train = y[:split_index]
X_test = X[split_index:]
y_test = y[split_index:]

k = 3
y_pred = knn(X_train, y_train, X_test, k)

accuracy = sum(y_pred[i] == y_test[i] for i in range(len(y_pred))) / len(y_pred)
print(f"Accuracy score: {accuracy*100:.2f}%")
