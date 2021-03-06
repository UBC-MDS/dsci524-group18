from eda_utils_py import __version__
from eda_utils_py import eda_utils_py
from pytest import raises
import pandas as pd
from pandas._testing import assert_frame_equal
import numpy as np


def test_version():
    assert __version__ == "0.1.0"


def test_imputer():
    data = pd.DataFrame(
        {"col1": [None, 4, 4, 7], "col2": [2, None, None, 2], "col3": [3, None, 6, 6]}
    )

    imp_mean = pd.DataFrame(
        {
            "col1": [5.0, 4.0, 4.0, 7.0],
            "col2": [2.0, 2.0, 2.0, 2.0],
            "col3": [3.0, 5.0, 6.0, 6.0],
        }
    )

    imp_median = pd.DataFrame(
        {
            "col1": [4.0, 4.0, 4.0, 7.0],
            "col2": [2.0, 2.0, 2.0, 2.0],
            "col3": [3.0, 6.0, 6.0, 6.0],
        }
    )

    imp_most_frequent = pd.DataFrame(
        {
            "col1": [4.0, 4.0, 4.0, 7.0],
            "col2": [2.0, 2.0, 2.0, 2.0],
            "col3": [3.0, 6.0, 6.0, 6.0],
        }
    )

    imp_constant = pd.DataFrame(
        {
            "col1": [1.0, 4.0, 4.0, 7.0],
            "col2": [2.0, 1.0, 1.0, 2.0],
            "col3": [3.0, 1.0, 6.0, 6.0],
        }
    )

    # Tests whether data is not of dataframe raises TypeError
    with raises(TypeError):
        eda_utils_py.imputer([4, None, 4, 7])

    # Tests whether strategy of incorrect type raises TypeError
    with raises(TypeError):
        eda_utils_py.imputer(data, strategy=2)

    # Tests whether fill_value of incorrect type raises TypeError
    with raises(TypeError):
        eda_utils_py.imputer(data, strategy="constant", fill_value="a string")

    # Tests whether inconsistency between strategy and fill_value raises Exception
    with raises(Exception):
        eda_utils_py.imputer(data, strategy="constant", fill_value=None)

    # Tests whether inconsistency between strategy and fill_value raises Exception
    with raises(Exception):
        eda_utils_py.imputer(data, strategy="median", fill_value=3)

    assert pd.DataFrame.equals(
        eda_utils_py.imputer(data), imp_mean
    ), "The returned dataframe using mean inputer is not correct"
    assert pd.DataFrame.equals(
        eda_utils_py.imputer(data, "median"), imp_median
    ), "The returned dataframe using median inputer is not correct"
    assert pd.DataFrame.equals(
        eda_utils_py.imputer(data, "most_frequent"), imp_most_frequent
    ), "The returned dataframe using most_frequent inputer is not correct"
    assert pd.DataFrame.equals(
        eda_utils_py.imputer(data, "constant", 1), imp_constant
    ), "The returned dataframe using constant imputer is not correct"


def test_cor_map():
    """
    A function to test whether the output of cor_map() is correct.
    """

    data = pd.DataFrame(
        {
            "SepalLengthCm": [5.1, 4.9, 4.7],
            "SepalWidthCm": [1.4, 1.4, 1.3],
            "PetalWidthCm": [0.2, 0.1, 0.2],
            "Species": ["Iris-setosa", "Iris-virginica", "Iris-germanica"],
        }
    )

    num_col_test = ["SepalLengthCm", "SepalWidthCm", "PetalWidthCm"]

    plot = eda_utils_py.cor_map(data, num_col_test, "redblue")

    # Tests whether output is of Altair type
    assert "altair" in str(type(plot)), "Output is not of Altair type"

    # Tests whether or not there are NaNs produced in the correlation values
    assert (
            plot.data["cor"].isnull().sum() == 0
    ), "There are NaN produced as correlation values"

    # Tests whether plot output scheme is one of the three given color schemes
    plot_dict = plot.to_dict()
    assert plot_dict["layer"][0]["encoding"]["color"]["scale"]["scheme"] in (
        "purpleorange",
        "blueorange",
        "redblue",
    ), "The plot color scheme is not one of the expected schemes"

    # Tests whether heatmap portion of plot is mark_rect()
    assert plot_dict["layer"][0]["mark"] == "rect", "mark should be rect"

    # Tests whether heatmap and correlation values have the same referenced var column
    assert (
            plot_dict["layer"][0]["encoding"]["x"]["field"]
            == plot_dict["layer"][1]["encoding"]["x"]["field"]
    ), "The heatmap and the correlation values are not referring to the same corresponding underlying variable x"
    assert (
            plot_dict["layer"][0]["encoding"]["y"]["field"]
            == plot_dict["layer"][1]["encoding"]["y"]["field"]
    ), "The heatmap and the correlation values are not referring to the same corresponding underlying variable y"

    # Tests whether axes is using correct calculated var column as reference
    assert (
            plot_dict["layer"][0]["encoding"]["x"]["field"] == "var1"
    ), "x should be referring to var1"
    assert (
            plot_dict["layer"][0]["encoding"]["y"]["field"] == "var2"
    ), "y should be referring to var2"

    # Testing the Exception Errors
    data2 = data.copy().to_csv()

    num_col_test1 = (1, 2, 3, 4)
    num_col_test2 = [1, 2, 3, "SepalLengthCm"]
    num_col_test3 = ["hi", "hey", "hi"]
    num_col_test4 = ["SepalLengthCm", "SepalWidthCm", "PetalWidthCm", "Species"]
    col_scheme_test = 3

    # Tests whether data is not of dataframe raises TypeError
    with raises(TypeError):
        eda_utils_py.cor_map(data2, num_col_test)

    # Tests whether num_col is of not type list raises TypeError
    with raises(TypeError):
        eda_utils_py.cor_map(data, num_col_test1)

    # Tests whether contents of num_col is notof type str raises TypeError
    with raises(TypeError):
        eda_utils_py.cor_map(data, num_col_test2)

    # Tests whether inputting unallowed col_scheme raises Exception
    with raises(Exception):
        eda_utils_py.cor_map(data, num_col_test, "bluegreen")

    # Tests whether inputting unallowed col_scheme raises TypeError
    with raises(TypeError):
        eda_utils_py.cor_map(data, num_col_test, col_scheme_test)

    # Tests whether columns do not exist in raises Exception
    with raises(Exception):
        eda_utils_py.cor_map(data, num_col_test3)

    # Tests whether if not all columns in num_col is numeric raises Exception
    with raises(Exception):
        eda_utils_py.cor_map(data, num_col_test4)


def test_scaler():
    mock_df_1 = pd.DataFrame(
        {"col1": [1, 0, 0, 3, 4],
         "col2": [4, 1, 1, 0, 1],
         "col3": [2, 0, 0, 2, 1]}
    )

    mock_df_2 = pd.DataFrame(
        {"col1": [1, 2, 1],
         "col2": [0, 1, 2]}
    )

    mock_df_1_standard = pd.DataFrame(
        {"col1": [-0.3302891295379082, -0.8807710121010884, -0.8807710121010884, 0.7706746355884523,
                  1.3211565181516325],
         "col2": [1.714389230829046, -0.26375218935831474, -0.26375218935831474, -0.9231326627541017,
                  -0.26375218935831474],
         "col3": [1.0, -1.0, -1.0, 1.0, 0.0]}
    )

    mock_df_1_minmax = pd.DataFrame(
        {"col1": [0.25, 0.00, 0.00, 0.75, 1.00],
         "col2": [1.00, 0.25, 0.25, 0.00, 0.25],
         "col3": [1.0, 0.0, 0.0, 1.0, 0.5]}
    )

    mock_df_2_standard = pd.DataFrame(
        {"col1": [-0.5773502691896256, 1.1547005383792517, -0.5773502691896256],
         "col2": [-1.0, 0.0, 1.0]}
    )

    mock_df_2_minmax = pd.DataFrame(
        {"col1": [0.0, 1.0, 0.0],
         "col2": [0.0, 0.5, 1.0]}
    )

    standard_scaled_mock_df_1 = eda_utils_py.scale(mock_df_1, ['col1', 'col2', 'col3'])
    standard_scaled_mock_df_2 = eda_utils_py.scale(mock_df_2, ['col1', 'col2'])
    minmax_scaled_mock_df_1 = eda_utils_py.scale(mock_df_1, ['col1', 'col2', 'col3'], scaler="minmax")
    minmax_scaled_mock_df_2 = eda_utils_py.scale(mock_df_2, ['col1', 'col2'], scaler="minmax")

    # Tests whether data is not of type pd.Dataframe raises TypeError
    with raises(TypeError):
        eda_utils_py.scale([14, None, 3, 27])

    # Tests whether scaler of incorrect method raises TypeError
    with raises(TypeError):
        eda_utils_py.scale(mock_df_1, ['col1', 'col2'], scaler=1)

    # Tests whether columns of incorrect type raises TypeError
    with raises(TypeError):
        eda_utils_py.scale(mock_df_1, {'col1': 1, 'col2': 3})

    assert pd.DataFrame.equals(
        standard_scaled_mock_df_1, mock_df_1_standard
    ), "The returned dataframe using standard scaler method is not correct"
    assert pd.DataFrame.equals(
        minmax_scaled_mock_df_1, mock_df_1_minmax
    ), "The returned dataframe using standard scaler method is not correct"

    assert pd.DataFrame.equals(
        standard_scaled_mock_df_2, mock_df_2_standard
    ), "The returned dataframe using most_frequent inputer is not correct"
    assert pd.DataFrame.equals(
        minmax_scaled_mock_df_2, mock_df_2_minmax
    ), "The returned dataframe using constant imputer is not correct"


def test_outlier_identifier():
    test_df = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 50, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm': [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
        'Species': ['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
                    'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    test_column = ['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']

    median_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 5.1, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 1.5, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm': [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 0.4],
        'Species': ['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
                    'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    trim_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 5.5, 5.1, 5.4, 5.0, 5.2, 5.3],
        'SepalWidthCm': [1.4, 1.4, 2.0, 0.7, 1.2, 1.4, 1.8, 1.5],
        'PetalWidthCm': [0.2, 0.2, 0.3, 0.4, 0.5, 0.6, 0.4, 0.2],
        'Species': ['Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
                    'Iris-setosa', 'Iris-setosa']
    })

    mean_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 9.21, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 3.19, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm': [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 0.77],
        'Species': ['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
                    'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    column_output = pd.DataFrame({
        'SepalLengthCm': [5.1, 4.9, 4.7, 5.5, 5.1, 9.21, 5.4, 5.0, 5.2, 5.3, 5.1],
        'SepalWidthCm': [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
        'PetalWidthCm': [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
        'Species': ['Iris-setosa', 'Iris-virginica', 'Iris-germanica', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
                    'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
    })

    # Test if the imput is not dataFrame
    with raises(TypeError):
        eda_utils_py.outlier_identifier("not dataframe")

    # Test if columns input is not list
    with raises(TypeError):
        eda_utils_py.outlier_identifier(test_df, columns=2)

    # Test if input column list is in the dataframe
    with raises(Exception):
        eda_utils_py.outlier_identifier(test_df, columns=["not in"])

    # Test if method input is not one of three methods provided
    with raises(Exception):
        eda_utils_py.outlier_identifier(test_df, columns=["SepalLengthCm"], method="no")

    # Test if column selected included non-numeric columns
    with raises(Exception):
        eda_utils_py.outlier_identifier(test_df, columns=["Species"])

    assert pd.DataFrame.equals(
        eda_utils_py.outlier_identifier(test_df, test_column), trim_output
    ), "Default test not pass"
    assert pd.DataFrame.equals(
        eda_utils_py.outlier_identifier(test_df, test_column, method="median"), median_output
    ), "The median method is not correct"
    assert pd.DataFrame.equals(
        eda_utils_py.outlier_identifier(test_df, test_column, method="mean"), mean_output
    ), "The mean method is not correct"
    assert pd.DataFrame.equals(
        eda_utils_py.outlier_identifier(test_df, columns=["SepalLengthCm"], method="mean"), column_output
    ), "The selected column method is not correct"
