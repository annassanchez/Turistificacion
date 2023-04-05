import numpy as np
import pandas as pd

def columnList(dataframe, condition):
    """
    This function takes a dataframe and returns the columns that fulfill a condition
    args: - dataframe: the dataframe you want to slice the columns
        - condition: as a string
    returns:
        the column as a list that fulfill that conditions
    """
    column_list = []
    for columna in dataframe.columns:
        if condition in columna:
            column_list.append(columna)
        else:
            pass
    print(f'the columns that have {condition} on their name are:', column_list)
    return column_list