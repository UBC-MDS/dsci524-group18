from math import sqrt


# calculate means
def _calculate_means(dataframe):
    means = [0 for _ in range(len(dataframe[0]))]
    for i in range(len(dataframe[0])):
        col_values = [row[i] for row in dataframe]
        means[i] = sum(col_values) / float(len(dataframe))

    return means


# calculate standard deviation
def _calculate_stdevs(dataframe, means):
    stdevs = [0 for _ in range(len(dataframe[0]))]
    for i in range(len(dataframe[0])):
        variance = [pow(row[i] - means[i], 2) for row in dataframe]
        stdevs[i] = sum(variance)
    stdevs = [sqrt(x / float(len(dataframe) - 1)) for x in stdevs]

    return stdevs


# scaled_value = (value - mean) / stdev
def _standardize(dataframe, means, stdevs):
    """Transform features by rescaling each feature to the range between 0 and 1.
    The transformation is given by:

        scaled_value = (feature_value - min) / (mix - min)

    where min, max = feature_range.

    This transformation is often used as an alternative to zero mean,
    unit variance scaling.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The data frame to be used for EDA.
    minmax : object
        The array returned from def _get_dataset_minmax(dataset)
    Returns
    -------
    self : object
        Scaled dataset
    """
    for row in dataframe:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]


def _get_dataframe_minmax(dataframe):
    """Compute the minimum and maximum for each feature in the dataset, to be used for later scaling.
    Parameters
    ----------
    dataframe : pandas.DataFrame
        The data frame to be used for EDA.
    Returns
    -------
    minmax : list
        An array of minimum and maximum values
    """
    minmax = []
    for i in range(len(dataframe[0])):
        col_values = [row[i] for row in dataframe]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax


def _minmax(dataframe, minmax):
    """Transform features by rescaling each feature to the range between 0 and 1.
    The transformation is given by:

        scaled_value = (feature_value - min) / (mix - min)

    where min, max = feature_range.
    
    This transformation is often used as an alternative to zero mean,
    unit variance scaling.
    
    Parameters
    ----------
    dataframe : pandas.DataFrame
        The data frame to be used for EDA.
    minmax : object
        The array returned from def _get_dataset_minmax(dataset)
    Returns
    -------
    self : object
        Scaled dataset
    """
    for row in dataframe:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
