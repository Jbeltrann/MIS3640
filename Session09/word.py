fin = open("Session09/words.txt")
# line = repr(fin.readline())

# print(line)
# line = fin.readline()
# print(line)
# counter = 0


# def read_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
#     for line in fin:
#       word = line.strip()
#       if len(word) > 20:
#           print(word)


# read_long_words()


# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter “e” in it.
#     """
#     pass
#     for letter in word:
#         if letter == 'e':
#             return False
#         return True

# print(has_no_e('Babson'))
# print(has_no_e('College'))


# def avoids(word, forbidden):
#     """
#     takes a word and a string of forbidden letters, and that returns True
#     if the word doesn’t use any of the forbidden letters.
#     """
#     for char in word:
#         if char in forbidden:
#           return False
#     return True
    

# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))


# def uses_only(word, available):
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
#     for letter in word:
#         if letter not in available:
#             return False
#     return True

# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))



def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True

# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
def find_words_using_all_vowels():
    fin = open('Session09/words.txt')
    counter = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            print(word)
            counter += 1
    return counter
# print(find_words_using_all_vowels())

# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
index = 0
    for index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

def find_abecedarian_words():
    counter = 0
    index = 0
    if word in is_abecedarian:
        print(word)
        counter += 1
    return counter 

