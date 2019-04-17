Package_URL = 'git+https://github.com/luaithrenn/multiplybyconstant.git'

import numpy as np
import pandas as pandas
from iotfunctions.preprocessor import BaseTransformer

class MultiplyBySix(BaseTransformer):

    '''
    Multiply input column by 6 to produce a result
    '''

    def __init__(self, input_item=input_item, result='result'):

        self.input_item = input_item
        self.result = result
        super().__init__()

    def execute (self, df)
        df = df.copy()
        df[self.result] = df[self.input_item] * 6

        return df
