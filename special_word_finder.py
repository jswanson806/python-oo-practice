from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """subclass of WordFinder that will ignore blank lines and comments """
    def __init__(self, path, words, count):
        super().__int__(path, words, count)
    
    def word_list(self, path):
        """reads words from list and """
        input_file = open(f"{path}", "r")

        stripped = []

        # iterate over file
        for line in input_file:
            # strip leading and trailing white space
            line = line.strip()
            # check if line is blank or line begins with '#', if so, skip line
            if not line or line.startswith("#"):
                continue
            # append the line to stripped[] and remove trailing "\n"
            stripped.append(line)

        # close the open file
        input_file.close()

        # return new local list of words
        return stripped
