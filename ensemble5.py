import pandas as pd

a = pd.read_csv("../output/ensemble2.csv")
b = pd.read_csv('../output/ensemble4.csv')

for e, (i, j) in enumerate(zip(a['ST1_GAP(eV)'], b['ST1_GAP(eV)'])):
    a['ST1_GAP(eV)'][e] = (i + j) / 2
print(a)
a.to_csv('../output/ensemble5.csv', index=False)
