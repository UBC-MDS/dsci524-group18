from eda_utils_py import __version__
from eda_utils_py import eda_utils_py
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
    