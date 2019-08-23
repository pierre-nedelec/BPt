***********
Model Types
***********

binary
======
dt classifier
*************

  Base Class Documenation: :class:`sklearn.tree.DecisionTreeClassifier`

  Param Distributions

	0. "base dt" ::

		defaults only

	1. "dt rs" ::

		max_depth: Random Integer Distribution (1, 19)
		min_samples_split: Random Integer Distribution (2, 49)


elastic net logistic
********************

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base elastic" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: elasticnet
		l1_ratio: 0.5

	1. "elastic classifier" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: elasticnet
		l1_ratio: Random Uniform Distribution (0.0, 1.0)
		C: Random Reciprical Distribution (0.0001, 10000.0)


gaussian nb
***********

  Base Class Documenation: :class:`sklearn.naive_bayes.GaussianNB`

  Param Distributions

	0. "base gnb" ::

		var_smoothing: 1e-09


gp classifier
*************

  Base Class Documenation: :class:`sklearn.gaussian_process.GaussianProcessClassifier`

  Param Distributions

	0. "base gp classifier" ::

		n_restarts_optimizer: 5


knn classifier
**************

  Base Class Documenation: :class:`sklearn.neighbors.KNeighborsClassifier`

  Param Distributions

	0. "base knn" ::

		n_neighbors: 5

	1. "knn rs" ::

		weights: ['uniform', 'distance']
		n_neighbors: Random Integer Distribution (2, 19)


lasso logistic
**************

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base lasso" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l1

	1. "lasso C" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l1
		C: Random Reciprical Distribution (0.0001, 10000.0)


light gbm classifier
********************

  Base Class Documenation: :class:`lightgbm.LGBMClassifier`

  Param Distributions

	0. "base lgbm" ::

		silent: True

	1. "lgbm rs" ::

		silent: True
		boosting_type: ['gbdt', 'dart', 'goss']
		n_estimators: Random Integer Distribution (3, 499)
		num_leaves: Random Integer Distribution (6, 49)
		min_child_samples: Random Integer Distribution (100, 499)
		min_child_weight: Random Reciprical Distribution (1e-05, 10000.0)
		subsample: Random Uniform Distribution (0.2, 1.0)
		colsample_bytree: Random Uniform Distribution (0.4, 1.0)
		reg_alpha: Random Reciprical Distribution (0.1, 100.0)
		reg_lambda: Random Reciprical Distribution (0.1, 100.0)


logistic
********

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base logistic" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: none


mlp classifier
**************

  Base Class Documenation: :class:`sklearn.neural_network.MLPClassifier`

  Param Distributions

	0. "base mlp" ::

		defaults only

	1. "mlp rs" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)

	2. "mlp rs es" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)
		early_stopping: True
		n_iter_no_change: Random Integer Distribution (5, 49)

	3. "mlp layers search" ::

		hidden_layer_sizes: Too many params to show


random forest classifier
************************

  Base Class Documenation: :class:`sklearn.ensemble.RandomForestClassifier`

  Param Distributions

	0. "base rf" ::

		n_estimators: 100

	1. "rf rs" ::

		n_estimators: Random Integer Distribution (3, 499)
		max_depth: Random Integer Distribution (2, 199)
		max_features: Random Uniform Distribution (0.0, 1.0)
		min_samples_split: Random Uniform Distribution (0.0, 1.0)
		bootstrap: True


ridge logistic
**************

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base ridge" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l2

	1. "ridge C" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l2
		C: Random Reciprical Distribution (0.0001, 10000.0)


svm classifier
**************

  Base Class Documenation: :class:`sklearn.svm.SVC`

  Param Distributions

	0. "base svm classifier" ::

		kernel: rbf
		gamma: scale
		probability: True

	1. "svm classifier rs" ::

		kernel: rbf
		gamma: Random Reciprical Distribution (1e-06, 0.1)
		C: Random Reciprical Distribution (0.0001, 10000.0)
		probability: True



regression
==========
dt regressor
************

  Base Class Documenation: :class:`sklearn.tree.DecisionTreeRegressor`

  Param Distributions

	0. "base dt" ::

		defaults only

	1. "dt rs" ::

		max_depth: Random Integer Distribution (1, 19)
		min_samples_split: Random Integer Distribution (2, 49)


elastic net regressor
*********************

  Base Class Documenation: :class:`sklearn.linear_model.ElasticNet`

  Param Distributions

	0. "base elastic net" ::

		max_iter: 5000

	1. "elastic regression" ::

		max_iter: 5000
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		l1_ratio: Random Uniform Distribution (0.0, 1.0)


gp regressor
************

  Base Class Documenation: :class:`sklearn.gaussian_process.GaussianProcessRegressor`

  Param Distributions

	0. "base gp regressor" ::

		n_restarts_optimizer: 5
		normalize_y: True


knn regressor
*************

  Base Class Documenation: :class:`sklearn.neighbors.KNeighborsRegressor`

  Param Distributions

	0. "base knn" ::

		n_neighbors: 5

	1. "knn rs" ::

		weights: ['uniform', 'distance']
		n_neighbors: Random Integer Distribution (2, 19)


light gbm regressor
*******************

  Base Class Documenation: :class:`lightgbm.LGBMRegressor`

  Param Distributions

	0. "base lgbm" ::

		silent: True

	1. "lgbm rs" ::

		silent: True
		boosting_type: ['gbdt', 'dart', 'goss']
		n_estimators: Random Integer Distribution (3, 499)
		num_leaves: Random Integer Distribution (6, 49)
		min_child_samples: Random Integer Distribution (100, 499)
		min_child_weight: Random Reciprical Distribution (1e-05, 10000.0)
		subsample: Random Uniform Distribution (0.2, 1.0)
		colsample_bytree: Random Uniform Distribution (0.4, 1.0)
		reg_alpha: Random Reciprical Distribution (0.1, 100.0)
		reg_lambda: Random Reciprical Distribution (0.1, 100.0)


light gbm regressor early stop
******************************

  Base Class Documenation: :class:`ABCD_ML.Early_Stop.EarlyStopLGBMRegressor`

  Param Distributions

	0. "base lgbm es" ::

		silent: True
		val_split_percent: 0.1
		early_stop_rounds: 50

	1. "lgbm es rs" ::

		silent: True
		boosting_type: ['gbdt', 'dart', 'goss']
		n_estimators: Random Integer Distribution (3, 499)
		num_leaves: Random Integer Distribution (6, 49)
		min_child_samples: Random Integer Distribution (100, 499)
		min_child_weight: Random Reciprical Distribution (1e-05, 10000.0)
		subsample: Random Uniform Distribution (0.2, 1.0)
		colsample_bytree: Random Uniform Distribution (0.4, 1.0)
		reg_alpha: Random Reciprical Distribution (0.1, 100.0)
		reg_lambda: Random Reciprical Distribution (0.1, 100.0)
		val_split_percent: Random Uniform Distribution (0.05, 0.25)
		early_stop_rounds: Random Integer Distribution (10, 149)


linear regressor
****************

  Base Class Documenation: :class:`sklearn.linear_model.LinearRegression`

  Param Distributions

	0. "base linear" ::

		fit_intercept: True


mlp regressor
*************

  Base Class Documenation: :class:`sklearn.neural_network.MLPRegressor`

  Param Distributions

	0. "base mlp" ::

		defaults only

	1. "mlp rs" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)

	2. "mlp rs es" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)
		early_stopping: True
		n_iter_no_change: Random Integer Distribution (5, 49)

	3. "mlp layers search" ::

		hidden_layer_sizes: Too many params to show


random forest regressor
***********************

  Base Class Documenation: :class:`sklearn.ensemble.RandomForestRegressor`

  Param Distributions

	0. "base rf" ::

		n_estimators: 100

	1. "rf rs" ::

		n_estimators: Random Integer Distribution (3, 499)
		max_depth: Random Integer Distribution (2, 199)
		max_features: Random Uniform Distribution (0.0, 1.0)
		min_samples_split: Random Uniform Distribution (0.0, 1.0)
		bootstrap: True


svm regressor
*************

  Base Class Documenation: :class:`sklearn.svm.SVR`

  Param Distributions

	0. "base svm" ::

		kernel: rbf
		gamma: scale

	1. "svm rs" ::

		kernel: rbf
		gamma: Random Reciprical Distribution (1e-06, 0.1)
		C: Random Reciprical Distribution (0.0001, 10000.0)



categorical multilabel
======================
dt classifier
*************

  Base Class Documenation: :class:`sklearn.tree.DecisionTreeClassifier`

  Param Distributions

	0. "base dt" ::

		defaults only

	1. "dt rs" ::

		max_depth: Random Integer Distribution (1, 19)
		min_samples_split: Random Integer Distribution (2, 49)


knn classifier
**************

  Base Class Documenation: :class:`sklearn.neighbors.KNeighborsClassifier`

  Param Distributions

	0. "base knn" ::

		n_neighbors: 5

	1. "knn rs" ::

		weights: ['uniform', 'distance']
		n_neighbors: Random Integer Distribution (2, 19)


mlp classifier
**************

  Base Class Documenation: :class:`sklearn.neural_network.MLPClassifier`

  Param Distributions

	0. "base mlp" ::

		defaults only

	1. "mlp rs" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)

	2. "mlp rs es" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)
		early_stopping: True
		n_iter_no_change: Random Integer Distribution (5, 49)

	3. "mlp layers search" ::

		hidden_layer_sizes: Too many params to show


random forest classifier
************************

  Base Class Documenation: :class:`sklearn.ensemble.RandomForestClassifier`

  Param Distributions

	0. "base rf" ::

		n_estimators: 100

	1. "rf rs" ::

		n_estimators: Random Integer Distribution (3, 499)
		max_depth: Random Integer Distribution (2, 199)
		max_features: Random Uniform Distribution (0.0, 1.0)
		min_samples_split: Random Uniform Distribution (0.0, 1.0)
		bootstrap: True



categorical multiclass
======================
dt classifier
*************

  Base Class Documenation: :class:`sklearn.tree.DecisionTreeClassifier`

  Param Distributions

	0. "base dt" ::

		defaults only

	1. "dt rs" ::

		max_depth: Random Integer Distribution (1, 19)
		min_samples_split: Random Integer Distribution (2, 49)


elastic net logistic
********************

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base elastic" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: elasticnet
		l1_ratio: 0.5

	1. "elastic classifier" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: elasticnet
		l1_ratio: Random Uniform Distribution (0.0, 1.0)
		C: Random Reciprical Distribution (0.0001, 10000.0)


gaussian nb
***********

  Base Class Documenation: :class:`sklearn.naive_bayes.GaussianNB`

  Param Distributions

	0. "base gnb" ::

		var_smoothing: 1e-09


gp classifier
*************

  Base Class Documenation: :class:`sklearn.gaussian_process.GaussianProcessClassifier`

  Param Distributions

	0. "base gp classifier" ::

		n_restarts_optimizer: 5


knn classifier
**************

  Base Class Documenation: :class:`sklearn.neighbors.KNeighborsClassifier`

  Param Distributions

	0. "base knn" ::

		n_neighbors: 5

	1. "knn rs" ::

		weights: ['uniform', 'distance']
		n_neighbors: Random Integer Distribution (2, 19)


lasso logistic
**************

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base lasso" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l1

	1. "lasso C" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l1
		C: Random Reciprical Distribution (0.0001, 10000.0)


light gbm classifier
********************

  Base Class Documenation: :class:`lightgbm.LGBMClassifier`

  Param Distributions

	0. "base lgbm" ::

		silent: True

	1. "lgbm rs" ::

		silent: True
		boosting_type: ['gbdt', 'dart', 'goss']
		n_estimators: Random Integer Distribution (3, 499)
		num_leaves: Random Integer Distribution (6, 49)
		min_child_samples: Random Integer Distribution (100, 499)
		min_child_weight: Random Reciprical Distribution (1e-05, 10000.0)
		subsample: Random Uniform Distribution (0.2, 1.0)
		colsample_bytree: Random Uniform Distribution (0.4, 1.0)
		reg_alpha: Random Reciprical Distribution (0.1, 100.0)
		reg_lambda: Random Reciprical Distribution (0.1, 100.0)


logistic
********

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base logistic" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: none


mlp classifier
**************

  Base Class Documenation: :class:`sklearn.neural_network.MLPClassifier`

  Param Distributions

	0. "base mlp" ::

		defaults only

	1. "mlp rs" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)

	2. "mlp rs es" ::

		hidden_layer_sizes: Too many params to show
		activation: ['identity', 'logistic', 'tanh', 'relu']
		alpha: Random Reciprical Distribution (1e-05, 100.0)
		batch_size: Random Integer Distribution (2, 199)
		learning_rate: ['constant', 'invscaling', 'adaptive']
		learning_rate_init: Random Reciprical Distribution (1e-05, 0.01)
		max_iter: Random Integer Distribution (100, 499)
		beta_1: Random Uniform Distribution (0.5, 1.0)
		beta_2: Random Uniform Distribution (0.5, 1.0)
		early_stopping: True
		n_iter_no_change: Random Integer Distribution (5, 49)

	3. "mlp layers search" ::

		hidden_layer_sizes: Too many params to show


random forest classifier
************************

  Base Class Documenation: :class:`sklearn.ensemble.RandomForestClassifier`

  Param Distributions

	0. "base rf" ::

		n_estimators: 100

	1. "rf rs" ::

		n_estimators: Random Integer Distribution (3, 499)
		max_depth: Random Integer Distribution (2, 199)
		max_features: Random Uniform Distribution (0.0, 1.0)
		min_samples_split: Random Uniform Distribution (0.0, 1.0)
		bootstrap: True


ridge logistic
**************

  Base Class Documenation: :class:`sklearn.linear_model.LogisticRegression`

  Param Distributions

	0. "base ridge" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l2

	1. "ridge C" ::

		solver: saga
		max_iter: 5000
		multi_class: auto
		penalty: l2
		C: Random Reciprical Distribution (0.0001, 10000.0)


svm classifier
**************

  Base Class Documenation: :class:`sklearn.svm.SVC`

  Param Distributions

	0. "base svm classifier" ::

		kernel: rbf
		gamma: scale
		probability: True

	1. "svm classifier rs" ::

		kernel: rbf
		gamma: Random Reciprical Distribution (1e-06, 0.1)
		C: Random Reciprical Distribution (0.0001, 10000.0)
		probability: True



***********
Samplers
***********

binary
======
adasyn
******

  Base Class Documenation: :class:`imblearn.over_sampling.ADASYN`

  Param Distributions

	0. "default" ::

		defaults only


all knn
*******

  Base Class Documenation: :class:`imblearn.under_sampling.AllKNN`

  Param Distributions

	0. "default" ::

		defaults only


borderline smote
****************

  Base Class Documenation: :class:`imblearn.over_sampling.BorderlineSMOTE`

  Param Distributions

	0. "default" ::

		defaults only


cluster centroids
*****************

  Base Class Documenation: :class:`imblearn.under_sampling.ClusterCentroids`

  Param Distributions

	0. "default" ::

		defaults only


condensed nn
************

  Base Class Documenation: :class:`imblearn.under_sampling.CondensedNearestNeighbour`

  Param Distributions

	0. "default" ::

		defaults only


enn
***

  Base Class Documenation: :class:`imblearn.under_sampling.EditedNearestNeighbours`

  Param Distributions

	0. "default" ::

		defaults only


kmeans smote
************

  Base Class Documenation: :class:`imblearn.over_sampling.KMeansSMOTE`

  Param Distributions

	0. "default" ::

		defaults only


near miss
*********

  Base Class Documenation: :class:`imblearn.under_sampling.NearMiss`

  Param Distributions

	0. "default" ::

		defaults only


neighbourhood cleaning rule
***************************

  Base Class Documenation: :class:`imblearn.under_sampling.NeighbourhoodCleaningRule`

  Param Distributions

	0. "default" ::

		defaults only


one sided selection
*******************

  Base Class Documenation: :class:`imblearn.under_sampling.OneSidedSelection`

  Param Distributions

	0. "default" ::

		defaults only


random over sampler
*******************

  Base Class Documenation: :class:`imblearn.over_sampling.RandomOverSampler`

  Param Distributions

	0. "default" ::

		defaults only


random under sampler
********************

  Base Class Documenation: :class:`imblearn.under_sampling.RandomUnderSampler`

  Param Distributions

	0. "default" ::

		defaults only


renn
****

  Base Class Documenation: :class:`imblearn.under_sampling.RepeatedEditedNearestNeighbours`

  Param Distributions

	0. "default" ::

		defaults only


smote
*****

  Base Class Documenation: :class:`imblearn.over_sampling.SMOTE`

  Param Distributions

	0. "default" ::

		defaults only


smote enn
*********

  Base Class Documenation: :class:`imblearn.combine.SMOTEENN`

  Param Distributions

	0. "default" ::

		defaults only


smote nc
********

  Base Class Documenation: :class:`imblearn.over_sampling.SMOTENC`

  Param Distributions

	0. "default" ::

		defaults only


smote tomek
***********

  Base Class Documenation: :class:`imblearn.combine.SMOTETomek`

  Param Distributions

	0. "default" ::

		defaults only


svm smote
*********

  Base Class Documenation: :class:`imblearn.over_sampling.SVMSMOTE`

  Param Distributions

	0. "default" ::

		defaults only


tomek links
***********

  Base Class Documenation: :class:`imblearn.under_sampling.TomekLinks`

  Param Distributions

	0. "default" ::

		defaults only



regression
==========

categorical multilabel
======================

categorical multiclass
======================
adasyn
******

  Base Class Documenation: :class:`imblearn.over_sampling.ADASYN`

  Param Distributions

	0. "default" ::

		defaults only


all knn
*******

  Base Class Documenation: :class:`imblearn.under_sampling.AllKNN`

  Param Distributions

	0. "default" ::

		defaults only


borderline smote
****************

  Base Class Documenation: :class:`imblearn.over_sampling.BorderlineSMOTE`

  Param Distributions

	0. "default" ::

		defaults only


cluster centroids
*****************

  Base Class Documenation: :class:`imblearn.under_sampling.ClusterCentroids`

  Param Distributions

	0. "default" ::

		defaults only


condensed nn
************

  Base Class Documenation: :class:`imblearn.under_sampling.CondensedNearestNeighbour`

  Param Distributions

	0. "default" ::

		defaults only


enn
***

  Base Class Documenation: :class:`imblearn.under_sampling.EditedNearestNeighbours`

  Param Distributions

	0. "default" ::

		defaults only


kmeans smote
************

  Base Class Documenation: :class:`imblearn.over_sampling.KMeansSMOTE`

  Param Distributions

	0. "default" ::

		defaults only


near miss
*********

  Base Class Documenation: :class:`imblearn.under_sampling.NearMiss`

  Param Distributions

	0. "default" ::

		defaults only


neighbourhood cleaning rule
***************************

  Base Class Documenation: :class:`imblearn.under_sampling.NeighbourhoodCleaningRule`

  Param Distributions

	0. "default" ::

		defaults only


one sided selection
*******************

  Base Class Documenation: :class:`imblearn.under_sampling.OneSidedSelection`

  Param Distributions

	0. "default" ::

		defaults only


random over sampler
*******************

  Base Class Documenation: :class:`imblearn.over_sampling.RandomOverSampler`

  Param Distributions

	0. "default" ::

		defaults only


random under sampler
********************

  Base Class Documenation: :class:`imblearn.under_sampling.RandomUnderSampler`

  Param Distributions

	0. "default" ::

		defaults only


renn
****

  Base Class Documenation: :class:`imblearn.under_sampling.RepeatedEditedNearestNeighbours`

  Param Distributions

	0. "default" ::

		defaults only


smote
*****

  Base Class Documenation: :class:`imblearn.over_sampling.SMOTE`

  Param Distributions

	0. "default" ::

		defaults only


smote enn
*********

  Base Class Documenation: :class:`imblearn.combine.SMOTEENN`

  Param Distributions

	0. "default" ::

		defaults only


smote nc
********

  Base Class Documenation: :class:`imblearn.over_sampling.SMOTENC`

  Param Distributions

	0. "default" ::

		defaults only


smote tomek
***********

  Base Class Documenation: :class:`imblearn.combine.SMOTETomek`

  Param Distributions

	0. "default" ::

		defaults only


svm smote
*********

  Base Class Documenation: :class:`imblearn.over_sampling.SVMSMOTE`

  Param Distributions

	0. "default" ::

		defaults only


tomek links
***********

  Base Class Documenation: :class:`imblearn.under_sampling.TomekLinks`

  Param Distributions

	0. "default" ::

		defaults only



**************
Feat Selectors
**************

binary
======
rfe
***

  Base Class Documenation: :class:`ABCD_ML.Feature_Selectors.RFE`

  Param Distributions

	0. "base rfe" ::

		n_features_to_select: None

	1. "rfe num feats rs" ::

		n_features_to_select: Random Uniform Distribution (0.0, 1.0)


univariate selection classification
***********************************

  Base Class Documenation: :class:`sklearn.feature_selection.SelectPercentile`

  Param Distributions

	0. "base univar fs classifier" ::

		score_func: f_classif
		percentile: 50

	1. "univar fs classifier rs" ::

		score_func: f_classif
		percentile: Random Integer Distribution (1, 98)

	2. "univar fs classifier gs" ::

		score_func: f_classif
		percentile: [10, 20, 30, 40, 50, 60, 70, 80, 90]



regression
==========
rfe
***

  Base Class Documenation: :class:`ABCD_ML.Feature_Selectors.RFE`

  Param Distributions

	0. "base rfe" ::

		n_features_to_select: None

	1. "rfe num feats rs" ::

		n_features_to_select: Random Uniform Distribution (0.0, 1.0)


univariate selection regression
*******************************

  Base Class Documenation: :class:`sklearn.feature_selection.SelectPercentile`

  Param Distributions

	0. "base univar fs regression" ::

		score_func: f_regression
		percentile: 50

	1. "univar fs regression rs" ::

		score_func: f_regression
		percentile: Random Integer Distribution (1, 98)

	2. "univar fs regression gs" ::

		score_func: f_regression
		percentile: [10, 20, 30, 40, 50, 60, 70, 80, 90]



categorical multilabel
======================

categorical multiclass
======================
rfe
***

  Base Class Documenation: :class:`ABCD_ML.Feature_Selectors.RFE`

  Param Distributions

	0. "base rfe" ::

		n_features_to_select: None

	1. "rfe num feats rs" ::

		n_features_to_select: Random Uniform Distribution (0.0, 1.0)


univariate selection classification
***********************************

  Base Class Documenation: :class:`sklearn.feature_selection.SelectPercentile`

  Param Distributions

	0. "base univar fs classifier" ::

		score_func: f_classif
		percentile: 50

	1. "univar fs classifier rs" ::

		score_func: f_classif
		percentile: Random Integer Distribution (1, 98)

	2. "univar fs classifier gs" ::

		score_func: f_classif
		percentile: [10, 20, 30, 40, 50, 60, 70, 80, 90]



***************
Ensemble Types
***************

binary
======
aposteriori
***********

  Base Class Documenation: :class:`deslib.dcs.a_posteriori.APosteriori`

  Param Distributions

	0. "default" ::

		defaults only


apriori
*******

  Base Class Documenation: :class:`deslib.dcs.a_priori.APriori`

  Param Distributions

	0. "default" ::

		defaults only


des clustering
**************

  Base Class Documenation: :class:`deslib.des.des_clustering.DESClustering`

  Param Distributions

	0. "default" ::

		defaults only


des knn
*******

  Base Class Documenation: :class:`deslib.des.des_knn.DESKNN`

  Param Distributions

	0. "default" ::

		defaults only


deskl
*****

  Base Class Documenation: :class:`deslib.des.probabilistic.DESKL`

  Param Distributions

	0. "default" ::

		defaults only


desmi
*****

  Base Class Documenation: :class:`deslib.des.des_mi.DESMI`

  Param Distributions

	0. "default" ::

		defaults only


desp
****

  Base Class Documenation: :class:`deslib.des.des_p.DESP`

  Param Distributions

	0. "default" ::

		defaults only


exponential
***********

  Base Class Documenation: :class:`deslib.des.probabilistic.Exponential`

  Param Distributions

	0. "default" ::

		defaults only


knop
****

  Base Class Documenation: :class:`deslib.des.knop.KNOP`

  Param Distributions

	0. "default" ::

		defaults only


knorae
******

  Base Class Documenation: :class:`deslib.des.knora_e.KNORAE`

  Param Distributions

	0. "default" ::

		defaults only


knrau
*****

  Base Class Documenation: :class:`deslib.des.knora_u.KNORAU`

  Param Distributions

	0. "default" ::

		defaults only


lca
***

  Base Class Documenation: :class:`deslib.dcs.lca.LCA`

  Param Distributions

	0. "default" ::

		defaults only


logarithmic
***********

  Base Class Documenation: :class:`deslib.des.probabilistic.Logarithmic`

  Param Distributions

	0. "default" ::

		defaults only


mcb
***

  Base Class Documenation: :class:`deslib.dcs.mcb.MCB`

  Param Distributions

	0. "default" ::

		defaults only


metades
*******

  Base Class Documenation: :class:`deslib.des.meta_des.METADES`

  Param Distributions

	0. "default" ::

		defaults only


min dif
*******

  Base Class Documenation: :class:`deslib.des.probabilistic.MinimumDifference`

  Param Distributions

	0. "default" ::

		defaults only


mla
***

  Base Class Documenation: :class:`deslib.dcs.mla.MLA`

  Param Distributions

	0. "default" ::

		defaults only


ola
***

  Base Class Documenation: :class:`deslib.dcs.ola.OLA`

  Param Distributions

	0. "default" ::

		defaults only


rank
****

  Base Class Documenation: :class:`deslib.dcs.rank.Rank`

  Param Distributions

	0. "default" ::

		defaults only


rrc
***

  Base Class Documenation: :class:`deslib.des.probabilistic.RRC`

  Param Distributions

	0. "default" ::

		defaults only


single best
***********

  Base Class Documenation: :class:`deslib.static.single_best.SingleBest`

  Param Distributions

	0. "default" ::

		defaults only


stacked
*******

  Base Class Documenation: :class:`deslib.static.stacked.StackedClassifier`

  Param Distributions

	0. "default" ::

		defaults only



regression
==========

categorical multilabel
======================

categorical multiclass
======================
aposteriori
***********

  Base Class Documenation: :class:`deslib.dcs.a_posteriori.APosteriori`

  Param Distributions

	0. "default" ::

		defaults only


apriori
*******

  Base Class Documenation: :class:`deslib.dcs.a_priori.APriori`

  Param Distributions

	0. "default" ::

		defaults only


des clustering
**************

  Base Class Documenation: :class:`deslib.des.des_clustering.DESClustering`

  Param Distributions

	0. "default" ::

		defaults only


des knn
*******

  Base Class Documenation: :class:`deslib.des.des_knn.DESKNN`

  Param Distributions

	0. "default" ::

		defaults only


deskl
*****

  Base Class Documenation: :class:`deslib.des.probabilistic.DESKL`

  Param Distributions

	0. "default" ::

		defaults only


desmi
*****

  Base Class Documenation: :class:`deslib.des.des_mi.DESMI`

  Param Distributions

	0. "default" ::

		defaults only


desp
****

  Base Class Documenation: :class:`deslib.des.des_p.DESP`

  Param Distributions

	0. "default" ::

		defaults only


exponential
***********

  Base Class Documenation: :class:`deslib.des.probabilistic.Exponential`

  Param Distributions

	0. "default" ::

		defaults only


knop
****

  Base Class Documenation: :class:`deslib.des.knop.KNOP`

  Param Distributions

	0. "default" ::

		defaults only


knorae
******

  Base Class Documenation: :class:`deslib.des.knora_e.KNORAE`

  Param Distributions

	0. "default" ::

		defaults only


knrau
*****

  Base Class Documenation: :class:`deslib.des.knora_u.KNORAU`

  Param Distributions

	0. "default" ::

		defaults only


lca
***

  Base Class Documenation: :class:`deslib.dcs.lca.LCA`

  Param Distributions

	0. "default" ::

		defaults only


logarithmic
***********

  Base Class Documenation: :class:`deslib.des.probabilistic.Logarithmic`

  Param Distributions

	0. "default" ::

		defaults only


mcb
***

  Base Class Documenation: :class:`deslib.dcs.mcb.MCB`

  Param Distributions

	0. "default" ::

		defaults only


metades
*******

  Base Class Documenation: :class:`deslib.des.meta_des.METADES`

  Param Distributions

	0. "default" ::

		defaults only


min dif
*******

  Base Class Documenation: :class:`deslib.des.probabilistic.MinimumDifference`

  Param Distributions

	0. "default" ::

		defaults only


mla
***

  Base Class Documenation: :class:`deslib.dcs.mla.MLA`

  Param Distributions

	0. "default" ::

		defaults only


ola
***

  Base Class Documenation: :class:`deslib.dcs.ola.OLA`

  Param Distributions

	0. "default" ::

		defaults only


rank
****

  Base Class Documenation: :class:`deslib.dcs.rank.Rank`

  Param Distributions

	0. "default" ::

		defaults only


rrc
***

  Base Class Documenation: :class:`deslib.des.probabilistic.RRC`

  Param Distributions

	0. "default" ::

		defaults only


single best
***********

  Base Class Documenation: :class:`deslib.static.single_best.SingleBest`

  Param Distributions

	0. "default" ::

		defaults only


stacked
*******

  Base Class Documenation: :class:`deslib.static.stacked.StackedClassifier`

  Param Distributions

	0. "default" ::

		defaults only


