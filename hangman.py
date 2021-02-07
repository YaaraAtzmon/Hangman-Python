
HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
                     \n"""
                     
MAX_TRIES = 6

old_letters_guessed = []

def hangman_art(): 
    """Print the opening screen.
    :return: none"""  
    print(HANGMAN_ASCII_ART, MAX_TRIES)  
 
HANGMAN_PHOTOS = {0: """
       x-------x
""", 
1: """
       x-------x
       |
       |
       |
       |
       |
""",
2: """
       x-------x
       |       |
       |       0
       |
       |
       |
 """,
3: """
       x-------x
       |       |
       |       0
       |       |
       |
       |
 """,
4: """
       x-------x
       |       |
       |       0
       |      /|\\
       |
       |
   """,
5: """
       x-------x
       |       |
       |       0
       |      /|\\
       |      /
       |
 """,
6: """
       x-------x
       |       |
       |       0
       |      /|\\
       |      / \\
       |
    """}    
 
def print_hangman(num_of_tries):
    """Return the hangman drawing considering number of tries.
    :param num_of_tries: number of tries value
    :type num_of_tries: int 
    :return: The hangman drawing
    :rtype: string"""    
    return HANGMAN_PHOTOS[num_of_tries]
    
def choose_word(file_path, index):
    """Open a file and choose a word.
    :param file_path: file path value
    :param index: index value
    :type file_path: string
    :type index: int 
    :return: A word from a file. 
    :rtype: int"""    
    words_input_file = open(file_path, "r")
    words = words_input_file.read()
    word = words.split()
    choose_word = word[index % len(word) - 1]
    return choose_word

def check_valid_input(letter_guessed, old_letters_guessed):
    """Check if the input is valid.
    :param letter_guessed: letter guessed value
    :param old_letters_guessed: list of old letters guessed value
    :type letter_guessed: string
    :type old_letters_guessed: list 
    :return: False or True
    :rtype: boolean"""    
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
       return False   
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Check if the letter guessed is valid. 
    If it is valid the letter guessed appends to the list of old letters gueseed.
    :param letter_guessed: letter guessed value
    :param old_letters_guessed: list of old letters guessed value
    :type letter_guessed: string
    :type old_letters_guessed: list 
    :return: False or True
    :rtype: boolean values"""    
    if not check_valid_input(letter_guessed, old_letters_guessed):
       print(" X\n")
       old_letters_guessed.sort()
       string = ' -> '.join(old_letters_guessed)
       print(string.lower())  
       return False
    elif check_valid_input(letter_guessed, old_letters_guessed):
       old_letters_guessed.append(letter_guessed)
       return True
       
def show_hidden_word(secret_word, old_letters_guessed):
    """Check if the letter guessed is in the secret word.
    If it is in the secret word, it appears at the right place and if not there is underline.  
    :param secret_word: secret word value
    :param old_letters_guessed: list of old letters guessed value
    :type secret_word: string
    :type old_letters_guessed: list 
    :return: The hidden word.
    :rtype: string"""    
    hidden_word = []
    for letter in secret_word:
        if letter in old_letters_guessed: 
           hidden_word.append(letter)
        else: 
           hidden_word.append("__")
    hidden_word = '  '.join(hidden_word)       
    return(hidden_word)  
    
def check_win(secret_word, old_letters_guessed):
    """Check if all the letters gueseed is in the secret word.  
    :param secret_word: secret word value
    :param old_letters_guessed: list of old letters guessed value
    :type secret_word: string
    :type old_letters_guessed: list 
    :return: False or True.
    :rtype: boolean"""    
    for letter in secret_word:
        if letter not in old_letters_guessed: 
           return False
    return True        
    
def hangman(secret_word): 
    """The process of the game.
    If the letter gueseed is not in the secret word the next drawing hangman appears. 
    At the end of the loop it prints "WIN" or "LOSE".     
    :param secret_word: secret word value
    :type secret_word: string
    :return: none""" 
    num_of_tries = 0
    while not check_win(secret_word, old_letters_guessed) and num_of_tries < 6:
        letter_guessed = input("Guess a letter: ") 
        letter_guessed = letter_guessed.lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                num_of_tries = num_of_tries + 1
                print(" :( ")
                print(print_hangman(num_of_tries))
            print(show_hidden_word(secret_word, old_letters_guessed))
    if check_win(secret_word, old_letters_guessed):
       print("WIN")   
    elif num_of_tries == 6:
       print("LOSE")
    
def main():
    hangman_art()
    file_path = input("enter file path: ")
    index = input("enter index: ")
    secret_word = choose_word(file_path, int(index))   
    print("Let's start!")
    print(print_hangman(0))
    print(len(secret_word) * " __ ")
    hangman(secret_word)
    
if __name__ == "__main__":
   main()


