def _standardize(dataframe):
    """Transform features by centering the distribution of the data
    on the value 0 and the standard deviation to the value 1.

    The transformation is given by:

        scaled_value = (value - mean) / standard deviation

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The data frame to be used for EDA.
    Returns
    -------
    self : object
        Scaled dataset
    """
    for feature_name in dataframe.columns:
        mean = dataframe[feature_name].mean()
        stdev = dataframe[feature_name].std()
        dataframe[feature_name] = (dataframe[feature_name] - mean) / stdev
    return dataframe


def _minmax(dataframe):
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
        Returns
        -------
        self : object
            Scaled dataset
        """
    for feature_name in dataframe.columns:
        max = dataframe[feature_name].max()
        min = dataframe[feature_name].min()
        dataframe[feature_name] = (dataframe[feature_name] - min) / (max - min)
    return dataframe
