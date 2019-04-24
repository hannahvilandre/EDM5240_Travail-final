import csv, codecs
import numpy as np 
import pandas as pan 
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import collections

nltk.download('stopwords')

words = """
a
abord
absolument
afin
ah
ai
aie
aient
aies
ailleurs
ainsi
ait
allaient
allo
allons
allô
alors
anterieur
anterieure
anterieures
apres
après
as
assez
attendu
au
aucun
aucune
aucuns
aujourd
aujourd'hui
aupres
auquel
aura
aurai
auraient
aurais
aurait
auras
aurez
auriez
aurions
aurons
auront
aussi
autre
autrefois
autrement
autres
autrui
aux
auxquelles
auxquels
avaient
avais
avait
avant
avec
avez
aviez
avions
avoir
avons
ayant
ayez
ayons
b
bah
bas
basee
bat
beau
beaucoup
bien
bigre
bon
boum
bravo
brrr
c
car
ce
ceci
cela
celle
celle-ci
celle-là
celles
celles-ci
celles-là
celui
celui-ci
celui-là
celà
cent
cependant
certain
certaine
certaines
certains
certes
ces
cet
cette
ceux
ceux-ci
ceux-là
chacun
chacune
chaque
cher
chers
chez
chiche
chut
chère
chères
ci
cinq
cinquantaine
cinquante
cinquantième
cinquième
clac
clic
combien
comme
comment
comparable
comparables
compris
concernant
contre
couic
crac
d
da
dans
de
debout
dedans
dehors
deja
delà
depuis
dernier
derniere
derriere
derrière
des
desormais
desquelles
desquels
dessous
dessus
deux
deuxième
deuxièmement
devant
devers
devra
devrait
different
differentes
differents
différent
différente
différentes
différents
dire
directe
directement
dit
dite
dits
divers
diverse
diverses
dix
dix-huit
dix-neuf
dix-sept
dixième
doit
doivent
donc
dont
dos
douze
douzième
dring
droite
du
duquel
durant
dès
début
désormais
e
effet
egale
egalement
egales
eh
elle
elle-même
elles
elles-mêmes
en
encore
enfin
entre
envers
environ
es
essai
est
et
etant
etc
etre
eu
eue
eues
euh
eurent
eus
eusse
eussent
eusses
eussiez
eussions
eut
eux
eux-mêmes
exactement
excepté
extenso
exterieur
eûmes
eût
eûtes
f
fais
faisaient
faisant
fait
faites
façon
feront
fi
flac
floc
fois
font
force
furent
fus
fusse
fussent
fusses
fussiez
fussions
fut
fûmes
fût
fûtes
g
gens
h
ha
haut
hein
hem
hep
hi
ho
holà
hop
hormis
hors
hou
houp
hue
hui
huit
huitième
hum
hurrah
hé
hélas
i
ici
il
ils
importe
j
je
jusqu
jusque
juste
k
l
la
laisser
laquelle
las
le
lequel
les
lesquelles
lesquels
leur
leurs
longtemps
lors
lorsque
lui
lui-meme
lui-même
là
lès
m
ma
maint
maintenant
mais
malgre
malgré
maximale
me
meme
memes
merci
mes
mien
mienne
miennes
miens
mille
mince
mine
minimale
moi
moi-meme
moi-même
moindres
moins
mon
mot
moyennant
multiple
multiples
même
mêmes
n
na
naturel
naturelle
naturelles
ne
neanmoins
necessaire
necessairement
neuf
neuvième
ni
nombreuses
nombreux
nommés
non
nos
notamment
notre
nous
nous-mêmes
nouveau
nouveaux
nul
néanmoins
nôtre
nôtres
o
oh
ohé
ollé
olé
on
ont
onze
onzième
ore
ou
ouf
ouias
oust
ouste
outre
ouvert
ouverte
ouverts
o|
où
p
paf
pan
par
parce
parfois
parle
parlent
parler
parmi
parole
parseme
partant
particulier
particulière
particulièrement
pas
passé
pendant
pense
permet
personne
personnes
peu
peut
peuvent
peux
pff
pfft
pfut
pif
pire
pièce
plein
plouf
plupart
plus
plusieurs
plutôt
possessif
possessifs
possible
possibles
pouah
pour
pourquoi
pourrais
pourrait
pouvait
prealable
precisement
premier
première
premièrement
pres
probable
probante
procedant
proche
près
psitt
pu
puis
puisque
pur
pure
q
qu
quand
quant
quant-à-soi
quanta
quarante
quatorze
quatre
quatre-vingt
quatrième
quatrièmement
que
quel
quelconque
quelle
quelles
quelqu'un
quelque
quelques
quels
qui
quiconque
quinze
quoi
quoique
r
rare
rarement
rares
relative
relativement
remarquable
rend
rendre
restant
reste
restent
restrictif
retour
revoici
revoilà
rien
s
sa
sacrebleu
sait
sans
sapristi
sauf
se
sein
seize
selon
semblable
semblaient
semble
semblent
sent
sept
septième
sera
serai
seraient
serais
serait
seras
serez
seriez
serions
serons
seront
ses
seul
seule
seulement
si
sien
sienne
siennes
siens
sinon
six
sixième
soi
soi-même
soient
sois
soit
soixante
sommes
son
sont
sous
souvent
soyez
soyons
specifique
specifiques
speculatif
stop
strictement
subtiles
suffisant
suffisante
suffit
suis
suit
suivant
suivante
suivantes
suivants
suivre
sujet
superpose
sur
surtout
t
ta
tac
tandis
tant
tardive
te
tel
telle
tellement
telles
tels
tenant
tend
tenir
tente
tes
tic
tien
tienne
tiennes
tiens
toc
toi
toi-même
ton
touchant
toujours
tous
tout
toute
toutefois
toutes
treize
trente
tres
trois
troisième
troisièmement
trop
très
tsoin
tsouin
tu
té
u
un
une
unes
uniformement
unique
uniques
uns
v
va
vais
valeur
vas
vers
via
vif
vifs
vingt
vivat
vive
vives
vlan
voici
voie
voient
voilà
vont
vos
votre
vous
vous-mêmes
vu
vé
vôtre
vôtres
w
x
y
z
zut
à
â
ça
ès
étaient
étais
était
étant
état
étiez
étions
été
étée
étées
étés
êtes
être
ô
cest
'
«
»
”
j
l
ctait
c
’
nest
quil
faire
nont
estce
quon
quils
dtre
quelles
quelle
dune
"""

stop_words = (list(words.split('\n')))
fichiers = ["Bonne_version_hashtags2.csv", "hashtags_.csv"]
obj = {}
messageList = []
mots = {}
hQ = []
hF = []
allText = []

Apres = {}
Avant = {}

hashTag = ["#lesmediasvousmentent","#journalismedemerde","#mainstream", "#journaux", "#presse","#lapresse" "#journlaiste", "#presselibre", "#journalisme", "#fakenews","#journalope","#merdias","#merdia"]

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def Ar():
	for jo in hashTag:
		obj[jo] = {'list': [], 'vien': 'quebec'}
		Avant[jo] = []
		Apres[jo] = []

def checkMedia(stri=''):
	
	k = stri.split(' ')
	c = []
	for i in k:
		if i.replace('@', '') == i and i.replace('#', '') == i:
			c.append(i)
	return ' '.join(c)

def Convert(message=''):

	noURL = re.sub(r"http\S+", "", message)
	
	split = noURL.split(' ')
	keyword = ''
	
	for word in split:
		if len(word) > 4:
			keyword += word + ' '
	
	return keyword


def Check():
	global h
	global messageList
	for fichier in fichiers:
		f = open(fichier, encoding="utf8")
		reader = csv.reader(f)
		last = {}
		for row in reader:
			message = Convert(row[2].replace('\n', ''))
			messageList.append(message)
		
		dedup = list(set(messageList))
		
		for message in dedup:
			for jour in hashTag:
				if message.find(jour) != -1:
					obj[jour]['list'].append(deEmojify(message))
				
def WriteFile():
	global allText
	with open('hashtags.csv', mode='w', encoding="utf8") as csv_file:
		fieldnames = ['Hashtag', 'Tweet']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		
		for jour in obj:
			print(jour)
			for m in obj[jour]['list']:

				final = m.translate(str.maketrans('', '', string.punctuation))
				allWord = word_tokenize(final) 
				filter = []

				if jour != '' or jour != ' ':
					case = 0
					match = 0
					tout = []
					haveTag = False
					for word in allWord:
						if word not in stop_words:
							filter.append(word.lower())
							tout.append(word)
							if jour.replace('#', '') == word:
								haveTag = True
								match = case
						case = case + 1
					
					if haveTag:
						finalLen = len(tout) - 1
						av = []
						ap = []
						
						if match - 2 < finalLen:
							av = [tout[match - 3], tout[match - 2], tout[match - 1]]
						elif match - 1 <= finalLen:
							av = [tout[match - 2], tout[match - 1]]
						elif match <= finalLen:
							av = [tout[match - 1]]
						
						if (match + 3) <= finalLen:
							ap = [tout[match + 1], tout[match + 2], tout[match + 3]]
						elif (match + 2) <= finalLen:
							ap = [tout[match + 1], tout[match + 2]]
						elif (match + 1) <= finalLen:
							ap = [tout[match + 1]]
						
						Avant[jour].append(av)
						Apres[jour].append(ap)
					
					if jour not in stop_words:
						allText.append(final + ' ')
						writer.writerow({'Hashtag': jour, 'Tweet': final})

def WriteWordFile():
	with open('hashtagsMot.csv', mode='w', encoding="utf8") as csv_file:
		fieldnames = ['Tag', 'Avant', 'Apres']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		for tag in Apres:
			t = Apres[tag]
			n = 0
			for ap in t:
				writer.writerow({'Tag': tag, 'Avant': ' '.join(Avant[tag][n]), 'Apres': ' '.join(ap)})
				n = n + 1
	
Ar()
Check()
WriteFile()
WriteWordFile()