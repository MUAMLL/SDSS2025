import geoplot as gplt
import geopandas as gpd
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt



st.set_page_config(page_title="U.S. Cities By State", layout="wide")
st.header("U.S. Cities By State")


usa_cities = gpd.read_file(gplt.datasets.get_path('usa_cities'))
state = st.selectbox("Choose State", usa_cities.STATE.unique())


col1, col2 = st.columns(2, vertical_alignment="top")

col1.subheader("Cities")
col2.subheader("Map")

df = usa_cities[usa_cities.STATE == state].reset_index(drop=True)
df2 = df.drop(columns=["geometry"]).copy()
col1.dataframe(df2)


df["lon"] = df.geometry.apply(lambda x: x.x)
df["lat"] = df.geometry.apply(lambda x: x.y)
col2.map(df, longitude="lon", latitude="lat")