#coding: utf-8

#Bon alors pour écrire le script d'analyse de texte il faut utiliser nlkt. Première étape j'importe nlkt sur python. Une fois que c'est fait j'importe tout ce dont j'ai besoin dans le script. 

import csv 
import nltk
import re, collections #https://codereview.stackexchange.com/questions/146800/read-a-csv-file-and-do-natural-language-processing-on-the-data
from nltk.tokenize import word_tokenize
from collections import Counter   # https://docs.python.org/3/library/collections.html
from nltk.tokenize import MWETokenizer

# Trois scénarios donc trois scripts différents : 
# 1- je veux analyser mes tweet en fonction de mes hastags (pour savoir quels mots sont associés #merdia #fakenews #journalope etc.. quels mots reviennent le plus souvent avec chancun d'eux)
# 2- ou je veux analyser mes tweets en fonction des @médias ( Je veux savoir quels mots reviennent le plus souvent avec @LeDevoir @BFMTV par exemple, qu'est ce qu'on dit sur ce média, qu'est ce qu'on lui reproche, quels #Hashtags sont les plus utilisés)
# 3- ou je veux analyser mes tweets adressés aux journalistes ( Je veux savoir quels mots reviennent le plus souvent avec @AMarieDussault par exemple, qu'est ce qu'on reproche le plus aux journalistes ou quels compliments lui sont réservés)


#Je me familiarise avec la fonction word_tokenize (ici directement TweetTokenizer)

#from nltk.tokenize import TweetTokenizer
#tknzr = TweetTokenizer()
# Essai = "Ceci est un tweet avec des emoticones  et des hashtags #merdias :-)"
#tknzr.tokenize(Essai)
#['Ceci', 'est', 'un', 'tweet', 'avec', 'des', 'emoticones', 'et', 'des', 'hashtags', '#merdias', ':-)']
# Essai2 = "Ceci est un : tweet avec des, emoticones,  et des. hashtags #merdias :-)"
#tknzr.tokenize(Essai2)
#['Ceci', 'est', 'un', ':', 'tweet', 'avec', 'des', ',', 'emoticones', ',', 'et', 'des', '.', 'hashtags', '#merdias', ':-)']
# Je remarque que mêmes les ponctuations sont considérées comme des mots. J'en déduis donc que dans mon script je vais devoir
# remplacer celles-ci par du vide/espace " " et cette fonction est .replace

#Chaque Tweet doit être séparé par mot (fonction word_tokenize) mais pour cela je dois déjà savoir comment les délimiter donc dans les tweets on retrouvent soit des espaces entre les mots soit des espaces " " ou ," "." ":" ou encore ";"
#ainsi j'ai trouvé la formule ici https://www.geeksforgeeks.org/python-string-split/ qui me donne ce code : str.split(separator, maxsplit). Je dois tout de même remplacer remplacer "," (etc) par " " (du vide)
# Une fois que j'ai tous les mots séparés je dois attribuer un nombre à chaque mot ( mot 1, mot 2, mot 3, mot 4) enfin de les comtabiliser par la suite. 



hashtags = ["#merdias","#journalope", "#merdia","#journaldegauche","#fakenews", "#radiopoubelle", "#bonjournalisme", "#presselibre","#freepress"]

h = str(hashtags)

for h in hashtags:
	fichier = "Bonne_version_hashtags2" + h + ".csv"

	token = nltk.word_tokenize(hashtags)
		#Sépare individuellement les mots tout en conservant les "'" pour le cas de don't, that's, etc. 
		count = {}
		#Crée un dictionnaire dans le but de compter les mots.

		for word in token:
			infos = []
			infos.append(data["#merdias"][i]["artist"]) 
			infos.append(data["#merdia"][i]["title"]) 
			infos.append(data["#journalope"][i]["album"]) 
			infos.append(data["#fakenews"][i]["year"])
			infos.append(data)
			infos.append(word.replace("_","'"))


remplacer ", " par " "
remplacer ":" par " "
remplacer "." par " "

str.split(separator, maxsplit) https://www.geeksforgeeks.org/python-string-split/