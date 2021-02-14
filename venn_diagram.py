import pandas as pd
from itertools import combinations as comb
from matplotlib_venn import venn2
from matplotlib import pyplot as plt

def venn_diagram(df):
    a = list(range(0, len(df.columns)))
    combination = comb(a, 2)        #Getting all possible combinations
    for each_comb in combination:
        col1 = df.columns[each_comb[0]]
        col2 = df.columns[each_comb[1]]
        set1 = set(df[col1])
        set2 = set(df[col2])
        venn2([set1, set2], set_labels=(col1, col2))
        plt.show()


df=pd.read_csv('estonia-passenger-list.csv')        #Put file name here
venn_diagram(df)