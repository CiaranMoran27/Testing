import pandas as pd
import os 

os.chdir(os.path.dirname(__file__))

#def read_irish_dataset():
iris_data_file = 'Iris_Data_Set.txt'
iris = pd.read_csv(iris_data_file, delimiter = ',', header = None)
    

#def adjust_dataset()
iris.columns =['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']
pd.set_option("display.precision", 2)
    

#def write_dataset_summary():
iris_species_count = iris.groupby('species').size()
iris_description = iris.describe()
iris_shape = iris.shape



x = iris.groupby('species').mean()
y = iris.mean()
average = x.append(y, ignore_index=True)
average.insert(0, 'species', ['setosa', 'versicolor', 'virginica', 'all_species'])



x = iris.groupby('species').std()
y = iris.std()
std_dev = x.append(y, ignore_index=True)
std_dev.insert(0, 'species', ['setosa', 'versicolor', 'virginica', 'all_species'])



with open('summary_file.txt', "a") as f:
    f.write((str(iris_species_count) +'\n'+'\n'))
    f.write((str(average) +'\n'+'\n'))
    f.write((str(std_dev) +'\n'+'\n'))
    f.write((str(iris_description) +'\n'+'\n'))
    f.write((str(iris_shape)+ '\n'+'\n'))



   
    #print(iris.shape) 
    #print(iris.head())   
    #print(iris.shape) 
    #print(iris.info())
    #print(iris.dtypes)
    #print(iris.corr())









'''
irish.shape()
iris.info()
iris.groupby()
iris.dtypes (data types)
iris.sample(10)
iris.describe()
iris.corr()
'''