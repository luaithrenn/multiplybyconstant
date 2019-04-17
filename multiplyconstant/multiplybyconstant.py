Package_URL = 'git+https://github.com/luaithrenn/multiplybyconstant.git'

import numpy as np
import pandas as pandas
from iotfunctions.preprocessor import BaseTransformer

class MultiplyBySix(BaseTransformer):

    '''
    Multiply input column by 6 to produce a result
    '''
    
    url = Package_URL

    def _init__(self, input_item, output_item = 'output_item'):

        self.input_item = input_item
        self.output_item =  output_item
        super().__init__()

    def execute(self, df):
        df = df.copy()
        df[self.output_item] = df[self.input_item] * 6
        return df
