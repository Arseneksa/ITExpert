import numpy as np
import scipy.stats as st
import pandas as pd


df = pd.read_excel("Abundance.xlsx")
df = df.loc[(df["Block"]=="Block A")&(df["Year"]==2010)&(df["Species"]=="ELEPH")]

interval =st.norm.interval(
                 confidence=0.95,
                 loc=np.mean(df["Average_Encounter_Rate (n/km)"]),
                 scale=st.sem(df["Average_Encounter_Rate (n/km)"]))
print(df.info())
print(df.head())
print(np.mean(df["Average_Encounter_Rate (n/km)"]))
min,max =interval
print(min,max)