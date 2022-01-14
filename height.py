import plotly.figure_factory as ff
import pandas as pandas
import csv

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
fig.show()