import random

HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |

=========''']

WORDS = ["BALE", "RONALDO", "MESSI", "HESKEY", "BENDTNER", "BENZEMA", "BECKHAM", "SOLSKJAER", "GERRARD", "LAMPARD", "AGUERO", "ZIDANE", "RONALDO", "NEYMAR", "ROONEY", "CHICHARITO", "SALAH", "MARADONA", "INIESTA", "HENRY", "CANTONA", "DROGBA", "LINEKER", "SILVA", "KOMPANY", "MARCELO", "VIDIC", "ERIKSON", "TERRY"]

print("Welcome to Worddrop!\n")

randomWord = random.choice(WORDS)

print(randomWord)