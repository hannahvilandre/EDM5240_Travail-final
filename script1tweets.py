#coding: utf-8

### Pour notre exercice de moissonnage, j'ai décidé de rester sur l'API Twitter créée précédemment.

### Différents import à faire, notamment les différentes clés auxquelles nous avons accès en créant notre API.
import csv
import json
import twitter
import pandas as pd
from textblob import TextBlob
#from textblob_fr import PatternTagger, PatternAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import math
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
from twit import cleAPI, cleSecreteAPI, jeton, jetonSecret

### Création de notre fichier .csv 
fichier = "twitter_media_devoir_1.csv"

### Ce bout de script est ce qui nous permet ensuite de pouvoir faire notre recherche "tweets"**
t = twitter.Api(consumer_key=cleAPI,
	consumer_secret=cleSecreteAPI,
	access_token_key=jeton,
	access_token_secret=jetonSecret,
	tweet_mode="extended"
	)

def sentiment_score(sentence):
    fr_blob = TextBlob(sentence)
    try:
        #translate sentence to english
        sentence_eng = fr_blob.translate(to='eng')
    except:
        sentence_eng = sentence
    #compute the polarity score -1 = negative, 1 = positive (continuous values)
    snt = analyser.polarity_scores(sentence_eng)
    return snt["compound"]

def cleanScrap(searchterm):
    #Scrap tweets
    pd_tweets = weekScrap(searchterm)
    
    #Keep one copy of retweeted tweets
    pd_tweets = rmDuplicatedRT(pd_tweets)
    
    #compute the sentiment of tweets
    pd_tweets["sentiment"] = pd_tweets.apply(lambda row: sentiment_score(row["full_text"]),axis=1)
    
    pd_tweets["searchTerm"] = searchterm
    
    return pd_tweets

def fullScrap(searchterm_list):
    init = False
    
    for term in searchterm_list:
        if(not init):
            df_all_tweet = cleanScrap(term)
            print(len(df_all_tweet["full_text"].values))
            init=True
        else:
            df_all_tweet = pd.concat([df_all_tweet,cleanScrap(term)])
            print(len(df_all_tweet["full_text"].values))

    return df_all_tweet

def getText(tweet):       
	    # Try for extended text of original tweet, if RT'd (streamer)
    try: text = tweet['retweeted_status']['extended_tweet']['full_text']
    except: 
        # Try for extended text of an original tweet, if RT'd (REST API)
        try: text = tweet['retweeted_status']['full_text']
        except:
            # Try for extended text of an original tweet (streamer)
            try: text = tweet['extended_tweet']['full_text']
            except:
                # Try for extended text of an original tweet (REST API)
                try: text = tweet['full_text']
                except:
                    # Try for basic text of original tweet if RT'd 
                    try: text = tweet['retweeted_status']['text']
                    except:
                        # Try for basic text of an original tweet
                        try: text = tweet['text']
                        except: 
                            # Nothing left to check for
                            text = ''
    return text

### Ici, on met une variable qui va nous donner l'opportunité de rentrer dans terminal les mots-clés recherchés
# onCherche = input("qué!? ")

### ** Ici, notre variable tweets qui va aller chercher les infos nécessaires
quebecMedia = ["@tvanouvelles","@JdeMontreal","@LP_LaPresse","@RadioCanadaInfo","@JdeQuebec","@vicequebec",
"@infomantv","@salutbonjour","@CBCMontreal","@TVASports","@RDSca","@icimontreal","@meteomedia","@CTVMontreal",
"@Global_Montreal","@telequebec","@LaTribune","@_URBANIA","@HuffPostQuebec","@LeDevoir","@mtlgazette","@iciquebec",
"@cyblesoleil","@Lactualite","@coupdepouce_mag","@la_lesaffaires","@journalmetro","@icircpremiere", "@RNCNouvellesAT"]

franceMedia = ["@Le_Figaro","@lemondefr","@canardenchaine","@Qofficiel", "@20hFrance2", "@TF1LeJT", "@LCI", "@BFMTV", 
              "@CNEWS", "@libe", "@lequipe", "@le_Parisien", "@20Minutes", "@lobs" ,"@LesEchos","@TV5MONDE", 
              "@Le_Soir3", "@ARTEjournal", "@LaTribune", "@franceinfo", "@FRANCE24","@rtlinfo","@Europe1",
              "@RMCinfo", "@franceinter","@francebleu","@Charlie_Hebdo_", "@LEXPRESS", "@LePoint", "@VICEfr", "@radiofrance", 
              "@mdiplo", "@Mediapart", "@RTLFrance", "@franceinfo", "@lejdd", "@RTenfrançais"]

medias = quebecMedia + franceMedia

# print(medias)

# tweets = t.GetSearch(term = media,count = 500,result_type = "recent", lang = "fr", return_json = True)
for i in reversed(range(19,27)):


	for media in medias:
		tweets = t.GetSearch(term = media,count = 100,result_type = "recent", lang = "fr", since="2019-03-{}".format(i-1),until="2019-03-{}".format(i), return_json = True)

		# print(json.dumps(tweets, indent=2, sort_keys=True))
		# print("*"*60)





		# def saveToCSV(df,filePath, sep="|"):
		#     df[columns_to_keep].to_csv(filePath,sep="|", encoding='utf-8')

		### Ensuite, passons à notre fonction 'for in' afin de récupérer toutes nos infos nécessaires.
		for tweet in tweets["statuses"]:
				cuicui = []
				cuicui.append(media)





		### Ici, toutes les infos qu'on veut consigner dans notre csv
				cuicui.append(tweet["created_at"])
		### Texte des tweets organiques sans la fonction 'def getText' -> Cette fonction est celle qui ne me laisse qu'un extrait des retweets.
				# s.append(tweet["full_text"])
		### ce .append() me permet, en accord avec la fonction 'def getText' de récupérer mes tweets en full_text.
				cuicui.append(getText(tweet))
				cuicui.append(tweet["user"]["name"])
		### J'ai ajouté "id" sur tes conseils afin de pouvoir, lorsqu'on traiterait ces informations de pouvoir faire le tri sur des tweets qui seraient en double.
				cuicui.append(tweet["id"])
				cuicui.append(tweet["retweet_count"])
				cuicui.append(tweet["favorite_count"])
				cuicui.append(tweet["lang"])
		### Ici, juste en ajoutant "location", il y a key error. Il fallait donc que je rajoute la clé "user" afin de récupérer l'info
				cuicui.append(tweet["user"]["location"])

				sentiment = sentiment_score(getText(tweet))
				cuicui.append(sentiment)
				print(sentiment)

		### On print ce qu'on veut trouver.
				print("Date/Heure: ", tweet["created_at"])
				# print("Contenu: ", tweet["full_text"])
				print("tweet: ", getText(tweet))
				print("Pseudo: ", tweet["user"]["name"])
				print("IdUser: ", tweet["id"])
				print("Retweets: ", tweet["retweet_count"])
				print("P'tits coeurs: ", tweet["favorite_count"])
				print("Language: ", tweet["lang"])
				print("Location: ", tweet["user"]["location"])
				print("dexcription: ", tweet["user"]["description"])

				print("*"*80)


		## Fonction nécessaire afin de créer notre fichier csv.
				cool = open(fichier,"a")
				pouetpouet = csv.writer(cool)
				pouetpouet.writerow(cuicui)




