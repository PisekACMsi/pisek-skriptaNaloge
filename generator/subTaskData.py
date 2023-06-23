from testExample import *
class SubtaskData:
    def __init__(self):
        self.examples = [TestExample()] #array objektov testExample testnih primerov
    
    def addExample(self, testExample):
        self.examples.append(testExample)

    def represent(self):
        return {"easy": [example.represent() for example in self.examples]}