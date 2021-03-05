import pandas as pd
import altair as alt
from pandas.api.types import is_numeric_dtype

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
    fill_value : numerical value, default=None
        When strategy == “constant”, fill_value is used to replace all occurrences of missing_values. If left to the default, fill_value will be 0 when imputing numerical data.
        
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


def cor_map(dataframe, num_col, col_scheme = 'purpleorange'):
    
    """
    A function to implement a correlation heatmap including coefficients based on given numeric columns of a data frame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The data frame to be used for EDA.
    num_col : list  
        A list of string of column names with numeric data from the data frame.
    col_scheme : str, default = 'purpleorange'  
        The color scheme of the heatmap desired, can only be one of the following;
            - 'purpleorange'
            - 'blueorange' 
            - 'redblue'

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
    >>> cor_map(data, numerical_columns, col_scheme = 'purpleorange')
        
    """
    
    # Tests whether input data is of pd.DataFrame type
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The input dataframe must be of pd.DataFrame type")

    # Tests whether input num_col is of type list
    if not isinstance(num_col, list):
        raise TypeError("The input num_col must be of type list")
    
    # Tests whether values of num_col is of type str 
    for x in num_col:
        if not isinstance(x, str):
            raise TypeError("The type of values in num_col must all be str")

    # Tests whether input col_scheme is of type str    
    if not isinstance(col_scheme, str):
        raise TypeError("col_scheme must be of type str")

    # Tests whether col_scheme is one of three possible options    
    if col_scheme not in ('purpleorange', 'blueorange', 'redblue'):
        raise Exception("This color scheme is not available, please use either 'purpleorange', 'blueorange' or 'redblue'")

    # Tests whether all input columns exist in the input data
    for x in num_col:
        if x not in list(dataframe.columns):
            raise Exception("The given column names must exist in the given dataframe.")    
        
    # Tests whether all input columns in num_col are numeric columns
    for x in num_col:
        if not is_numeric_dtype(dataframe[x]):
            raise Exception("The given numerical columns must all be numeric.")
    
    
    corr_matrix = dataframe[num_col].corr().reset_index().melt('index')
    corr_matrix.columns = ['var1', 'var2', 'cor']

    plot = alt.Chart(corr_matrix).mark_rect().encode(
        x=alt.X('var1', title=None),
        y=alt.Y('var2', title=None),
        color=alt.Color('cor',legend=None,
                       scale = alt.Scale(scheme = col_scheme)),
    ).properties(
        title = 'Correlation Matrix',
        width=400, height=400
    )

    text = plot.mark_text(size=15).encode(
        text=alt.Text('cor', format=".2f"),
        color=alt.condition(
            "datum.cor > 0.5 | datum.cor < -0.3",
            alt.value('white'),
            alt.value('black')
        )
    )
    
    cor_heatmap = plot + text

    return cor_heatmap


def outlier_identifier(dataframe, columns=None, method="trim"):
    """
    A function that identify and deal with outliers based on the method the user choose

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
    pass


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
