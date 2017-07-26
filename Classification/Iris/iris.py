import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import neighbors, datasets
from matplotlib.colors import ListedColormap

iris = datasets.load_iris()

fp = "E:\Python Workspace\Data Science Projects\Classification\Iris\data\working\iris_data.txt"

n_neighbors = 2
h = 0.02

sns.set(style="darkgrid")

data = pd.read_csv(fp,
                   names=["sepal_l", "sepal_w", "petal_l", "petal_w", "class"])

setosa = data.loc[data['class'] == 'Iris-setosa']
versicolor = data.loc[data['class'] == 'Iris-versicolor']
virginica = data.loc[data['class'] == 'Iris-virginica']

plt.xlabel("$Sepal\ Length\ (cm)$")
plt.ylabel("$Petal\ Length\ (cm)$")
plt.scatter(setosa.iloc[:, 0], setosa.iloc[:, 1], label="$Setosa$")
plt.scatter(versicolor.iloc[:, 0], versicolor.iloc[:, 1], label="$Versicolor$")
plt.scatter(virginica.iloc[:, 0], virginica.iloc[:, 1], label="$Virginica$")
plt.legend()
plt.show()

plt.xlabel("$Species$")
plt.ylabel("$Sepal\ Length\ (cm)$")
plt.boxplot([setosa.iloc[:, 0], versicolor.iloc[:, 0], virginica.iloc[:, 0]],
            labels=["$Setosa$", "$Versicolor$", "$Virginica$"])
plt.show()

plt.xlabel("$Species$")
plt.ylabel("$Sepal\ Width\ (cm)$")
plt.boxplot([setosa.iloc[:, 1], versicolor.iloc[:, 1], virginica.iloc[:, 1]],
            labels=["$Setosa$", "$Versicolor$", "$Virginica$"])
plt.show()

plt.xlabel("$Species$")
plt.ylabel("$Petal\ Length\ (cm)$")
plt.boxplot([setosa.iloc[:, 2], versicolor.iloc[:, 2], virginica.iloc[:, 2]],
            labels=["$Setosa$", "$Versicolor$", "$Virginica$"])
plt.show()

plt.xlabel("$Species$")
plt.ylabel("$Petal\ Width\ (cm)$")
plt.boxplot([setosa.iloc[:, 3], versicolor.iloc[:, 3], virginica.iloc[:, 3]],
            labels=["$Setosa$", "$Versicolor$", "$Virginica$"])
plt.show()

ax = sns.jointplot(x="sepal_l", y="sepal_w", data=setosa, kind="reg", space=0)
ax2 = sns.pairplot(data, hue="class", markers=["o", "s", "D"])

x = np.concatenate((setosa.iloc[:, :4],
                    versicolor.iloc[:, :4],
                    virginica.iloc[:, :4]))

X = x[:, 2:4]

y = np.sort(np.array([1, 2, 3] * 50))

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, z, cmap=cmap_light)

    plt.scatter(x[:, 2], x[:, 3], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class Classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

plt.show()
