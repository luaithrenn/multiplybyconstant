Package_URL = 'git+https://github.com/luaithrenn/multiplybyconstant.git'
#URL of the package repository.
    
import numpy as np
import pandas as pandas
from iotfunctions.preprocessor import BaseTransformer

#The function inherits from the BaseTransformer class in the preprocessor module.

class MultiplyBySix(BaseTransformer):
   

    '''
    Multiply input column by 6 to produce a result
    '''
    #Help text.  Displays in the configuration dialog on the UI.
    
    url = Package_URL

     
    def _init__(self, input_item, output_item = 'output_item'):
    #Initalization method.  Define input and output items here.  

        self.input_item = input_item
        self.output_item =  output_item
        super().__init__()
        

    def execute(self, df):
    #Initalization method.  Define input and output items here.  
        
        df = df.copy()
        df[self.output_item] = df[self.input_item] * 6
        return df

    ≈
    
    @classmethod
    def build_ui(cls):
    #Define UI controls for the inputs and output.  Required for registration with the catalog.
    
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(UISingletem(name = 'input_item',
                                              datatype=float,
                                              description = 'Input number'
                                              ))
        #define arguments that behave as function outputs
        outputs = []
        outputs.append(UIFunctionOutSingle(name = 'output_name',
                                                     datatype=None,
                                                     description='Result of the calculation'
                                                     ))
    
        return (inputs,outputs) 
