import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 

os.chdir(os.path.dirname(__file__))                                                                    # change current directory to that of this module


def read_iris_dataset():
    iris_data_file = 'iris_data_set.txt'
    iris_df = pd.read_csv(iris_data_file, delimiter = ',', header = None)                              # read in Iris Dataset via Pandas Library
    iris_df.columns =['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']          # add columns headers
    return iris_df
iris_df = read_iris_dataset()

    

def summary_variables():
    
    shape = (len(iris_df.axes[1]),len(iris_df.axes[0]))                                  # count # rows on each axis of array
    data_types = iris_df.dtypes                                                            
    null_count = iris_df.isnull().sum()                                                  # True for NaN / blank values
    species_count = iris_df.groupby('species').size()                                    
    desc_all_species = iris_df.describe()
    df_head = iris_df.head(5)
    correlation = iris_df.corr()
    pd.set_option("display.precision", 2)
    print(set(iris_df['species'].apply(lambda x: type(x))))
    print(set(iris_df['sepal_length'].apply(lambda x: type(x))))
    
    return shape, data_types, null_count, species_count, df_head, desc_all_species, correlation
    
summary_tuple = summary_variables()   



def write_summary_variables(summary_tuple):
    with open('summary_file.txt', 'w') as f:

        skip_three_lines = ('\n' * 3)
        
        f.write('Fisher Iris Dataset Summary' + skip_three_lines)
        f.write('Number of columns = {} \nNumber of rows = {}{}'.format(summary_tuple[0][0],summary_tuple[0][1],skip_three_lines)) 
        f.write('Column name:  Pandas dtypes: \n'+ str(summary_tuple[1]) + skip_three_lines) 
        f.write('Column name:  Null Count: \n'+ str(summary_tuple[2]) + skip_three_lines)
        f.write('Row Count per Species: \n'+ str(summary_tuple[3]) + skip_three_lines)  
        f.write(' '*17 + 'First 5 rows of the Dataset\n' + str(summary_tuple[4])  + skip_three_lines)
        f.write(' '*17 + 'All Species : Summary Statistics \n' + str(summary_tuple[5]) + skip_three_lines)
        f.write(' '*17 + 'All Species : Correlation Statistics \n' + str(summary_tuple[6]) + skip_three_lines)

write_summary_variables(summary_tuple)




# !delete this if you cant pass plot to function sucessfully!
def write_plot(plot,file_name):
    fig.savefig('Images/' + file_name + '.png')


def scatter_plot(): 


    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    fig.suptitle('Scatter Plot of all variables (Units = cm)',fontsize = 25)
    
    ax = sns.scatterplot(ax=axes[0, 0], data=iris_df, x='petal_length', y='petal_width', hue = 'species',legend = False)
    ax = sns.scatterplot(ax=axes[0, 1], data=iris_df, x='petal_length', y='sepal_length',hue = 'species',legend = False)
    ax = sns.scatterplot(ax=axes[0, 2], data=iris_df, x='petal_length', y='sepal_width', hue = 'species',legend = False)
    ax = sns.scatterplot(ax=axes[1, 0], data=iris_df, x='sepal_length', y='sepal_width', hue = 'species',legend = False)
    ax = sns.scatterplot(ax=axes[1, 1], data=iris_df, x='sepal_length', y='petal_width', hue = 'species',legend = False)
    ax = sns.scatterplot(ax=axes[1, 2], data=iris_df, x='sepal_width',  y='petal_width', hue = 'species')

    plt.legend(fontsize='12', loc = 2 ,bbox_to_anchor=(1.02, 1),borderaxespad=0.,)

    x = ax.get_xlabel()
    y = ax.get_ylabel()
    for ax in plt.gcf().axes:
        ax.set_xlabel(x, fontsize=12)
        ax.set_ylabel(y, fontsize=12)
      
    plt.savefig('Images/' + 'scatter_plots' +'.png')

#scatter_plot()

def plot_histograms():

    fig, axes = plt.subplots(2, 2, figsize=(18, 10))
    fig.suptitle('Histogram of all variables (Units = cm)',fontsize = 25)

    ax = sns.histplot(ax=axes[0, 0], data=iris_df, x='petal_length', hue = 'species', bins = 30, legend = False)
    ax = sns.histplot(ax=axes[0, 1], data=iris_df, x='petal_width',  hue = 'species', bins = 30, legend = False)
    ax = sns.histplot(ax=axes[1, 0], data=iris_df, x='sepal_length', hue = 'species', bins = 30, legend = False)
    ax = sns.histplot(ax=axes[1, 1], data=iris_df, x='sepal_width',  hue = 'species', bins = 30)
    plt.legend(fontsize='14', labels = ['virginica', 'versicolor','setosa'], loc = 2 ,bbox_to_anchor=(1.02, 1),borderaxespad=0.,)

    for ax in plt.gcf().axes:
        x = ax.get_xlabel()
        y = ax.get_ylabel()
        ax.set_xlabel(x, fontsize=15)
        ax.set_ylabel(y, fontsize=15)

    plt.savefig('Images/' + 'histograms' +'.png')

#plot_histograms()




#[*1] GeekforGeeks, 2021, Plotting graph For IRIS Dataset Using Seaborn And Matplotlib, viewed 08 April 2021, https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/

#[*2] Waskomm M, 2021, seaborn.Pairgrid, viewed 08 April 2021, https://seaborn.pydata.org/generated/seaborn.PairGrid.html 



