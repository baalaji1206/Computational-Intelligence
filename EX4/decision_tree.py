import pandas as pd
import math

def calculate_counts(data, column):
    counts = data[column].value_counts().to_dict()
    return counts

def calculate_entropy(counts):
    total_count = sum(counts.values())
    entropy = 0
    for count in counts.values():
        probability = count / total_count
        entropy -= probability * math.log2(probability)
    return round(entropy, 3)

# def calculate_column_entropy(data, column):
#     counts = calculate_counts(data, column)
#     entropy = calculate_entropy(counts)
#     return entropy, counts

def calculate_information_gain(data, column, target):
    dataset_entropy = calculate_entropy(calculate_counts(data, target))
    
    unique_values = data[column].unique()
    weighted_entropies = 0
    for value in unique_values:
        subset = data[data[column] == value]
        subset_entropy = calculate_entropy(calculate_counts(subset, target))
        weighted_entropies += (len(subset) / len(data)) * subset_entropy
    
    information_gain = dataset_entropy - weighted_entropies
    return round(information_gain, 3)

def find_root_node(data, target, column_names, excluded_columns):
    max_info_gain = -1
    root_column = None
    
    for column in column_names:
        if column not in excluded_columns and column != target:
            info_gain = calculate_information_gain(data, column, target)
            if info_gain > max_info_gain:
                max_info_gain = info_gain
                root_column = column
    
    return root_column

data = pd.read_csv('./play_tennis.csv')
target_column = data.columns[-1]
column_names = data.columns[1:-1]
excluded_columns = ['Day']

dataset_entropy = calculate_entropy(calculate_counts(data, target_column))
print("Entropy of Entire Dataset = ", dataset_entropy)
print(f"Yes count: {calculate_counts(data, target_column).get('Yes', 0)}")
print(f"No count: {calculate_counts(data, target_column).get('No', 0)}")
print()

for column in column_names:
    print(f"Split: {column}")
    print(f"{column} Count:", calculate_counts(data, column))
    unique_values = data[column].unique()
    for value in unique_values:
        subset = data[data[column] == value]
        subset_counts = calculate_counts(subset, target_column)
        print(f"Counts for {column} = {value}: {subset_counts}")
        print(f"Entropy of {column} = {value}: {calculate_entropy(calculate_counts(subset, target_column))}\n")
    
    info_gain = calculate_information_gain(data, column, target_column)
    print(f"Information Gain of {column} = ",info_gain)
    
    print()

root_node = find_root_node(data, target_column, column_names, excluded_columns)
print(f"Root Node of the decision tree is: {root_node}")
