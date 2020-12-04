import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from classification_model.config import franquicia_categories, tipo_tarjeta_categories


class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.loc[:, self.columns]
        return X


class ConvertDtypes(BaseEstimator, TransformerMixin):
    def __init__(self, numerical: list, categorical: list):
        if not isinstance(numerical, list):
            self.numerical = [numerical]
        else:
            self.numerical = numerical
        if not isinstance(categorical, list):
            self.categorical = [categorical]
        else:
            self.categorical = categorical

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        for numerical in self.numerical:
            X[numerical] = pd.to_numeric(X[numerical])
        for categorical in self.categorical:
            if categorical == 'franquicia':
                categories = franquicia_categories
            else:
                categories = tipo_tarjeta_categories
            X[categorical] = pd.Categorical(X[categorical], categories=categories)
        return X


class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = pd.get_dummies(X, columns=self.columns)
        return X


class GetDataFrame(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = pd.DataFrame(X, columns=self.columns)
        return X
