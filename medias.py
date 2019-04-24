#coding: utf-8

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

#stop_words = set(stopwords.words('french')) 

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
aprs
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
concernant
couic
crac
d
da
dans
de
deja
delà
depuis
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
même
mêmes
n
na
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
relative
relativement
rend
rendre
restant
reste
restent
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
stop
strictement
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
vraiment
sest
aprs
grand
tait
"""

stop_words = (list(words.split('\n')))
fichiers = ["twitter_medias.csv", "twitter_journalistes.csv"]
obj = {}
messageList = []
mots = {}
hQ = []
hF = []
allText = []

quebecMedia = ["@tvanouvelles","@JdeMontreal","@LP_LaPresse","@RadioCanadaInfo","@JdeQuebec","@vicequebec", "@infomantv","@salutbonjour","@CBCMontreal","@TVASports","@RDSca","@icimontreal","@meteomedia","@CTVMontreal", "@Global_Montreal","@telequebec","@LaTribune","@_URBANIA","@HuffPostQuebec","@LeDevoir","@mtlgazette","@iciquebec", "@cyblesoleil","@Lactualite","@coupdepouce_mag","@la_lesaffaires","@journalmetro","@icircpremiere", "@RNCNouvellesAT"]
franceMedia = ["@Le_Figaro","@lemondefr","@canardenchaine","@Qofficiel", "@20hFrance2", "@TF1LeJT", "@LCI", "@BFMTV", "@CNEWS", "@libe", "@lequipe", "@le_Parisien", "@20Minutes", "@lobs" ,"@LesEchos","@TV5MONDE",  "@Le_Soir3", "@ARTEjournal", "@LaTribune", "@franceinfo", "@FRANCE24","@rtlinfo","@Europe1", "@RMCinfo", "@franceinter","@francebleu","@Charlie_Hebdo_", "@LEXPRESS", "@LePoint", "@VICEfr", "@radiofrance", "@mdiplo", "@Mediapart", "@RTLFrance", "@franceinfo", "@lejdd", "@RTenfrançais"]

AllMedia = list(set(quebecMedia + franceMedia))

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def Ar():
	for jo in quebecMedia:
		obj[jo] = {'list': [], 'vien': 'quebec'}
	for jour in franceMedia:
		obj[jour] = {'list': [], 'vien': 'france'}

def checkMedia(stri=''):
	
	k = stri.split(' ')
	c = []
	for i in k:
		if i.replace('@', '') == i:
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
			mentionner = False
			messageList.append(message)
		
		dedup = list(set(messageList))
		
		for message in dedup:
			for jour in AllMedia:
				if message.find(jour) != -1:
					mentionner = True
					obj[jour]['list'].append(deEmojify(message))
				
def WriteFile():
	global allText
	with open('media.csv', mode='w', encoding="utf8") as csv_file:
		fieldnames = ['Media', 'Tweet']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		
		for jour in obj:
			print(jour)
			for m in obj[jour]['list']:
				noTag = checkMedia(m)
				final = noTag.translate(str.maketrans('', '', string.punctuation))
				allWord = word_tokenize(final) 
				filter = [] 

				if jour != '' or jour != ' ':
					for word in allWord: 
						if word not in stop_words:
							filter.append(word.lower())
							if obj[jour]['vien'] == 'quebec':
								hQ.append(word.lower().replace(' ', ''))
							else:
								hF.append(word.lower().replace(' ', ''))
					
					for word in filter:
						if word in mots:
							mots[word]['num'] = mots[word]['num'] + 1
						else:
							mots[word] = {'num': 1}
					
					if jour not in stop_words:
						allText.append(final + ' ')
						writer.writerow({'Media': jour, 'Tweet': final})

def WriteWordFile():
	with open('mediaMotQuebec.csv', mode='w', encoding="utf8") as csv_file:
		fieldnames = ['Mot', 'Nombre de fois']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()

		l = collections.Counter()
		l.update(hQ)

		print('Most common:')
		o = l.most_common(len(hQ))
		for letter, count in o:
			if letter not in stop_words:
				if count <= 100:
					return
				print('%s: %7d' % (letter, count))
				writer.writerow({'Mot': letter, 'Nombre de fois': count})

				
def WriteWordFile2():
	with open('mediaMotFrance.csv', mode='w', encoding="utf8") as csv_file:
		fieldnames = ['Mot', 'Nombre de fois']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()

		l = collections.Counter()
		l.update(hF)

		print('Most common:')
		o = l.most_common(len(hF))
		for letter, count in o:
			if letter not in stop_words:
				if count <= 100:
					return
				print('%s: %7d' % (letter, count))
				writer.writerow({'Mot': letter, 'Nombre de fois': count})

Ar()
Check()
WriteFile()
WriteWordFile()
WriteWordFile2()