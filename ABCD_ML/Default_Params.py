"""
Default_Params.py
====================================
File with different saved default parameter grids,
for various classifiers within ABCD_ML.
"""

from scipy.stats import (randint as sp_randint, uniform as sp_uniform)

RF_GRID1 = {'n_estimators': list(range(3, 500)),
            'max_depth': [None] + list(range(2, 100, 5)),
            'max_features': sp_uniform(),
            'min_samples_split': sp_uniform(),
            'bootstrap': [True]}

DTC_GRID1 = {'max_depth': list(range(1, 20)),
             'min_samples_split': list(range(2, 50))}

KNN_GRID1 = {'weights': ['uniform', 'distance'],
             'n_neighbors': list(range(1, 20))}
