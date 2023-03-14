import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table_clients = pd.read_csv('data/base_comptoir_espace_table_clients.csv',sep=';')
table_decisions_entreprises=pd.read_csv('data/base_comptoir_espace_table_decisions_entreprises.csv',sep=';')

fig, ax = plt.subplots()

annee = 2
produit = 1
choixClient = table_clients[(table_clients["CLI_CHOIX"]>0)&(table_clients["CLI_ANNEE"]==annee)&(table_clients["CLI_PROD"]==produit)]
nombreClients = choixClient["CLI_CHOIX"].value_counts()

plt.pie(nombreClients,labels=nombreClients.index,autopct='%1.0f%%',counterclock=False,startangle=110)
plt.title("Part de marché sur l'année" +str(annee)+  "en quantité des différentes entreprises sur le produit"+str(produit))

ClientParEntreprise = table_clients.groupby(["CLI_ANNEE","CLI_CHOIX"])
choixClientAnnee1 = table_clients[(table_clients["CLI_CHOIX"]>0)&(table_clients["CLI_ANNEE"]==1)][["CLI_PROD","CLI_CHOIX"]].value_counts()
print(choixClientAnnee1)
choixClientAnnee2 = table_clients[(table_clients["CLI_CHOIX"]>0)&(table_clients["CLI_ANNEE"]==2)][["CLI_PROD","CLI_CHOIX"]].value_counts()

print("----------------------------------")
print(choixClientAnnee2)
#plt.show()




