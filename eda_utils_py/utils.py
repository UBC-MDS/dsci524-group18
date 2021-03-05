from math import sqrt

# calculate means
def _calculate_means(dataset):
    means = [0 for _ in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / float(len(dataset))

    return means


# calculate standard deviation
def _calculate_stdevs(dataset, means):
    stdevs = [0 for _ in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance = [pow(row[i] - means[i], 2) for row in dataset]
        stdevs[i] = sum(variance)
    stdevs = [sqrt(x / float(len(dataset) - 1)) for x in stdevs]

    return stdevs


# scaled_value = (value - mean) / stdev
def _standardize_dataset(dataset, means, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]


# Find the min and max values for each column
def _dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax


# Rescale dataset columns to the range 0-1
# scaled_value = (value - min) / (mix - min)
def _minmax_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])