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

WORDS = ["BALE", "RONALDO", "MESSI", "HESKEY", "BENDTNER", "BENZEMA", "BECKHAM", "SOLSKJAER",
"GERRARD", "LAMPARD", "AGUERO", "ZIDANE", "RONALDO", "NEYMAR", "ROONEY", 
"CHICHARITO", "SALAH", 
"MARADONA", "INIESTA", "HENRY", "CANTONA", "DROGBA", "LINEKER", "SILVA", 
"KOMPANY", "MARCELO", 
"VIDIC", "ERIKSON", "TERRY"]

guesses = 0
MAX_WRONG = 7
print("Welcome to Worddrop!")

randomWord = random.choice(WORDS)
current_word = randomWord = "_" * len(randomWord)

print(current_word)