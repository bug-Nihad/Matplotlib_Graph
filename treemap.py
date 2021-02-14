import pandas as pd
import matplotlib.pyplot as plt
import squarify

def treemap(df):
    col0 = list(df[df.columns[0]])
    col1 = list(df[df.columns[1]])
    squarify.plot(sizes=col0, label=col1, alpha=0.8)
    plt.show()


df = pd.read_csv('estonia-passenger-list.csv')        #Put file name here
treemap(df)