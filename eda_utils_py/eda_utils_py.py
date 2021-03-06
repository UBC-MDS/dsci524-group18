import pandas as pd
import altair as alt
from pandas.api.types import is_numeric_dtype
import numpy as np


def imputer(dataframe, strategy="mean", fill_value=None):
    """
    A function to implement imputation functionality for completing missing values.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        a dataframe that might contain missing data
    strategy : string, default="mean"
        The imputation strategy.
            - If “mean”, then replace missing values using the mean along each column. Can only be used with numeric data.
            - If “median”, then replace missing values using the median along each column. Can only be used with numeric data.
            - If “most_frequent”, then replace missing using the most frequent value along each column. Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.
            - If “constant”, then replace missing values with fill_value. Can be used with strings or numeric data.
    fill_value : string or numerical value, default=None
        When strategy == “constant”, fill_value is used to replace all occurrences of missing_values. If left to the default, fill_value will be 0 when imputing numerical data and “missing_value” for strings or object data types.
        
    Returns
    -------
    pandas.core.frame.DataFrame
        a dataframe that contains no missing data
        
    Examples
    ---------
    >>> import pandas as pd
    >>> from eda_utils_py import cor_map
    
    >>> data = pd.DataFrame({
    >>>     'SepalLengthCm':[5.1, 4.9, 4.7],
    >>>     'SepalWidthCm':[1.4, 1.4, 1.3],
    >>>     'PetalWidthCm':[0.2, None, 0.2]
    >>> })

    >>> imputer(data, numerical_columns)
       SepalLengthCm  SepalWidthCm  PetalWidthCm
    0            5.1           1.4           0.2
    1            4.9           1.4           0.2
    2            4.7           1.3           0.2
    """
    pass


def cor_map(dataframe, num_col):
    """
    A function to implement a correlation heatmap including coefficients based on given numeric columns of a data frame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The data frame to be used for EDA.
    num_col : list  
        A list of string of column names with numeric data from the data frame.

    Returns
    -------
    altair.vegalite.v4.api.Chart
        A correlation heatmap plot with correlation coefficient labels based on the numeric columns specified by user.

    Examples
    ---------
    >>> import pandas as pd
    >>> from eda_utils_py import cor_map
    
    >>> data = pd.DataFrame({
    >>>     'SepalLengthCm':[5.1, 4.9, 4.7],
    >>>     'SepalWidthCm':[1.4, 1.4, 1.3],
    >>>     'PetalWidthCm':[0.2, 0.2, 0.2],
    >>>     'Species':['Iris-setosa','Iris-virginica', 'Iris-germanica']
    >>> })

    >>> numerical_columns = ['SepalLengthCm','SepalWidthCm','PetalWidthCm']    
    >>> cor_map(data, numerical_columns)
        
    """
    pass


def outlier_identifier(dataframe, columns=None, method="trim"):
    """
    A function that identify by z-test with threshold of 3, and deal with outliers based on the method the user choose

    Parameters
    ---------- 
    dataframe : pandas.core.frame.DataFrame
        The target dataframe where the function is performed.
    columns : list, default=None
        The target columns where the function needed to be performed. Defualt is None, the function will check all columns
    method : string
        The method of dealing with outliers. 
            - if "trim" : we completely remove data points that are outliers.
            - if "median" : we replace outliers with median values
            - if "mean" : we replace outliers with mean values
        
    Returns
    -------
    pandas.core.frame.DataFrame
        a dataframe which the outlier has already process by the chosen method
    
    Examples
    --------
    >>> import pandas as pd
    >>> from eda_utils_py import cor_map
        
    >>> data = pd.DataFrame({
    >>>    'SepalLengthCm':[5.1, 4.9, 4.7],
    >>>    'SepalWidthCm':[1.4, 1.4, 9999999.99],
    >>>    'PetalWidthCm:[0.2, 0.2, 0.2],
    >>>    'Species':['Iris-setosa', 'Iris-virginica', 'Iris-germanica']
    >>> })

    >>> outlier_identifier(data)

    """

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The argument @dataframe must be of pd.DataFrame")

    if columns is not None:
        if not isinstance(columns, list):
            raise TypeError("The argument @columns must be of type list")
        
        for col in columns:
            if col not in list(dataframe.columns):
                raise Exception("The given column list contains column that is not exist in the given dataframe.")    
            if not is_numeric_dtype(dataframe[col]):
                raise Exception("The given column list contains column that is not numeric column.")
 
    if method not in ("trim", "median", "mean"):
        raise Exception("The method must be -trim- or -median- or -mean-")

    
    target_columns = []
    if(columns is None):
        target_columns = list(dataframe.columns.values.tolist()) 
        
    

    outlier_index = []
    for column in target_columns:
        current_column = dataframe[column]
        mean = np.mean(current_column)
        std = np.std(current_column)
        threshold = 3 
        
        for i in range(len(current_column)):
            current_item = current_column[i]
            z = (current_item - mean) / std
            if z >= threshold:
                if(i not in outlier_index):
                    outlier_index.append(i)
                if(method == "median"):
                    dataframe[column][i] = np.median(current_column)
                if(method == "mean"):
                    dataframe[column][i] = np.mean(current_column)
    
    if(method == "trim"):
        dataframe = dataframe.drop(outlier_index)

    return dataframe


def scale(dataframe, columns=None):
    """
    A function to scale features by removing the mean and scaling to unit variance

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The data frame to be used for EDA.
    columns : list, default=None
        A list of string of column names with numeric data from the data frame that we wish to scale.

    Returns
    -------
    dataframe : pandas.core.frame.DataFrame
        The scaled dataframe for numerical features

    Examples
    --------
    >>> import pandas as pd
    >>> from eda_utils_py import scale
    
    >>> data = pd.DataFrame({
    >>>     'SepalLengthCm':[5.1, 4.9, 4.7],
    >>>     'SepalWidthCm':[1.4, 1.4, 1.3],
    >>>     'PetalWidthCm:[0.2, 0.2, 0.2],
    >>>     'Species':['Iris-setosa','Iris-virginica', 'Iris-germanica']
    >>> })

    >>> numerical_columns = ['SepalLengthCm','SepalWidthCm','PetalWidthCm']
    
    >>> scale(data, numerical_columns)
    """
    pass
