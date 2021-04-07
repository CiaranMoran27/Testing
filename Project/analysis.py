import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 

os.chdir(os.path.dirname(__file__))

def read_iris_dataset():
    #def read_irish_dataset():
    iris_data_file = 'Iris_Data_Set.txt'
    iris = pd.read_csv(iris_data_file, delimiter = ',', header = None)
    

def alter_iris_dataset():
    #def adjust_dataset()
    iris.columns =['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']
    pd.set_option("display.precision", 2)
    

def summary_iris_dataset():
    iris_species_count = iris.groupby('species').size()
    iris_description = iris.describe()
    iris_shape = iris.shape


def write_iris_dataset():
    with open('summary_file.txt', "a") as f:
        f.write((str(iris_species_count) +'\n'+'\n'))
        f.write((str(average) +'\n'+'\n'))
        f.write((str(std_dev) +'\n'+'\n'))
        f.write((str(iris_description) +'\n'+'\n'))
        f.write((str(iris_shape)+ '\n'+'\n'))








def scatter_plot():
    # ref: https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/
    iris = sns.load_dataset('iris')
    sns.set_style("whitegrid")

    plot_one = sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", s = 45).set_title('Sepal length Vs. Sepal width (units = cm)',fontdict= { 'fontsize': 14, 'fontweight':'bold'})
    writePlot('plot1.png')
    plt.clf()

    plot_two = sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue="species", s = 45).set_title('Petal length Vs. Petal width (units = cm)',fontdict= { 'fontsize': 14, 'fontweight':'bold'})  
    writePlot('plot2.png')
    plt.clf()

def writePlot(file_name):
    plt.savefig(file_name)


scatter_plot()

 












'''
x = iris.groupby('species').mean()
y = iris.mean()
average = x.append(y, ignore_index=True)
average.insert(0, 'species', ['setosa', 'versicolor', 'virginica', 'all_species'])

x = iris.groupby('species').std()
y = iris.std()
std_dev = x.append(y, ignore_index=True)
std_dev.insert(0, 'species', ['setosa', 'versicolor', 'virginica', 'all_species'])

'''
   
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