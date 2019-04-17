#coding: utf-8

import csv
import json
import twitter
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import math
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
from cleftweet import CleeApi, CleeApisecret, Jeton, Jetonsecret


fichier = "freepress.csv"


t = twitter.Api(consumer_key=CleeApi,
	consumer_secret=CleeApisecret,
	access_token_key=Jeton,
	access_token_secret=Jetonsecret,
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



tweets = t.GetSearch(term = onCherche,count = 500,result_type = "recent",return_json = True, lang = "fr")

hashtags = ["#lesmediasvousmentent","#journalismedemerde","#mainstream", "#journaux", "#presse", "#lapresse", "#presselibre", "#journalisme"]

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

onCherche = input("dequéssé")   

for tweet in tweets["statuses"]:
		cuicui = []

		#cuicui.append(hashtag1)
		#cuicui.append(hashtag2)
		#cuicui.append(hashtag3)
		#cuicui.append(hashtag4)
		#cuicui.append(hashtag5)
		#cuicui.append(hashtag6)
		#cuicui.append(hashtag7)
		#cuicui.append(hashtag8)
		cuicui.append(hashtag9)

		cuicui.append(tweet["created_at"])

		cuicui.append(getText(tweet))
		cuicui.append(tweet["user"]["name"])
#
		cuicui.append(tweet["id"])
		cuicui.append(tweet["retweet_count"])
		cuicui.append(tweet["favorite_count"])
		cuicui.append(tweet["lang"])
#
		cuicui.append(tweet["user"]["location"])

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
	
	
###  fichier csv.
		cool = open(fichier,"a")
		pouetpouet = csv.writer(cool)
		pouetpouet.writerow(cuicui)
