import pandas as pd
import json

sexe = "Femme"
Age = "70 - 100"
motif = "dorsalgie haute"

df = pd.read_csv("data/sympto_patho_test.csv")
df["GROUPE"] = df["GROUPE"].ffill()
df = df.set_index(["CLASSIFICATION","SYMPTÔME SPÉ"])

del df["GROUPE"]

df = df.apply(pd.to_numeric, errors="coerce")

s_sex = df.loc[("Sexe", sexe)]
s_age = df.loc[("Age", Age)]
s_motif = df.loc[("Motif", motif)]

mask = (s_sex > 0) & (s_age > 0) & (s_motif > 0)
list_conv = s_age.index[mask].tolist()

motifs = df.loc["Motif"]
motifs = motifs[motifs.index != motif][list_conv]
motifs_index = motifs.index
result = motifs[(motifs > 0).sum(axis=1) == 1].index.tolist()
print(df[list_conv])
print(result)