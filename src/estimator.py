import numpy as np

from sklearn.base import BaseEstimator, ClassifierMixin

from sklearn.utils.validation import validate_data, check_is_fitted

from sklearn.utils.multiclass import unique_labels

from sklearn.metrics import euclidean_distances

from sklearn import datasets


iris_X, iris_y = datasets.load_iris(return_X_y=True)
np.unique(iris_y)

# den Datensatz in zwei teile für test und training aufspalten
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
X = iris_X[indices[:-10]]
Y = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

class TemplateClassifier(ClassifierMixin, BaseEstimator):


    def __init__(self):

        pass


    def fit(self, X, y):


        # Check that X and y have correct shape, set n_features_in_, etc.

        X, y = validate_data(self, X, y)

        # Store the classes seen during fit

        self.classes_ = unique_labels(y)


        self.X_ = X

        self.y_ = y

        # Return the classifier

        return self


    def predict(self, blume):


        # Check if fit has been called

        check_is_fitted(self)


        # Input validation

        iris_X_test = validate_data(self, blume, reset=False)


        closest = np.argmin(euclidean_distances(blume, self.X_), axis=1)

        return self.y_[closest]
    
meineklasse=TemplateClassifier()
blume=TemplateClassifier(iris_X_test[0])