import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("class108/data.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].to_list()], ["Weight"], show_hist=False)
fig.show()
