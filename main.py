import plotly.express as px
import pandas as pd


def spider_graph(df):
    name = list(df['Firstname'])
    age = list(df['Age'])
    df = pd.DataFrame(dict(
        age = age,
        name = name
    ))
    fig = px.line_polar(df, r='age', theta='name', line_close=True)
    fig.show()

df = pd.read_csv('estonia-passenger-list.csv')
spider_graph(df)