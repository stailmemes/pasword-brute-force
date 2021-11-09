# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  innerlist = words
  outerlist = words
  return words


# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses


def search(password):
  words = get_dictionary()
  guesses = 0
  for outerlist in words:
    for innerlist in words: 
      guesses += 1
      if (outerlist+innerlist == password):
        print("found")
        return True, guesses
  return False,guesses 