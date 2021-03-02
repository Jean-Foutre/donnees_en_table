#Partie B:
#1
"""
fichier = open("indicateurs.csv","r")
contenu = fichier.read()
fichier.close()
"""
#print(type(contenu))

#2

def B2(nom_du_fichier): #La fonction a été un peu modifiée pour fonctionner avec les questions suivantes
  f = open(nom_du_fichier); c = f.read()
  f.close(); l = []; ch = '' #Ces lignes sont une version abrégée de ce qui est inscrit en commentaire. A apprendre
  for i in range(len(c)):
    ch += c[i]
    if c[i] == '\n':
      l.append(ch)
      ch = ''
  return l
# print(B2("indicateurs.csv"))

#3 Ce sont des chaînes de caractères

def B3():
  a = B2("indicateurs.csv") #variable qui permet de stocker le résultat de la fonction. Une ligne sera donc désignée par l'instruction suivante: a[n]
  for i in range(len(a)):
    print(len(a[i]),type(a[i]))
  return #La fonction ne sert à rien: c'est juste pour éviter d'avoir à tout mettre en commentaire
#4
# print(a[0])
#5
# print(a[5459])
# Partie C:

#1
def split(texte, sep):
  l = []; c = ''
  for i in range(len(texte)):
    if texte[i] == sep:
      l.append(c)
      c = ''
    elif texte[i] != sep and texte[i] != '\n':#voir ligne48
      c += texte[i]
  l.append(c)#si on ne fait pas cette instruction, la dernière valeur de chaque ligne n'est pas prise en compte, car notre magnifique fonction de départ faisait en sorte que les lignes ne se terminent pas par une virgule
  return l
a = B2("indicateurs.csv")
# print(split(a[5459],','))

#2
def create_dataset(nom_du_fichier):
  l = []
  a = B2(nom_du_fichier) #Cela sert à faire de chaque ligne du fichier une liste à part entière
  for i in range(len(a)):
    l.append(split(a[i],','))
  return l
base = create_dataset("indicateurs.csv")
#print(base[9365])

#Partie D:

#1
def chercher(nom_du_fichier):
  for i in base: #On réutilise la fonction écrite plus haut, abrégée par la variable base. On a besoin de cette fonction, car si on utilise juste la fonction B2, les éléments de la listes sont les lignes sous forme de chaînes de caractères
    if i[0] == 'LYCEE BUFFON' and i[1] == '2018':
      return i[7]
# print(chercher("indicateurs.csv"))

#2a
def chercher2(nom_du_fichier):
  a = 0
  for i in base:
      a += 1
  return a
# print(chercher2("indicateurs.csv"))
#2b
def chercher3(nom_du_fichier):
  a = 0
  for i in base:
    if i[7] == '100' and i[1] == '2017' and i[4] == 'PU':
      a += 1
  return a
#print(chercher3("indicateurs.csv"))

#3
def chercher4(nom_du_fichier):
  a = 0
  for i in base:
    if i[5] == '100' and i[1] == '2016' and i[3] == 'PARIS':
      a += 1
  return a
#print(chercher4("indicateurs.csv"))

#4
def chercher5(nom_du_fichier):
  l = []
  for i in base:
    v = True
    for j in range(5,8):
      if i[j] != '100' and i[j] != '':
        v = False
    if v == True and i[1] == '2018' and i[3] == 'PARIS' and i[4] == 'PU':
      l.append(i[0])
  return l
#print(chercher5("indicateurs.csv"))

#ex5:
#a
def chercher6(nom_du_fichier):
  a = 0; b = 0
  for i in base:
    if i[1] == '2012' and i[6] != '' and i[9] != '':
      if int(i[6])-int(i[9]) > a:
        a = int(i[6])-int(i[9])
        b = i[0]
  return b, a
print(chercher6("indicateurs.csv"))
#b
def chercher7(nom_du_fichier):
  a = 0; b = 0
  for i in base:
    c = 0; d = 0
    for j in range(5,8):
      if i[1] == '2016' and i[j] != '' and i[j+3] != '': #Si on regarde le fichier, on constate que le taux attendu est trois cases plus loin que le taux brut
        c = int(i[j])-int(i[j+3]); d += c
        if d > a:
          a = d; b = i[0]
  print("plus value=",a)
  return b
print(chercher7("indicateurs.csv"))

