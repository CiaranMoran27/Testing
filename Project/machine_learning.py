from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


'''
# Create a logistic regression classifier
lr = LogisticRegression()

# Create an EFS object
efs = EFS(estimator=lr,        # Use logistic regression as the classifier/estimator
          min_features=1,      # The minimum number of features to consider is 1
          max_features=4,      # The maximum number of features to consider is 4
          scoring='accuracy',  # The metric to use to evaluate the classifier is accuracy 
          cv=5)                # The number of cross-validations to perform is 5

# Train EFS with our dataset
efs = efs.fit(X_data, y_data)

# Print the results
print('Best accuracy score: %.2f' % efs.best_score_) # best_score_ shows the best score 
print('Best subset (indices):', efs.best_idx_)       # best_idx_ shows the index of features that yield the best score 
print('Best subset (corresponding names):', efs.best_feature_names_) # best_feature_names_ shows the feature names                                                         # that yield the best score
'''

'''
from sklearn.neighbors import KNeighborsClassifier
X = iris_df.data
y = iris_df.target

knn = KNeighborsClassifier(n_neighbors=3)

efs1 = EFS(knn, 
           min_features=1,
           max_features=4,
           scoring='accuracy',
           print_progress=True,
           cv=5)

efs1 = efs1.fit(X, y)

print('Best accuracy score: %.2f' % efs1.best_score_)
print('Best subset (indices):', efs1.best_idx_)
print('Best subset (corresponding names):', efs1.best_feature_names_)
'''

# Reference: http://rasbt.github.io/mlxtend/user_guide/feature_selection/ExhaustiveFeatureSelector/


from sklearn.neighbors import KNeighborsClassifier
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
import pandas as pd
import numpy as np
from sklearn import preprocessing
from analysis import read_iris_dataset

iris_df = read_iris_dataset()                                                                   # store iris dataframe (function was imported)


def knearest_neighbour():
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
            cv=5)                               # cross validation score = 5:  splits data into 5 groups of 30 observations 


    efs1 = efs1.fit(iris_data, iris_target_numeric)                               # fit data to efs1 pre-defined model

    df = pd.DataFrame.from_dict(efs1.get_metric_dict()).T                         # uses get_metric_dict method on efs1 variable, efs1 is then converted from dict to dataframe
    df.sort_values('avg_score', inplace=True, ascending=False)                    # sort column in ascending order, inplace True means no copy is made
    df.drop(df.columns.difference(['avg_score','feature_idx']), 1, inplace=True)  # retain two columns if interest
    df[['avg_score']] = df[['avg_score']].apply(pd.to_numeric)                    # convet avg_score column to numberic
    df['avg_score'] = df['avg_score'].apply(lambda x:round(x*100,2))              # multipy average  avg_score *100 and round to 2 decimals 
    df.to_csv('knn_summary.csv', header=True, index=None, sep=',', mode='w')      # write to summary csv
    plt.plot('feature_idx','avg_score')
    plt.show()




if __name__ == '__main__':
    knearest_neighbour()
else:
    pass