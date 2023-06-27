import random

def vygeneruj_cislo():
  cislo=[-1,-1,-1,-1]
  cislo[0] = random.randint(1,9) 

  for i in range(1,4):  
      cislo[i] = random.randint(0,9)
      while cislo.count(cislo[i])-1 :
          cislo[i] = random.randint(0,9)
              
  return(cislo)   


def vloz_cislo():
  proslo_kontrolou=False

  while not(proslo_kontrolou):
      print("-"*50)
      str_cislo = input(">>> ")
      proslo_kontrolou=True

      if not(str_cislo.isdigit()) or str_cislo[0]=="0" or len(str_cislo) != 4:
          proslo_kontrolou=False
      else:
        for i in range(3):
          if str_cislo.count(str_cislo[i]) > 1:
            proslo_kontrolou=False
            break

      if  not(proslo_kontrolou):
        print("""Chyba - zadané číslo nesmí začínat 0 a musí obsahovat
přesně 4, navzájem různé číslice.""")
        print("Zadejte jej prosím ještě jednou")

  return str_cislo



def vyhodnot(vlozene_cislo, tajne_cislo):

  bulls=0
  cows=0

  for i in range(4):
      if int(vlozene_cislo[i]) == tajne_cislo[i]:
        bulls +=1
      else: 
        if tajne_cislo.count(int(vlozene_cislo[i])) :
          cows +=1

  return bulls,cows


##############################   zacatek programu ########################
author =(
'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ales Stransky
email: ales.stransky@seznam.cz
discord: Ales S#5138
''')


bulls_cows=[0,0]

tajne_cislo = vygeneruj_cislo() 
#print(tajne_cislo)
print("Hi there!")
print("-"*50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-"*50)
print("Enter a number:")

pokusu=0
while not(bulls_cows[0]==4):
    vlozene_cislo = vloz_cislo()
    pokusu +=1
    bulls_cows = vyhodnot(vlozene_cislo, tajne_cislo)

    if not(bulls_cows[0]==4): #dokud to neni kompletne uhadnute
        byci="bulls"
        if bulls_cows[0]==1:
           byci="bull"

        kravy="cows"
        if bulls_cows[1]==1:
           kravy="cow"
        print(f"{bulls_cows[0]} {byci}, {bulls_cows[1]} {kravy}")


print("Correct, you've guessed the right number")
print(f"in {pokusu} guesses!")
print("-"*50)

vysledek="not so good"
if pokusu<8:
   vysledek="amazing"
elif pokusu<18:
   vysledek="average"

print(f"That's {vysledek}")   