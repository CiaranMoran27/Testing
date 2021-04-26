# This module uses Exhaustive Feature Selector (EHS) wrapper method to evaluate 
# mean accuracy % of Knearest Neighbouts Machine Learning Model
# Author Ciaran Moran

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
from sklearn import preprocessing
from analysis import read_iris_dataset


iris_df = read_iris_dataset()                                                                   # store iris dataframe (function was imported)


def knearest_neighbour(cross_validation):
#Reference: 
# Raschka, S, 2020, Example 2 - Visualizing the feature selection results, viewed 26 April 2021, 
# http://rasbt.github.io/mlxtend/user_guide/feature_selection/ExhaustiveFeatureSelector/#example-2-visualizing-the-feature-selection-results

    iris_data = iris_df[["petal_length", "petal_width", "sepal_length","sepal_width"]].to_numpy()   # seperate feature columns into numpy list of lists
    iris_target = iris_df[iris_df.columns[4]]                                                       # seperate species column into own series

    # instansiate label encoder object
    label_encoder = preprocessing.LabelEncoder()

    # fit species series  into label_encoder object using fit_transform function -> fits numeric values rather than species name
    iris_target_numeric = label_encoder.fit_transform(iris_target)

    # set model parameters
    knn = KNeighborsClassifier(n_neighbors=3)   # looks a 3 nearest neighbours (including itself as datapoint)
    efs1 = EFS(knn,                             # specify model type 
            min_features=1,                     # min features for comparison 
            max_features=4,                     # min features for comparison 
            scoring='accuracy',                 # accuracy method
            print_progress=True,             
            cv = cross_validation)              # cross validation score = 5:  splits data into 5 groups of 30 observations 
    
    
    feature_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
    efs1 = efs1.fit(iris_data, iris_target_numeric, custom_feature_names=feature_names)   # fit data to efs1 pre-defined model

    df = pd.DataFrame.from_dict(efs1.get_metric_dict()).T                                 # uses get_metric_dict method on efs1 variable, efs1 is then converted from dict to dataframe
    df.sort_values('avg_score', inplace=True, ascending=False)                            # sort column in ascending order, inplace True means no copy is made
  
  
    # Create bar chart on mean performance of each subset of features
    fig, ax = plt.subplots(figsize=(12,9))                                                # create figure & axes
    y_pos = np.arange(len(df))                                                            # stores evenly spaced values that total the length of the df 

    ax.barh(y_pos, df['avg_score'], xerr=df['std_dev'])                                   # sets chart parameters
    ax.set_yticks(y_pos)                                                                  # sets y positions 
    ax.set_yticklabels(df['feature_names'])                                               # sets y labels
    ax.yaxis.tick_right()                                                                 # y axis ticks right
    ax.yaxis.set_label_position("right")                                                  # y axis labels right 
    ax.set_xlabel('Accuracy')                                                             # sets x axis labels

    plt.title('Plox X: KNeighborsClassifier Model % Accuracy')                            # add title
    fig.tight_layout()                                                                    # adjust plot format to frame size
    plt.savefig('Images/' + 'knn_average_score' +'.png')   
    


if __name__ == '__main__':
    knearest_neighbour(5)
else:
    pass