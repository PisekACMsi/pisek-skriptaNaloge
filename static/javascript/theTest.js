function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {}
     },
     hideControls: {
          restart: false,
          saveOrLoad: false,
          loadBestAnswer: false,
          speedSlider: false,
          backToFirst: false,
          nextStep: false,
          goToEnd: false
     },
     zoom: {
          controls: true,
          scale: 1
     },
     hasGravity: false,
     introMaxHeight: "33%",
     maxListSize: 100,
     scrollbars: true,
     actionDelay: 400,
     blocklyColourTheme: "bwinf",
     maxInstructions: 10,
     ignoreInvalidMoves: false,
     border: 0.02,
     backgroundColour: "white",
     backgroundTile: "",
     borderColour: "black",
     showLabels: true,
     cellSide: 60,
     numberOfRobots: 1,
     startingExample: {
          blockly: ""
     },
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: [
                    "moveSimple",
                    "forward",
                    "forwardSimple"
               ]
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [
                    "logic",
                    "loops",
                    "math"
               ],
               singleBlocks: [],
               excludedBlocks: []
          }
     },
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		//,
		//
	])
},
     itemTypes: {
          obstacle0: {
               num: 3,
               category: [
                    {
                         'obstacle': true
                    }
               ],
               img: [
                    "objects/banana.png"
               ],
               zOrder: 5
          },
          number0: {
               num: 4,
               category: [
                    {
                         'number': true
                    }
               ],
               zOrder: 4,
               value: "0"
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1]],
               initItems: []
          }
     ]
};
initBlocklySubTask(subTask); 
}