
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


def outlier_identifier(dataframe, columns = None, method = "somefunction"):
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