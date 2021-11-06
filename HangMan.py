print("This is hangman game")
# Problem Set 2, hangman.py
# Name: Chernenko Kolya
# Collaborators: 1 (just me)
# Time spent: 05.11.21 - 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from ast import Num
import random
import string
from collections import Counter

WORDLIST_FILENAME = "/home/kolya/Desktop/Studying/Основы программирования/DMKR/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  '''
    secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
  '''

  flag = False
  letters_secret_word = list(secret_word)
  counter = 0
  for i in letters_guessed:
    if i in letters_secret_word:
      counter += letters_secret_word.count(i)

  if counter == len(letters_secret_word):
    flag = True
  else:
    flag = False

  return flag



def get_guessed_word(secret_word, letters_guessed):
  '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"
  str_result = ""

  for i in list(secret_word):
    if i in letters_guessed:
      str_result += i
    else:
      str_result += '_ '

  return str_result


  



def get_available_letters(letters_guessed):
  '''
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string (of letters), comprised of letters that represents which letters have not
  yet been guessed.
  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"
  
  str_result = ""
  for i in string.ascii_lowercase:
    if i in letters_guessed:
      pass
    else:
      str_result += i

  return str_result
    
    

def hangman(secret_word):
  '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"

  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is", len(secret_word), "letters long.")
  print("You have 3 warnings left.")
  print("----------------")
  win = False
  game = True
  number_of_guesses = 6
  number_of_warnings = 3
  arr_char_guess = []
  while game == True:
    gueesed = False
    print("You have", number_of_guesses  , "guesses left.")
    print("Available letters: ", get_available_letters(arr_char_guess))
    input_char = input("Please guess a letter: ")
    input_char = input_char.lower()
    word = get_guessed_word(secret_word, arr_char_guess)

    if input_char.isalpha() == False:
      number_of_warnings -= 1
      if number_of_warnings >= 0:
          print("Oops! That is not a valid letter. You now have", number_of_warnings,"warnings left:", word)
      else:
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", word)
      if number_of_warnings < 0:
        number_of_guesses -= 1
    else:
      if input_char in arr_char_guess:
        number_of_warnings -= 1
        if number_of_warnings >= 0:
          print("Oops! You've already guessed that letter. You now have", number_of_warnings,"warnings left:", word)
        else:
          print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", word)
        if number_of_warnings < 0:
          number_of_guesses -= 1
      else:
        arr_char_guess.append(input_char)
        word = get_guessed_word(secret_word, arr_char_guess)
        if input_char in list(secret_word):
          print("Good guess: ", word)
        else:
          golos = ["a", "e", "i", "o", "u"]
          print("Oops! That letter is not in my word:", word)
          if input_char in golos:
            number_of_guesses -= 2
          else:
            number_of_guesses -= 1

        if is_word_guessed(secret_word, arr_char_guess):
          gueesed = True
          win = True

    if number_of_guesses <= 0 or win == True:
      game = False
    print("----------------")

  if win == True:
    print("Congratulations, you won!")
    print("Your total score for this game is: ", (number_of_guesses*len(Counter(secret_word))))
  else:
    print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
  '''
  my_word = str(my_word)
  flag = False

  length = 0
  txt = ''
  for i in my_word:
    if i != " ":
      length += 1
      txt += i

      arr = []
            
    if length != len(other_word):
      flag = False
    else:
      j = 0
      flag = True
      for i in other_word:
        if txt[j] != "_":
          if i != txt[j]:
            flag = False
            break
        else:
            if i in list(txt):
              flag = False
        j += 1

  return flag


def show_possible_matches(my_word):
  '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"

  res = ""

  flag = False
  for i in wordlist:
    val = match_with_gaps(my_word, i)
    if val == True:
      res += i
      res += " "
      flag = True

  if flag == False:
    res = "No matches found!"

  return res



def hangman_with_hints(secret_word):
  '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
  '''

  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is", len(secret_word), "letters long.")
  print("You have 3 warnings left.")
  print("----------------")
  win = False
  game = True
  number_of_guesses = 6
  number_of_warnings = 3
  arr_char_guess = []
  while game == True:
    gueesed = False
    print("You have", number_of_guesses  , "guesses left.")
    print("Available letters: ", get_available_letters(arr_char_guess))
    input_char = input("Please guess a letter: ")
    input_char = input_char.lower()
    word = get_guessed_word(secret_word, arr_char_guess)

    if input_char == "*":
      print("word: ", word)
      matches = show_possible_matches(word)
      print("Possible word matches are: ", matches)
    else:
      if input_char.isalpha() == False:
        number_of_warnings -= 1
        if number_of_warnings >= 0:
          print("Oops! That is not a valid letter. You now have", number_of_warnings,"warnings left:", word)
        else:
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", word)
        if number_of_warnings < 0:
          number_of_guesses -= 1
      else:
        if input_char in arr_char_guess:
          number_of_warnings -= 1
          if number_of_warnings >= 0:
            print("Oops! You've already guessed that letter. You now have", number_of_warnings,"warnings left:", word)
          else:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", word)
          if number_of_warnings < 0:
            number_of_guesses -= 1
        else:
          arr_char_guess.append(input_char)
          word = get_guessed_word(secret_word, arr_char_guess)
          if input_char in list(secret_word):
            print("Good guess: ", word)
          else:
            golos = ["a", "e", "i", "o", "u"]
            print("Oops! That letter is not in my word:", word)
            if input_char in golos:
              number_of_guesses -= 2
            else:
              number_of_guesses -= 1

        if is_word_guessed(secret_word, arr_char_guess):
          gueesed = True
          win = True
          
    if number_of_guesses <= 0 or win == True:
      game = False
    print("----------------")

  if win == True:
    print("Congratulations, you won!")
    print("Your total score for this game is: ", (number_of_guesses*len(Counter(secret_word))))
  else:
    print("Sorry, you ran out of guesses. The word was", secret_word)


    


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist) 
    #hangman("gypot")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints("apple") #secret_word