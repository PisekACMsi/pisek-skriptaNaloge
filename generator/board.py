class Board:
    def __init__(self, backgColor = "white", backgImage = "", lineColor = "black", lineWidth = 0.02, showLabels = True, gravity = False, maxInstructions=0, numberOfRobots=1, checkEndEveryTurn=False):
        self.backgColor = backgColor #string
        self.backgImage = backgImage #string path to image
        self.lineColor = lineColor #string
        self.lineWidth = lineWidth #float
        self.showLabels = showLabels #bool
        self.gravity = gravity #bool
        self.maxInstructions = maxInstructions
        self.numberOfRobots = numberOfRobots
        self.checkEndEveryTurn = checkEndEveryTurn
        
        self.introMaxHeight = "33%"
        self.maxListSize = 100
        self.scrollbars = True
        self.actionDelay = 400
        self.blocklyColourTheme = "bwinf"
        self.ignoreInvalidMoves = False
        self.cellSide = 60
        self.hideControls = {
          "restart": False,
          "saveOrLoad": False,
          "loadBestAnswer": False,
          "speedSlider": False,
          "backToFirst": False,
          "nextStep": False,
          "goToEnd": False
        }
        self.zoom = {
            "controls": True,
            "scale": 1
        }
        self.startingExample = {
          "blockly": ""
        }

    def updateStartingExample(self, example):
        self.startingExample["blockly"] = example
    
    def representSolo(self):
        return { "hasGravity":self.gravity, "introMaxHeight": self.introMaxHeight, "maxListSize":self.maxListSize,
                "scrollbars":self.scrollbars, "zoom":self.zoom, "actionDelay":self.actionDelay,
                "blocklyColourTheme": self.blocklyColourTheme,  "maxInstructions":self.maxInstructions,
                "ignoreInvalidMoves":self.ignoreInvalidMoves, "border":self.lineWidth,
                "backgroundColour":self.backgColor, "backgroundTile":self.backgImage, 
                "borderColour":self.lineColor, "showLabels":self.showLabels, 
                "cellSide":self.cellSide, "numberOfRobots":self.numberOfRobots, 
                  "startingExample":self.startingExample, "checkEndEveryTurn":self.checkEndEveryTurn}
    
    def representHideControls(self):
        return {"hideControls":self.hideControls}
    
    def representZoom(self):
        return {"zoom":self.zoom}
    
    def representStartingExample(self):
        return {"startingExample":self.startingExample}