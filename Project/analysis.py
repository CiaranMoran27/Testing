import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 

os.chdir(os.path.dirname(__file__))                                                                           # change current directory to that of this module


def read_iris_dataset():
    iris_data_file = 'iris_data_set.txt'
    iris_dataframe = pd.read_csv(iris_data_file, delimiter = ',', header = None)                              # read in Iris Dataset via Pandas Library
    iris_dataframe.columns =['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']          # add columns headers
    return iris_dataframe
    
iris_dataframe = read_iris_dataset()        


def summary_variables():
    
    shape = (len(iris_dataframe.axes[1]),len(iris_dataframe.axes[0]))
    data_types = iris_dataframe.dtypes                                                            
    species_count = iris_dataframe.groupby('species').size()
    null_count = iris_dataframe.isnull().sum()                               # True for NaN / blank values
    desc_all_species = iris_dataframe.describe()
    correlation = iris_dataframe.corr()
    pd.set_option("display.precision", 2)

    # Check if numeric columns can be converted to integer
    numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    try:
        iris_dataframe[numeric_columns].astype(float).astype(int)
        integer_check = 'The following columns only contain numeric values:\n{}.'.format(numeric_columns)      
    except ValueError:
        integer_check = 'Not all entires in the following columns contain numeric values \n{}.'.format(numeric_columns)  
    
    return shape, data_types, null_count,species_count, integer_check, desc_all_species, correlation
    
summary_tuple = summary_variables()   


def write_summary_variables(summary_tuple):
    with open('summary_file.txt', 'w') as f:
        
        skip_three_lines = ('\n' * 3)
        f.write('Fisher Iris Dataset Summary' + skip_three_lines)
        f.write('Number of columns = {} \nNumber of rows = {}{}'.format(summary_tuple[0][0],summary_tuple[0][1],skip_three_lines)) 
        f.write('Column name:  Data Types: \n'+ str(summary_tuple[1]) + skip_three_lines) 
        f.write('Column Name:  Null Count: : \n'+ str(summary_tuple[2]) + skip_three_lines)
        f.write('Row Count per Species: \n'+ str(summary_tuple[3]) + skip_three_lines)  
        f.write(summary_tuple[4] + '\n' + skip_three_lines)
        f.write(' '*17 + 'All Species : Summary Statistics \n' + str(summary_tuple[5]) + skip_three_lines)
        f.write(' '*17 + 'All Species : Correlation Statistics \n' + str(summary_tuple[6]) + skip_three_lines)

write_summary_variables(summary_tuple)


    # generate dataframe for each species   NOT YET USED
    #df_virginica = iris_dataframe[iris_dataframe['species'] == 'Iris-virginica']
    #df_setosa = iris_dataframe[iris_dataframe['species'] == 'Iris-setosa']
    #df_versicolor = iris_dataframe[iris_dataframe['species'] == 'Iris-versicolor']v



def write_plot(sub_directory,file_name):
    plt.savefig(sub_directory + file_name)
 

def scatter_plot(series_one, series_two): #[*1]

    iris = sns.load_dataset('iris')      
    plot = sns.scatterplot(data=iris, x=series_one, y=series_two, hue='species')

    fig, axs = plt.subplots(ncols=2)
    sns.scatterplot(x=series_one, y=series_two, data=iris, ax=axs[0])
    sns.scatterplot(x=series_two, y=series_one, data=iris, ax=axs[1])
 
    # set background style
    sns.set_style('whitegrid')

    # set custom legend                              
    plt.legend(title='Species', fontsize = 10, mode='expand', borderaxespad=0, ncol=3,loc='lower left',bbox_to_anchor=(0,1.02,1,0.2))  
    
    fig, axes = plt.subplots(2, 2, sharex=True, figsize=(16,8))
    fig.suptitle('test')
    plt.show()


    # set label axies     
    plt.xlabel(series_one + ' (cm)', fontsize = 10)
    plt.ylabel(series_two + ' (cm)', fontsize = 10)

    # declare variables & pass to write_plot function
    sub_directory = 'Images/'
    file_name = str(series_one + ' Vs. ' + series_two + '.png')
    write_plot(sub_directory,file_name)
    plt.clf()


def pair_plot(): #[*2]
    iris = sns.load_dataset('iris')   
    sns.pairplot(iris, hue='species', diag_kind='hist')

    sub_directory = 'Images/'
    filename = 'iris_dataset_pairplot'
    write_plot(sub_directory,filename)


# ref these website https://seaborn.pydata.org/tutorial/distributions.html
def histogram():
    iris = sns.load_dataset('iris')                                                                                  # this statement imports the matplotlib library (REF: https://matplotlib.org/2.2.2/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter)
    #plt.figure(figsize = (10, 7))
    #x = iris['sepal_length']

    sns.displot(iris, x='sepal_length',hue="species",stat="density")

    #plt.hist(x, bins = 20, color = "green")
    #plt.title("Petal Width in cm")
    #plt.xlabel("Petal_Width_cm")
    #plt.ylabel("Count")
    
    plt.show()

#scatter_plot("sepal_length","sepal_width")
#scatter_plot("sepal_length","petal_length")
#scatter_plot("sepal_length","petal_width")
#scatter_plot("sepal_width","petal_length")
#scatter_plot("sepal_width","petal_width")
#scatter_plot("petal_length","petal_width")
#scatter_plot("sepal_length","sepal_width")
#pair_plot() 
#histogram_plot()

#histogram()

# histogram  plots
#https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib



#[*1] GeekforGeeks, 2021, Plotting graph For IRIS Dataset Using Seaborn And Matplotlib, viewed 08 April 2021, https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/

#[*2] Waskomm M, 2021, seaborn.Pairgrid, viewed 08 April 2021, https://seaborn.pydata.org/generated/seaborn.PairGrid.html 



