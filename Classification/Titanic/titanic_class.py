"""
SYNOPSIS
    titanic_class.py [-h, --help] [-i, --infile]
DESCRIPTION
    Runs exploratory analysis on Titanic dataset
EXAMPLES
    titanic.py -i data/working/train.csv -p
AUTHOR
    Thomas Ayalde (tayalde268@gmail.com)
"""

import argparse as ap
import pandas as pd
import random
import numpy as np
from sklearn import (
        datasets,
        svm,
        cross_validation,
        tree,
        preprocessing,
        metrics
        )
import sklearn.ensemble as ske
import tensorflow as tf
from tensorflow.contrib import skflow
from sklearn.tree import export_graphviz


fp = "E:\Python Workspace\Data Science Projects\Classification\Titanic\data\working\\train.csv"

titanic = pd.read_csv(fp)
titanic.columns
titanic['Survived'].mean()
class_sex_group = titanic.loc[:, "Survived":].groupby(['Pclass', 'Sex']).mean()
class_sex_group['Survived'].plot.bar()

titanic.count()
titanic = titanic.drop(['Cabin'], axis=1)
titanic = titanic.dropna()
titanic.count()


def preprocess_titanic(df):
    processed_df = df.copy()
    le = preprocessing.LabelEncoder()
    processed_df.Sex = le.fit_transform(processed_df.Sex)
    processed_df.Embarked = le.fit_transform(processed_df.Embarked)
    processed_df = processed_df.drop(['Name', 'Ticket'], axis=1)
    return processed_df


processed_df = preprocess_titanic(titanic)

X = processed_df.drop(['Survived'], axis=1).values
y = processed_df['Survived'].values

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf_dt = tree.DecisionTreeClassifier(max_depth=10)

clf_dt.fit(X_train, y_train)
clf_dt.score(X_test, y_test)

shuffle_validator = cross_validation.ShuffleSplit(len(X), n_iter=20,
                                                  test_size=0.2,
                                                  random_state=0)


def test_classifier(clf):
    scores = cross_validation.cross_val_score(clf, X, y, cv=shuffle_validator)
    print("Accuracy: %0.4f (+/- %0.2f)" % (scores.mean(), scores.std()))


test_classifier(clf_dt)


if __name__ == "__main__":
    desc = "Runs decision tree classifier for Titanic dataset"
    parser = ap.ArgumentParser(description=desc)

    parser.add_argument('-i', '--infile', type=str,
                        help="input file name")

    args = parser.parse_args()
    df = pd.read_csv(args.infile)
    cols = df.columns.tolist()
