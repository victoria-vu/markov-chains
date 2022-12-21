"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    file = open(file_path).read().split() # Can add .read() and .split() together 
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
    
    chains = {}

    for i in range(len(text_string) - 2): 
        key = (text_string[i], text_string[i + 1]) 
        if key in chains: # Appending the value (word) to an existing key (bigram)
            chains[key].append(text_string[i+2])
        else: # Creating a new key if it does not exist in dictionary
            chains[key] = [text_string[i+2]] # Bigram is added to dictionary, the value is the word following the bigram
        # Had an IndexError because - 2 had to match +2 so that it didn't loop farther than the list
    
    print(chains)
    return chains

    


def make_text(chains):
    """Return text from chains."""

    words = []

    # Get a list of all of the keys in the dictionary
    key_list = chains.keys() 
    key_list = list(key_list)

    # Create a starting link (first three words) with a random key and random word from a list of words that follow it
    starting_link = choice(key_list)
    for item in starting_link:
        words.append(item)
    words.append(choice(chains[starting_link]))

    # Make a new key out of the second word in the first key and the random word you pulled out from a list of words that follow it
    # Keep on creating sentences until it ends with "Sam I am?"
    while True:
        new_link = (words[-2], words[-1])
        if new_link in key_list:
            words.append(choice(chains[new_link]))
        else:
            break

    print(words)
    return ' '.join(words)

# input_path = 'green-eggs.txt'
input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
