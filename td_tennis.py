import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

donneesJoueurs = pd.read_csv(f'data_tennis/data_players.csv',sep=',')
donneesScores= pd.read_csv(f'data_tennis/match_scores.csv',sep=',')
donneesMatchStats = pd.read_csv(f'data_tennis/match_stats.csv',sep=',')
donneesRanking = pd.read_csv(f'data_tennis/rankings.csv',sep=',')
donneesRanking2= pd.read_csv(f'data_tennis/rankings_2.csv',sep=',')
donneesRanking3 = pd.read_csv(f'data_tennis/rankings_3.csv',sep=',')
rankingFinal = pd.concat([donneesRanking,donneesRanking2,donneesRanking3])
donneesTournois = pd.read_csv(f'data_tennis/tournaments.csv',sep=',')

#Ex1
def tailleJoueurs(anneeNaissance):
    joueursPlusgrandsque = donneesJoueurs[donneesJoueurs["height_cm"]>6.5]
    tailleJoueursNesApres = joueursPlusgrandsque[joueursPlusgrandsque["birth_year"]>= anneeNaissance]["height_cm"]

    print("Nombre de joueur(s) concernés ", len(tailleJoueursNesApres))
    print("Moyenne taille des joueur(s) concernés ", tailleJoueursNesApres.mean())
    print("Médiane taille des joueur(s) concernés ", tailleJoueursNesApres.median())
    print("Ecart type taille des joueur(s) concernés ", tailleJoueursNesApres.std())
    x = np.arange(tailleJoueursNesApres.min(),tailleJoueursNesApres.max(),5)
    bins = []
    for i in range(int(tailleJoueursNesApres.min()),int(tailleJoueursNesApres.max())):
        if i % 5 == 0:
            bins.append(i)
    plt.hist(tailleJoueursNesApres,bins=x,ec="black")
    plt.title("Distribution des tailles des joueurs nés à partir de "+ str(anneeNaissance))
    plt.show()


#Ex2
def evolutionRang(identifiant):


    rechercheJoueurIdentifiant = donneesJoueurs[donneesJoueurs["player_id"]==identifiant]

    rankingJoueur = rankingFinal[rankingFinal["player_id"]==identifiant]["rank_number"]
    
    dateRank = rankingFinal[rankingFinal["player_id"]==identifiant]["week_title"]
    dateRankNumpy = np.array([date for date in dateRank])
    dates = np.array([datetime.datetime(int(date[0:4]),int(date[5:7]),int(date[8:11])) for date in dateRankNumpy])

    ordreDates = np.argsort(dates)

    datesRangees = dateRankNumpy[ordreDates]

 



    plt.plot(datesRangees, rankingJoueur)
    plt.ylim(max(rankingJoueur)+5,min(rankingJoueur)-5)

    plt.locator_params(axis='x', nbins=3)
    
    plt.show()



#Ex 3
def lienTaillePoints():
    