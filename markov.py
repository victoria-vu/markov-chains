"""Generate Markov text from text files."""

from random import choice
# choice()

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # open the file using "file_path"
    # return string as text using open("filename").read()
    
    file = open(file_path).read().split() #can add .read and .split together -
    #this read the entire file per item
    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    
    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
        #nothing follows juanita
    """
    
    #can loop over list 2 words at a time by index instead of item with range
        # for i in range (len(text) - 1): 
            # print text [i], text[i + 1] 
        #create tuple of keys (word1, word2) using the for loop
    #create list of values that follow those two words (word1, word2)
    #chain = tuple(key) and list(values)
        # exclude the last bigram as key in chains dictionary
    # .keys ? sorted(_.keys())?
    # 
    #return dict of chains
    #
    chains = {}

    for i in range(len(text_string) - 2): #gets rid of last items
        green_eggs = (text_string[i], text_string[i + 1]) #made into tuple - set to this variable 
        if green_eggs in chains: # Appending the value to an existing key 
            chains[green_eggs].append(text_string[i+2])
        else: # Creating a new key 
            chains[green_eggs] = [text_string[i+2]] #tuple became key (green_eggs), value set to word after tuple
        #dict[key] = [string[value]] means key and value
        #had an error because - 2 had to match +2 so that it didnt loop farther than the list
    
    print(chains)
    return chains

    


def make_text(chains):
    """Return text from chains."""

    words = [] # container

    # create a link (link is a key from our dictionary and a random word from the list of words that follow it)
        # you can use random's choice function (choice()) to pick a random key from chains.keys()
        # current_key
    # put the words from that link in a container
        #chosen_word ?
    # make a new key out of the second word in the first key and the random word you pulled out from the list of words that followed it
        #new_key

    key_list = chains.keys() #took all keys out
    key_list = list(key_list) #made into a list

    #link = key + random word from list of words that follow 
    for chosen_word in words:
        words[chosen_word] = choice(key_list), # chosen_word is a random key from the key list
        words[chosen_random_word] = choice(chains[chosen_word]) # a random word from list of words that follow that key
        
    
    # word = [(Would, you, could)]
    # random_key = choice(key_list) 
    # random_key.add(choice(chains[random_key]))
     


    print(words)
    return ' '.join(words)

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)
# John#Peter#Vicky




input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
