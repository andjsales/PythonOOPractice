"""Word Finder: finds random words from a dictionary.

>>> wf = WordFinder("/Users/student/words.txt")
3 words read

>>> wf.random()
'cat'

>>> wf.random()
'cat'

>>> wf.random()
'porcupine'

>>> wf.random()
'dog'

"""

# Define a class called WordFinder.
class WordFinder:
    def __init__(self, wf):
        self.words = [] 
        with open(wf, 'r') as file:
            self.words = file.read().splitlines()
        print(f"{len(self.words)} words read")

    def random(self):
        import random
        return random.choice(self.words)


wf = WordFinder("/Users/andrewsales/Development/PythonOOPractice/words.txt")

print(wf.random())