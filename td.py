import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
--LINUX/IUT
table_clients = pd.read_csv(f'data/base_comptoir_espace_table_clients.csv',sep=';')
table_decisions_entreprises=pd.read_csv(f'data/base_comptoir_espace_table_decisions_entreprises.csv',sep=';')
'''


# WINDOWS / MAISON
table_clients = pd.read_csv(r'd:\Work\Stats\Stats\data\base_comptoir_espace_table_clients.csv',sep=';')
table_decisions_entreprises=pd.read_csv(r'd:\Work\Stats\Stats\data\base_comptoir_espace_table_decisions_entreprises.csv',sep=';')


# EXERCICE 1
'''
fig, ax = plt.subplots()

annee = 2
produit = 1
choixClient = table_clients[(table_clients["CLI_CHOIX"]>0)&(table_clients["CLI_ANNEE"]==annee)&(table_clients["CLI_PROD"]==produit)]
nombreClients = choixClient["CLI_CHOIX"].value_counts()


# Affichage du camembert
plt.pie(nombreClients,labels=nombreClients.index,autopct='%1.0f%%',counterclock=False,startangle=110)
plt.title("Part de marché sur l'année" +str(annee)+  "en quantité des différentes entreprises sur le produit"+str(produit))

'''

choixClientAnnee1 = table_clients[(table_clients["CLI_CHOIX"]>0)&(table_clients["CLI_ANNEE"]==1)][["CLI_CHOIX","CLI_PROD","CLI_ANNEE"]].value_counts()
choixClientAnnee2 = table_clients[(table_clients["CLI_CHOIX"]>0)&(table_clients["CLI_ANNEE"]==2)][["CLI_PROD","CLI_CHOIX","CLI_ANNEE"]].value_counts()

# Statistiques pour l'année 1
prixProduitAnnee1 = table_decisions_entreprises[(table_decisions_entreprises["ENT_ANNEE"]==1)][["ENT_ID","ENT_PRIX","ENT_PROD","ENT_ANNEE"]]
entAvecChoixAnnee1 = pd.merge(choixClientAnnee1.rename('Nombre_Choix'),prixProduitAnnee1,how="left",left_on=["CLI_CHOIX","CLI_ANNEE","CLI_PROD"],right_on=["ENT_ID","ENT_ANNEE","ENT_PROD"])
chiffreAffaireAnnee1 = (entAvecChoixAnnee1["Nombre_Choix"] * entAvecChoixAnnee1["ENT_PRIX"])
chiffreAffaireTableAnnee1 =pd.merge(entAvecChoixAnnee1,chiffreAffaireAnnee1.rename("Chiffre_Affaire"),left_index=True,right_index=True)[["ENT_ID","ENT_PROD","Chiffre_Affaire"]]
chiffreAffaireTableAnnee1 = chiffreAffaireTableAnnee1.groupby(["ENT_ID"])['Chiffre_Affaire'].sum()


# Statistiques pour l'année 2
prixProduitAnnee2 = table_decisions_entreprises[(table_decisions_entreprises["ENT_ANNEE"]==2)][["ENT_ID","ENT_PRIX","ENT_PROD","ENT_ANNEE"]]
entAvecChoixAnnee2 = pd.merge(choixClientAnnee2.rename('Nombre_Choix'),prixProduitAnnee2,how="left",left_on=["CLI_CHOIX","CLI_ANNEE","CLI_PROD"],right_on=["ENT_ID","ENT_ANNEE","ENT_PROD"])
chiffreAffaireAnnee2 = (entAvecChoixAnnee2["Nombre_Choix"] * entAvecChoixAnnee2["ENT_PRIX"])
chiffreAffaireTableAnnee2 =pd.merge(entAvecChoixAnnee2,chiffreAffaireAnnee2.rename("Chiffre_Affaire"),left_index=True,right_index=True)[["ENT_ID","ENT_PROD","Chiffre_Affaire"]]
chiffreAffaireTableAnnee2 = chiffreAffaireTableAnnee2.groupby(["ENT_ID"])['Chiffre_Affaire'].sum()

# Affichage des résultats
x=np.arange(1,6)

x_labels = ["Entreprise"+str(i) for i in range (1,6) ]
plt.xticks(x, x_labels, color='black', fontweight='bold', fontsize='9')

width = 0.3
plt.bar(x-width/2,chiffreAffaireTableAnnee1,width)
plt.bar(x+width/2,chiffreAffaireTableAnnee2,width)
plt.legend(['Année 1', 'Année 2'], loc='upper left')
plt.show()





