import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df = df.rename({
    'starnames':"Star_names",
    'distance':"Distance",
    'mass':"Mass",
    'radius':"radius"
}, axis="columns")

df.to_csv("total_stars_again_but_why_do_i_have_to_do_this.csv")