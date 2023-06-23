from testExample import *
class SubtaskData:
    def __init__(self):
        self.examples = [TestExample()] #array objektov testExample testnih primerov
    
    def addExample(self, testExample):
        self.examples.append(testExample)

    def updateExample(self, id, width, height):
        if id > len(self.examples):
            self.addExample(TestExample(matrixWidth = width, matrixHeight = height))
        else:
            self.examples[id-1].matrix.resizeMatrix(width, height)

    def represent(self):
        return {"easy": [example.represent() for example in self.examples]}
    
    def removeExample(self, id):
        if(len(self.examples) > 1):
            self.examples = self.examples[:id] + self.examples[id+1:]

    def removeItemType(self, itemName, itemNum):
        for example in self.examples:
            example.removeAllFromMatrix(itemNum, itemName)
    
    def updateExamplesHtmlString(self):
        html = ""
        for i in range(len(self.examples)):
            html += "<option>" + str(i+1) + "</option> <br>"
        return html
