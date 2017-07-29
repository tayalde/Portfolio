"""
SYNOPSIS
    titanic.py [-h, --help] [-i, --infile] [-p, --plot] [-t, --table]
               [-s, --summary]
DESCRIPTION
    Runs exploratory analysis on Titanic dataset
EXAMPLES
    titanic.py -i data/working/train.csv -p
AUTHOR
    Thomas Ayalde (tayalde268@gmail.com)
"""

import argparse as ap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def match_case(factor):
    """ Auxiliary function to capitalize the first letter of the chosen factors.
    """
    try:
        for idx, item in enumerate(factor):
            factor[idx] = item.title()
    except TypeError:
        factor = factor.title()
    return factor


def explore_plots(df, index, factor):
    """ Uses pandas df and seaborn countplots to run adhoc A/B tests.
    """
    ax = sns.countplot(x=index, hue=factor, data=df)
    plt.show()
    return


def explore_crosstabs(df, index, factors):
    """ Uses pandas df to make crosstabs for the given args.
    """
    freq_table = pd.crosstab(df[index], [df[x] for x in factors], margins=True)
    return freq_table


if __name__ == "__main__":
    desc = "Runs analysis on Titanic dataset"
    parser = ap.ArgumentParser(description=desc)

    parser.add_argument('-i', '--infile', type=str,
                        help="input file name")
    parser.add_argument('-p', '--plot', action='store_true',
                        help="flags plots")
    parser.add_argument('-t', '--table', action='store_true',
                        help="flags crosstab")
    parser.add_argument('-s', '--summary', action='store_true',
                        help="flags summary")

    args = parser.parse_args()

    check = False
    df = pd.read_csv(args.infile)
    cols = df.columns.tolist()

    if args.summary:
        print(df.describe(), "\n\nThe number of NaN found in each column is:")
        print(df.isnull().sum())

    if args.table or args.plot:
        while not check:
            print("Here is a list of factors: \n", cols)
            index = input("\nSelect index: \n").lower()
            if index in map(lambda x: x.lower(), cols):
                check = True
            else:
                print("Not a factor. \n")

    if args.table:
        check = False
        factors = []
        while not check:
            print("Here is a list of factors: \n", cols)
            factor = input("\nSelect factor: \n").lower()
            if factor in map(lambda x: x.lower(), cols):
                factors.append(factor)
                if input("Would you like to add another? (Y/N) \n") is not "Y":
                    check = True
                elif len(factors) > 2:
                    print("Sorry, you can only pick 3.")
                    check = True
            else:
                print("Not a factor. \n")
        try:
            a, b = list(map(match_case, [index, factors]))
            print(explore_crosstabs(df, a, b))
        except ValueError:
            print("Check args you bozo")

    if args.plot:
        check = False
        while not check:
            print("Here is a list of factors: \n", cols)
            factor = input("\nSelect factor: \n").lower()
            if factor in map(lambda x: x.lower(), cols):
                check = True
            else:
                print("Not a factor. \n")
        try:
            a, b = list(map(match_case, [index, factor]))
            explore_plots(df, a, b)
        except ValueError:
            print("Check args you bozo")
