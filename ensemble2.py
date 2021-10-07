import pandas as pd

a = pd.read_csv("../output/seed_resnet200_3_not90_tta.csv")
b = pd.read_csv('../output/seed_resnet200_3_1e4_tta.csv')

# for e, (i, j, h) in enumerate(zip(a['ST1_GAP(eV)'], b['ST1_GAP(eV)'], c['ST1_GAP(eV)'])):
#     a['ST1_GAP(eV)'][e] = (i + j + h) / 3
# print(a)
# a.to_csv('../output/ensemble_test2.csv', index=False)
for e, (i, j) in enumerate(zip(a['ST1_GAP(eV)'], b['ST1_GAP(eV)'])):
    a['ST1_GAP(eV)'][e] = (i + j) / 2
print(a)
a.to_csv('../output/seed_ensemble2.csv', index=False)
