import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", rc={"lines.color": 'r', "lines.linewidth": 10})

titanic = pd.read_csv('E:\Python Workspace\Data Science Projects'
                      + '\Titanic Classification\data\working\\train.csv')

titanic

ax = sns.countplot(x="Sex", hue="Survived", data=titanic)

ax2 = sns.countplot(x="Pclass", hue="Survived", data=titanic)

ax3 = sns.countplot(x="Embarked", hue="Survived", data=titanic)
