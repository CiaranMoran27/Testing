import pandas as pd
import os
import sys

os.chdir(os.path.dirname(__file__))
iris_data_file = 'Iris_Data_Set.txt'

with open(iris_data_file,'r') as f:
    dataframe = pd.read_csv(f,sep = ",")
    print(dataframe.describe())


