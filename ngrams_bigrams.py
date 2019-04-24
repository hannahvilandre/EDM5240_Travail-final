#coding: utf-8

# import nltk
import csv, codecs
import numpy as np 
import pandas as pan 
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from collections import Counter
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.tokenize import TweetTokenizer
# from bigrams import find_bigrams
# from mots_vides import rien
# import treetaggerwrapper

# nltk.download()
fichiers = ["twitter_medias.csv", "twitter_journalistes.csv"]
fich = ["out.csv"]
# data = pan.read_csv("twitter_médias.csv")
# docs = data["Tweet"].tolist()
# print(docs)

# rep = input("On veut mots seuls (0), bigrammes (1) ou trigrammes (2)?")

# tag = treetaggerwrapper.TreeTagger(TAGLANG='fr')

stop_words = list(stopwords.words("french"))
# stop_words = (list(words.split("\n")))
# stop_words = (list[(stopwords.words("french"), (words.split("\n")))])
stop_words.append("http")
stop_words.append("https")
stop_words.append("les")
stop_words.append("là")
stop_words.append("si")
stop_words.append("ils")
# stop_words.append("@")
# # stop_words.append("\u2069")
# stop_words.append("#")
# # stop_words.append("\u2066")
# stop_words.append(": 1—")
# stop_words.append("//t.co")
# stop_words.append(".")
# stop_words.append(";")
# stop_words.append("&")
# stop_words.append("⤵️")
# stop_words.append("``")
# stop_words.append("''")
# print(stop_words)

nb = 0
liste = []

fichierOUTunigram = "twitter_unigrams.csv"
fichierOUTbigram = "twitter_bigrams.csv"
fichierOUTtrigram = "twitter_trigrams.csv"
fichierOUThashtag = "twitter_hashtags.csv"


for fichier in fichiers:
	f = open(fichier)
	lignes = csv.reader(f)
	# print(lignes)

	next(lignes)

	for ligne in lignes:
		# print(ligne)
		nb+=1
		# print(nb)
		# if ligne[8] == "québec":
		# print(nb, fichier, ligne)
		tweet = ligne[2]
		print(tweet)
		macron = TweetTokenizer()
		tokens = macron.tokenize(tweet)
		# print(tokens)
		# tokens = tokens.lower()
	# 	n=0
	# 	# # print(tokens)
		tokensPropres = []
		for token in tokens:
			# print(token)

	# 		# n+=1
	# 		token = token.lower()
			if token.lower() not in stop_words:
				if len(token) > 1:
					# print(token)
					if not token.startswith("http"):
		# # 				print(token)
						# if token.isalpha():
						tokensPropres.append(token.lower().strip())
		print(tokensPropres)

		for token in tokensPropres:
			if token[0] == "#":
				ying = open(fichierOUThashtag, "a")
				yang = csv.writer(ying)
				yang.writerow([token])
		
		for n in range(0, len(tokensPropres)):
			mot = ["{}".format(tokensPropres[n])]
			ying = open(fichierOUTunigram, "a")
			yang = csv.writer(ying)
			yang.writerow(mot)

		for n in range(0, len(tokensPropres)-1):
			# big = [tokensPropres[n], tokensPropres[n+1]]
			big = ["{} {}".format(tokensPropres[n], tokensPropres[n+1])]
			print(big)
			ying = open(fichierOUTbigram, "a")
			yang = csv.writer(ying)
			yang.writerow(big)

		for n in range(0, len(tokensPropres)-2):
			# tri = [tokensPropres[n], tokensPropres[n+1], tokensPropres[n+2]]
			tri = ["{} {} {}".format(tokensPropres[n], tokensPropres[n+1], tokensPropres[n+2])]
			print(tri)
			ying = open(fichierOUTtrigram, "a")
			yang = csv.writer(ying)
			yang.writerow(tri)

		print("*"*40)
		print(nb)


#Spacey : autre outil nltk

		# 					n+=1
		# 					if token != tokens[n].lower():
		# 						if token not in stop_words or tokens[n] not in stop_words:
		# 							bigram = [token, tokens[n]]

		# 							print(bigram)
	# 							liste.append(bigram)

								
								

# 							# print(token)

									# unigrams = ngrams(token,1)
									# bigrams = ngrams(token,2)
									# trigrams = ngrams(token,3)
									# fourgrams = ngrams(token,4)
									# fivegrams = ngrams(token,5)

									# print(list(trigrams))

									# allgrams = 


								

								

								# def find_bigrams(tokens):
								# 	bigram_list=[]
								# 	for i in range(len(token)-1):
								# 		bigram_list.append((token[i], token[i+1]))
								# 		return bigram_list
								


								# def find_bigrams(token):

									# bigram_list = []
									# for i in range(len(token)-1):
	    				# 					bigram_list.append((token[i], token[i+1]))
									# return bigram_list
								# ying = open(fich, "a")
								# yang = csv.writer(ying)
								# yang.writerow(token)





								# ### Pour compter mots lemmatisés

				# 				if rep == "0":
				# 					letype = "mots"
				# 					for token in tokens:
				# 						token = token.lower()
										
				# 						if token.isalpha():
				# 							lemme = tag.tag_text(mot)
				# 							lemme = lemme[0].split("\t")
				# 							m += 1
				# 							print(token,lemme[2],t,nb,m)
				# 							liste.append(lemme[2])

				# # ### Pour compter 2-grams

				# 				elif rep == "1":
				# 					letype = "bigrams"
				# 					i = 0
				# 					for mot in mots[:-1]:
				# 						mot = mot.lower()
				# 						if mot.isalpha():
				# 							if len(mot) > 1:
				# 								i += 1
				# 								if mot != mots[i].lower():
				# 									if mot not in rien or mots[i].lower() not in rien:
				# 										if "." not in mot and "," not in mot and "-" not in mot and "’" not in mot and "!" not in mot and ":" not in mot and "." not in mots[i] and "," not in mots[i] and "-" not in mots[i] and "’" not in mots[i] and "!" not in mots[i] and ":" not in mots[i]:
				# 											bigram = "{} {}".format(mot,mots[i])
				# 											print(nb,bigram)
				# 											liste.append(bigram)

				# # ### Pour compter 3-grams

				# 				elif rep == "2":
				# 					letype = "trigrammes"
				# 					i = 0
				# 					for mot in mots[:-2]:
				# 						mot = mot.lower()
				# 						if mot.isalpha():
				# 							if len(mot) > 1:
				# 								i += 1
				# 								if mot != mots[i].lower() and mots[i].lower() != mots[i+1].lower() and mot != mots[i+1].lower():
				# 									if (mot not in rien or mots[i].lower() not in rien) and (mots[i].lower() not in rien or mots[i+1].lower() not in rien):
				# 										trigram = "{} {} {}".format(mot,mots[i].lower(),mots[i+1].lower())
				# 										print(nb,trigram)
				# 										liste.append(trigram)

				# # 				else:
				# # 					print("Mauvaise réponse")

				# # print("$"*40)

				# # distFreq = nltk.FreqDist(liste)
				# # for m, frequence in distFreq.most_common(200):
				# # 	print('{} ->\t {}'.format(m, frequence))

				# ### Pour compter mots pondérés

				# 				if rep == "0":
				# 					fichierOUT = "twitter-mots-medias.csv"
				# 					for mot in mots:
				# 						mot = mot.lower()
				# 						if mot not in rien:
				# 							if mot.isalpha():
				# 								lemme = tag.tag_text(mot)
				# 								lemme = lemme[0].split("\t")
				# 								if mot != "http" or mot != "https":
				# 									m += 1
				# 									print(mot,lemme[2],engagement,m,t,nb)
				# 									ajout = [lemme[2],engagement]

				# 									ying = open(fichierOUT, "a")
				# 									yang = csv.writer(ying)
				# 									yang.writerow(ajout)

				# ### Pour compter bigrames pondérés

				# 				elif rep == "1":
				# 					fichierOUT = "twitter-bigrams-medias.csv"
				# 					i = 0
				# 					for mot in mots[:-1]:
				# 						mot = mot.lower()
				# 						if mot.isalpha():
				# 							if len(mot) > 1:
				# 								i += 1
				# 								if mot != mots[i].lower():
				# 									if mot not in rien or mots[i].lower() not in rien:
				# 										if "." not in mot and "," not in mot and "-" not in mot and "’" not in mot and "!" not in mot and ":" not in mot and "." not in mots[i] and "," not in mots[i] and "-" not in mots[i] and "’" not in mots[i] and "!" not in mots[i] and ":" not in mots[i]:
				# 											bigram = "{} {}".format(mot,mots[i])
				# 											# print(nb,bigram)
				# 											ajout = [bigram, engagement]
				# 											# liste.append(bigram)
				# 											print(ajout,nb)

				# 											ying = open(fichierOUT, "a")
				# 											yang = csv.writer(ying)
				# 											yang.writerow(ajout)

				# ### Pour compter trigrames pondérés

				# 				elif rep == "2":
				# 					fichierOUT = "twitter-trigrams-medias.csv"
				# 					i = 0
				# 					for mot in mots[:-2]:
				# 						mot = mot.lower()
				# 						if mot.isalpha():
				# 							if len(mot) > 1:
				# 								i += 1
				# 								if mot != mots[i].lower() and mots[i].lower() != mots[i+1].lower() and mot != mots[i+1].lower():
				# 									if (mot not in rien or mots[i].lower() not in rien) and (mots[i].lower() not in rien or mots[i+1].lower() not in rien):
				# 										trigram = "{} {} {}".format(mot,mots[i].lower(),mots[i+1].lower())
				# 										ajout = [trigram, engagement]
				# 										# liste.append(bigram)
				# 										print(ajout,nb)

				# 										ying = open(fichierOUT, "a")
				# 										yang = csv.writer(ying)
				# 										yang.writerow(ajout)

				# 				else:
				# 					print("Mauvaise réponse")
								

