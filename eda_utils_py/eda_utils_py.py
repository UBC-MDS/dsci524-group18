def imputer(dataframe, strategy = "mean", fill_value):
    """
    A function to implement imputation functionality for completing missing values.

    Parameters
    ----------
    dataframe : pandas.DataFrame
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
    pandas.DataFrame 
        a dataframe that contains no missing data
    """
    

def cor_map(dataframe, num_col):
    """
    A function to implement a correlation heatmap including coefficients based on given numeric columns of a data frame.

    Args:
        dataframe (pandas.DataFrame): The data frame to be used for EDA.
        num_col (list):  A list of string of column names with numeric data from the data frame.

    Returns:
        (altair): A correlation heatmap plot with correlation coefficient labels based on the numeric columns specified by user.

    Examples: 
        import pandas as pd
        from eda_utils_py import cor_map

        data = pd.DataFrame({
            'SepalLengthCm':[5.1, 4.9, 4.7],
            'SepalWidthCm':[1.4, 1.4, 1.3],
            'PetalWidthCm:[0.2, 0.2, 0.2],
            'Species':['Iris-setosa','Iris-virginica']
        })

        numerical_columns = ['SepalLengthCm','SepalWidthCm','PetalWidthCm']
        
        cor_map(data, numerical_columns)
        
    """


def outlier_identifier(dataframe, columns=None, method="somefunction"):
    """
    A function that identify and deal with outliers based on the method the user choose

    Key arguments: 
        dataframe [pandas.DataFrame]: 
            The target dataframe where the function is performed.
        columns [list] : None
            The target columns where the function needed to be performed. Defualt is None, the function will check all columns
        method [string] : "somefunction"
            The method of dealing with outliers. 
        
    Returns:
        dataframe :
            The dataframe which the outlier has already process by the chosen method
    
    Examples:
        data = pd.DataFrame({
            'SepalLengthCm':[5.1, 4.9, 4.7],
            'SepalWidthCm':[1.4, 1.4, 9999999.99],
            'PetalWidthCm:[0.2, 0.2, 0.2],
            'Species':['Iris-setosa','Iris-virginica']
        })

        outlier_identifier(data)

    """


def scale(dataframe, columns=None):
    """
    A function to scale features by removing the mean and scaling to unit variance
.

    Args:
        dataframe (pandas.DataFrame): The data frame to be used for EDA.
        columns (list):  A list of string of column names with numeric data from the data frame that we wish to scale.

    Returns:
        dataframe :
            The scaled dataframe for numerical features

    Examples:
        import pandas as pd
        from eda_utils_py import scale

        data = pd.DataFrame({
            'SepalLengthCm':[5.1, 4.9, 4.7],
            'SepalWidthCm':[1.4, 1.4, 1.3],
            'PetalWidthCm:[0.2, 0.2, 0.2],
            'Species':['Iris-setosa','Iris-virginica']
        })

        numerical_columns = ['SepalLengthCm','SepalWidthCm','PetalWidthCm']

        scale(data, numerical_columns)

    """
    pass
