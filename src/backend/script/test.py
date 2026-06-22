import pandas as pd
import json

df = pd.read_csv("data/sympto_patho_test.csv")
df["GROUPE"] = df["GROUPE"].ffill()
df = df.set_index(["CLASSIFICATION","SYMPTÔME SPÉ"])

del df["GROUPE"]

df = df.apply(pd.to_numeric, errors="coerce")

s = df.loc[("Age", "35 - 55")]
print(s[s >= 0.5])