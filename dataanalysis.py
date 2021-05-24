import pandas as pb
import csv
import plotly.express as px
df = pb.read_csv("dataanalysis.csv")
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = px.scatter(
    mean,
    x = "student_id",
    y = "level",
    size = "attempt",
    color = "attempt"
)
fig.show()