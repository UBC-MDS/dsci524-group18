from eda_utils_py import __version__
from eda_utils_py import eda_utils_py
from pytest import raises
import pandas as pd

def test_version():
    assert __version__ == '0.1.0'

def test_cor_map():
    
    """
    A function to test whether the output of cor_map() is correct.
    """
    
    data = pd.DataFrame({
    'SepalLengthCm':[5.1, 4.9, 4.7], 
    'SepalWidthCm':[1.4, 1.4, 1.3],
    'PetalWidthCm':[0.2, 0.1, 0.2],
    'Species':['Iris-setosa', 'Iris-virginica', 'Iris-germanica']
    })
    
    num_col_test = ['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']
    
    plot = eda_utils_py.cor_map(data, num_col_test, 'redblue')
    
    # Tests whether output is of Altair type
    assert "altair" in str(type(plot)), "Output is not of Altair type"
    
    # Tests whether or not there are NaNs produced in the correlation values
    assert plot.data['cor'].isnull().sum() == 0, "There are NaN produced as correlation values"
    
    # Tests whether plot output scheme is one of the three given color schemes
    plot_dict = plot.to_dict() 
    assert plot_dict["layer"][0]['encoding']['color']['scale']['scheme'] in ('purpleorange','blueorange', 'redblue'), "The plot color scheme is not one of the expected schemes"
    
    # Tests whether heatmap portion of plot is mark_rect()
    assert plot_dict["layer"][0]['mark'] == 'rect', "mark should be rect"
    
    # Tests whether heatmap and correlation values have the same referenced var column
    assert plot_dict['layer'][0]['encoding']['x']['field'] == plot_dict['layer'][1]['encoding']['x']['field'], "The heatmap and the correlation values are not referring to the same corresponding underlying variable x"
    assert plot_dict['layer'][0]['encoding']['y']['field'] == plot_dict['layer'][1]['encoding']['y']['field'], "The heatmap and the correlation values are not referring to the same corresponding underlying variable y"
    
    # Tests whether axes is using correct calculated var column as reference
    assert plot_dict['layer'][0]['encoding']['x']['field'] == 'var1', "x should be referring to var1"
    assert plot_dict['layer'][0]['encoding']['y']['field'] == 'var2', "y should be referring to var2"
    
    
    # Testing the Exception Errors
    data2 = data.copy().to_csv()

    num_col_test1 = (1, 2, 3, 4)
    num_col_test2 = [1, 2, 3, 'SepalLengthCm']
    num_col_test3 = ['hi', 'hey', 'hi']
    num_col_test4 = ['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm', 'Species']
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
        eda_utils_py.cor_map(data, num_col_test, 'bluegreen')

    # Tests whether inputting unallowed col_scheme raises TypeError
    with raises(TypeError):
        eda_utils_py.cor_map(data, num_col_test, col_scheme_test)

    # Tests whether columns do not exist in raises Exception
    with raises(Exception):
        eda_utils_py.cor_map(data, num_col_test3)

    # Tests whether if not all columns in num_col is numeric raises Exception
    with raises(Exception):
        eda_utils_py.cor_map(data, num_col_test4)