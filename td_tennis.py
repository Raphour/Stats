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
def evolutionRang(id):
    player = rankingFinal[rankingFinal['player_id']==id]
    player['week_title'] = pd.to_datetime(player['week_title'], format='%Y.%m.%d')
    player = player.sort_values(by='week_title')
    #Inverser l'axe y
    title = "Evolution du classement de "+donneesJoueurs[donneesJoueurs['player_id']==id]['first_name'].values[0]+" "+donneesJoueurs[donneesJoueurs['player_id']==id]['last_name'].values[0]
    evolution = player.plot(x='week_title',y='rank_number',title=title,figsize=(15, 10), fontsize=12,legend=False)
    plt.gca().invert_yaxis()
    evolution.set_xlabel("", fontsize=12)
    evolution.set_ylabel("Classement", fontsize=12)
    plt.show()



#Ex 3
def lienTaillePoints():
    joueurheight = donneesJoueurs[(donneesJoueurs['height_cm']>6.5)][['player_id','height_cm']]
    ServReussis = donneesMatchStats[(donneesMatchStats['winner_first_serve_points_won']<=donneesMatchStats['winner_first_serves_in'])&(donneesMatchStats['loser_first_serve_points_won']<=donneesMatchStats['loser_first_serves_in'])&(donneesMatchStats['winner_first_serves_in']>0)&(donneesMatchStats['loser_first_serves_in']>0)][['match_id','winner_first_serve_points_won','loser_first_serve_points_won','winner_first_serves_in','loser_first_serves_in']]
    winners = donneesScores.merge(ServReussis, on='match_id', how='inner')
    losers = donneesScores.merge(ServReussis, on='match_id', how='inner')
    winners = winners.merge(joueurheight, left_on='winner_player_id', right_on='player_id', how='inner')
    losers = losers.merge(joueurheight, left_on='loser_player_id', right_on='player_id', how='inner')
    winnerheight = winners[['player_id','height_cm','winner_first_serve_points_won','winner_first_serves_in']]
    loserheight = losers[['player_id','height_cm','loser_first_serve_points_won','loser_first_serves_in']]
    general = pd.concat([winnerheight,loserheight])
    general = general.groupby('player_id').mean()
    general['first_serve_points_won'] = (general['winner_first_serve_points_won']+general['loser_first_serve_points_won'])/(general['winner_first_serves_in']+general['loser_first_serves_in'])
    #Enlever les NaN
    general = general.dropna()
    print(general)
    plt.scatter(general['height_cm'],general['first_serve_points_won'],s=1)
    plt.title("Nuage de points des joueurs en fonction de leur taille et du nombre de points gagnés sur leur premier service")
    plt.xlabel("Taille en cm")
    plt.ylabel("Nombre de points gagnés sur le premier service")
    plt.yticks = np.arange(0.1,0.9,0.1)
    plt.show()

lienTaillePoints()