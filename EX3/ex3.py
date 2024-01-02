import pandas as pd
import math

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (float(point1[i]) - float(point2[i])) ** 2
    return math.sqrt(distance)

def knn(train_data, new_data, k):
    distances = []
    for index, row in train_data.iterrows():
        dist = euclidean_distance(row[new_data.columns], new_data.values.tolist()[0])
        distances.append((index, dist))

    distances.sort(key=lambda x: x[1])  # Sort distances in ascending order

    print("\nEuclidean Distances:")
    for i, (_, dist) in enumerate(distances, start=1):
        print(f"D{i}: {dist:.4f}")

    neighbors = [train_data.iloc[i] for i, _ in distances[:k]]

    print("\nCounts:")
    print()
    #for rank, neighbor in enumerate(neighbors, start=1):
     #   label = neighbor.iloc[-1]  # Last column is the target
      #  print(f"Rank {rank}: {label}")

    class_counts = {}
    for neighbor in neighbors:
        label = neighbor.iloc[-1]  # Last column is the target
        if label in class_counts:
            class_counts[label] += 1
        else:
            class_counts[label] = 1
    print(class_counts)
    print()
    predicted_label = max(class_counts, key=class_counts.get)
    return predicted_label

def main():
    filename = input("Enter the dataset filename: ")
    data = pd.read_csv(filename)

    print("\nAvailable features:")
    for index, feature in enumerate(data.columns[:-1]):
        print(f"{index + 1}. {feature}")

    feature_indices = input("Selected features index: ").split(',')
    selected_features = [data.columns[int(index) - 1] for index in feature_indices]
    new_data = data[selected_features]

    new_data_values = []
    for feature in selected_features:
        value = float(input(f"Enter value for {feature}: "))
        new_data_values.append(value)

    new_data = pd.DataFrame([new_data_values], columns=selected_features)
    k=1
    while(k!=0):
        k = int(input("Enter the value of K: "))
        if(k!=0):
            predicted_target = knn(data, new_data, k)
            print(f"\nPredicted Target: {predicted_target}")
        print()
    
if __name__ == "__main__":
    main()
