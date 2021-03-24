import pandas as pd

iris_data_file = 'Iris_Data_Set.txt'

with open(iris_data_file,'r') as f:
    dataframe = pd.read_csv(f,sep = ",")
    print(dataframe.describe())


