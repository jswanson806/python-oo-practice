
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("words.txt")
        Total words read: 235886

    >>> wf.random()
        'cat'

    >>> wf.random()
        'apprehension'

    """

    def __init__(self, path):
        self.path = path
        self.words = self.word_list(path)
        self.count = self.words_read(self.words)
        

    def word_list(self, path):
        """returns list of words from file path that is read"""

        # save the input file to read to variable
        input_file = open(f"{path}", "r")

        # iterate over file, place each word in local list, strip the \n from each new line
        stripped = [i.replace('\n', '') for i in input_file]

        # close the open file
        input_file.close()

        # return new local list of words
        return stripped

    def words_read(self, words):
        """print a message indicating total words read from source path"""

        #when run, print message with number of words read
        print(f"Total words read: {len(words)}")

        # return length of list of words for potential use
        return len(words)

    def random(self):
        """return a random word from the local list of words"""

        return choice(self.words)


        
