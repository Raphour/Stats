from scipy.stats import linregress
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table_clients = pd.read_csv(f'data/base_comptoir_espace_table_clients.csv',sep=';')
table_decisions_entreprises=pd.read_csv(f'data/base_comptoir_espace_table_decisions_entreprises.csv',sep=';')
annee = 1
produit = 1
confortClient = table_clients[(table_clients["CLI_ANNEE"]==annee)&(table_clients["CLI_PROD"]==produit)]["CLI_CONFORT"]
prixClient = table_clients[(table_clients["CLI_ANNEE"]==annee)&(table_clients["CLI_PROD"]==produit)]["CLI_PRIX"]
confortEntreprise = table_decisions_entreprises[(table_decisions_entreprises["ENT_ANNEE"]==annee)&(table_decisions_entreprises["ENT_PROD"]==produit)]["ENT_CONF"]
prixEntreprise=table_decisions_entreprises[(table_decisions_entreprises["ENT_ANNEE"]==annee)&(table_decisions_entreprises["ENT_PROD"]==produit)]["ENT_PRIX"]
print(confortClient)
res_reg=linregress(prixClient,confortClient)
a=res_reg.slope
b=res_reg.intercept
coef_cor=res_reg.rvalue
x = np.arange(0,33000,1)
modele_confort = a * x + b
plt.plot(modele_confort,"r-")

plt.title("Etude d'une corrélation entre attentes sur prix et cout confort sur le produit {} sur l'année {}".format(produit,annee))
categories = np.array([0, 1, 2,3])

# use colormap
colormap = np.array(['tab:olive', 'b', 'r','tab:orange'])

plt.scatter(prixClient,confortClient)
plt.scatter(prixEntreprise,confortEntreprise,c=colormap[categories])
plt.yticks(np.arange(start=0,step=500,stop=4000))
plt.show()