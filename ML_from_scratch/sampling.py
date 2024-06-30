import numpy as np


def uniform_sampling(data, sample_size):
    return np.random.choice(data, sample_size, replace=False)

# O(N) O(K)
def reservoir_sampling(data, sample_size):
    """
    Reservoir sampling is used for sampling k elements from a large or unknown data stream 
    where you don't know the size of the data beforehand.
    """
    reservisor = []
    for i in range(sample_size):
        reservisor.append(data[i])
    
    for i in range(sample_size, len(data)):
        j = np.random.randint(0, i)
        if j < sample_size:
            reservisor[j] = data[i]
    
    return reservisor


def stratified_sampling(data, labels, sample_size):
    """
    1. Divide the dataset into strata based on the labels.
    2. Determine the number of samples to draw from each stratum. (Same proportion/number for each class)
    3. Randomly sample from each stratum.
    """
    unique_labels, label_counts = np.unique(labels, return_counts=True)
    proportions = label_counts / len(data)
    stratified_counts = (proportions * sample_size).astype(int)
    stratified_counts[-1] = sample_size - stratified_counts[:-1].sum()
    stratified_sample = []
    stratified_label = []
    
    for label, sub_count in zip(unique_labels, stratified_counts):
        sub_data_idx = np.where(labels == label)[0]
        sub_sample_idx = np.random.choice(sub_data_idx, sub_count, replace=False)
        
        stratified_sample.extend(data[sub_sample_idx])
        stratified_label.extend(labels[sub_sample_idx])
    
    return np.array(stratified_sample), np.array(stratified_label)


def k_flod(data, labels, k=5):
    idx = list(range(len(data)))
    np.random.shuffle(idx)
    k_fold_result = []
    test_size = len(data) // k

    for i in range(k):
        test_data_idx = idx[i * test_size: (i + 1) * test_size]
        train_data_idx = idx[: i * test_size] + idx[(i + 1) * test_size: ]
        k_fold_result.append([data[train_data_idx], data[test_data_idx], labels[train_data_idx], labels[test_data_idx]])

    return k_fold_result


if __name__ == '__main__':
    # Uniform Sample
    data = np.array([i for i in range(100)])
    sample_size = 10
    uniform_sample = uniform_sampling(data, sample_size)
    print("Uniform Sample:", uniform_sample)

    # Reservoir Sample
    uniform_sample = reservoir_sampling(data, sample_size)
    print("Reservoir Sample:", uniform_sample)
    
    data = np.array([i for i in range(100)])
    labels = np.array([i % 3 for i in range(100)]) # 3 classes
    sample_size = 10
    stratified_sample, stratified_sample_labels = stratified_sampling(data, labels, sample_size)
    print("Stratified Sample:", stratified_sample)
    print("Stratified Sample Labels:", stratified_sample_labels)

    k_fold_result = k_flod(data, labels, k=5)
    print('1st result of K fold', k_fold_result[0])
