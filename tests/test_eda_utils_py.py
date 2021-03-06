from eda_utils_py import __version__
from eda_utils_py import eda_utils_py
import pandas as pd
import altair as alt
from pandas.api.types import is_numeric_dtype
import numpy as np


def test_version():
    assert __version__ == '0.1.0'


def test_outlier_identifier():
    test_df = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 50, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm' :[0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
        'Species':['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    test_column = ['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']

    median_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 5.1, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 1.5, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm' :[0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 0.4],
    'Species':['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    trim_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 5.5, 5.1, 5.4, 5.0, 5.2, 5.3],
        'SepalWidthCm': [1.4, 1.4, 2.0, 0.7, 1.2, 1.4, 1.8, 1.5],
        'PetalWidthCm' :[0.2, 0.2, 0.3, 0.4, 0.5, 0.6, 0.4, 0.2],
        'Species':['Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    mean_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 9.21, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 3.19, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm' :[0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 0.77],
        'Species':['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    column_output= pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 9.21, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm' :[0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
        'Species':['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    # Test if the imput is not dataFrame
    with raise(TypeError):
        eda_utils_py.outlier_identifier("not dataframe")

    # Test if columns input is not list
    with raise(TypeError):
        eda_utils_py.outlier_identifier(test_df, columns=2)

    # Test if input column list is in the dataframe
    with raise(TypeError):
        eda_utils_py.outlier_identifier(test_df, columns=["not in"])

    # Test if method input is not one of three methods provided
    with raise(TypeError):
        eda_utils_py.outlier_identifier(test_df, columns=["SepalLengthCm"], method = "no")

    # Test if column selected included non-numeric columns
    with raise(Exception):
        eda_utils_py.outlier_identifier(test_df, columns=["Species"])

    assert pd.DataFrame.equals(
        outlier_identifier(test_df, test_column), trim_output
    ), "Default test not pass"
    assert pd.DataFrame.equals(
        outlier_identifier(test_df, test_column,method = "median"), median_output
    ), "The median method is not correct"
    assert pd.DataFrame.equals(
        outlier_identifier(test_df, test_column, method = "mean"), mean_output
    ), "The mean method is not correct"
    assert pd.DataFrame.equals(
        outlier_identifier(test_df, columns = ["SepalLengthCm"], method = "mean"), column_output
    ), "The selected column method is not correct"
