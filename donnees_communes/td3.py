import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
donneesCommunes = pd.read_csv(f'donnees_communes/RGC_2013.csv',sep=';')
donneesSalaries = pd.read_csv(f'donnees_communes/Emplois_salaries.csv',sep=';')
donneesCommunes['DEP'] = donneesCommunes['DEP'].astype(str)
donneesCommunes['COM'] = donneesCommunes['COM'].astype(str)
donneesSalaries['CODGEO'] = donneesSalaries['CODGEO'].astype(str)
donneesCommunes.insert(2,"COG",donneesCommunes['DEP']+donneesCommunes['COM'].str.zfill(3))

def associate_arr_mun(num_dep,cod_com,num_arr_debut,num_arr_fin):
    list_arr_com=[str(num_dep)+str(num_arr).zfill(3) for num_arr in \
                  range(num_arr_debut,num_arr_fin+1)]
    mask=donneesSalaries['CODGEO'].str.zfill(5).isin(list_arr_com)
    data_emplois_commune=donneesSalaries[mask].sum()
    data_emplois_commune['CODGEO']=str(cod_com)
    donneesSalaries.loc[len(donneesSalaries)]=data_emplois_commune.values
 
donneesCommunesPop = donneesCommunes[donneesCommunes["POPU"]>0][["COG","POPU"]]

associate_arr_mun(75,75056,101,120)
associate_arr_mun(13,13055,201,216)
associate_arr_mun(69,69123,381,389)

jointure = pd.merge(donneesSalaries,donneesCommunesPop,'inner',left_on="CODGEO",right_on="COG")[["CODGEO","EFF_TOT","POPU"]]
jointure.insert(3,"Ratio",jointure["EFF_TOT"]/(jointure["POPU"]*100))
plt.boxplot(jointure["Ratio"]*100,showfliers=False,showmeans=True)
plt.title("Repartition ratio salarié/ habitants par commune")
plt.show()