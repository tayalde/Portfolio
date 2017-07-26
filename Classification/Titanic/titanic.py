"""
SYNOPSIS
    titanic.py [-h, --help] [-i, --infile]
DESCRIPTION
    Runs exploratory analysis on Titanic dataset
EXAMPLES
    titanic.py -i data/working/train.csv "
AUTHOR
    Thomas Ayalde (tayalde268@gmail.com)
"""

import argparse as ap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def explore_plots(df, index, factor):
    """ Uses pandas df and seaborn countplots to run adhoc A/B tests.
    """
    # ax = sns.countplot(x=index, hue=factor, data=df)
    # plt.plot()
    print(index, factor)
    return


def explore_crosstabs(df, index, factors):
    """ Uses pandas df to make crosstabs for the given args.
    """
    print(index, factors)
    return


# sns.set(style="whitegrid", rc={"lines.color": 'r', "lines.linewidth": 10})
#
#
# titanic = pd.read_csv(fp)
#
#
#
# ax2 = sns.countplot(x="Pclass", hue="Survived", data=titanic)
#
# ax3 = sns.countplot(x="Embarked", hue="Survived", data=titanic)
#
# freq_table_sex = pd.crosstab(titanic["Sex"],
#                              titanic["Survived"],
#                              margins=True)
#
# freq_table_sex_class = pd.crosstab([titanic["Sex"], titanic["Pclass"]],
#                                    titanic["Survived"],
#                                    margins=True)

# pd.isnull(titanic).sum()


if __name__ == "__main__":
    desc = "Runs analysis on Titanic dataset"
    parser = ap.ArgumentParser(description=desc)

    parser.add_argument('-i', '--infile', type=str, help="input file name")
    parser.add_argument('-p', '--plot', action='store_true', help="flags plots")
    parser.add_argument('--table', action='store_true', help="flags crosstab")
    parser.add_argument('--summary', action='store_true', help="flags summary")

    args = parser.parse_args()

    check = False
    df = pd.read_csv(args.infile)
    cols = df.columns.tolist()
    while not check:
        print("Here is a list of factors: \n", cols)
        index = input("\n Select index: \n")
        if index.lower() in map(lambda x: x.lower(), cols):
            check = True
        else:
            print("Not a factor. \n")

    # print(factors, type(factors))

    if args.summary:
        print(df.describe())

    if args.table:
        check = False
        factors = []
        while not check:
            print("Here is a list of factors: \n", cols)
            factor = input("\n Select factor: \n")
            if factor.lower() in map(lambda x: x.lower(), cols):
                factors.append(factor)
                if input("Would you like to add another? (Y/N) \n") is "N":
                    check = True
                elif len(factors) > 2:
                    print("Sorry you can only pick 3.")
                    check = True
            else:
                print("Not a factor. \n")
        try:
            explore_crosstabs(df, index, factors)
        except ValueError:
            print("Check args you bozo")

    if args.plot:
        check = False
        while not check:
            print("Here is a list of factors: \n", cols)
            factor = input("\n Select factor: \n")
            if factor.lower() in map(lambda x: x.lower(), cols):
                check = True
            else:
                print("Not a factor. \n")
        try:
            explore_plots(df, index, factor)
        except ValueError:
            print("Check args you bozo")
