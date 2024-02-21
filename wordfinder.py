from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, location):
        """Creates an instance of WordFinder given
        a file's location"""
        self.location = location
        self.word_list = self.get_words()

        self.print_words_read()

    def __repr__(self):
        return f"""WordFinder with the following location:
        {self.location}"""

    def get_words(self):
        """ Reads a file given in the intance's location,
        and returns a list with every single word in the file"""
        word_list = []

        with open(self.location, "r") as file:
            for line in file:
                word_list.append(line.rstrip())

        return word_list

    def print_words_read(self):
        """Prints the number of words read in the file"""
        print(f"{len(self.word_list)} words read")

    def random(self):
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder that omits blank lines and comment lines"""

    def __init__(self, location):
        super().__init__(location)
        self.remove_special_words()


    def remove_special_words(self):
        for word in self.word_list:
            if (word.startswith("#") or len(word) == 0):
                self.word_list.remove(word)
