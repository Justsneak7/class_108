import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df=pd.read_csv("class108/data.csv")
fig=ff.create_distplot([df["Height(Inches)"].to_list()], ["Height"], show_hist=False)
fig.show()