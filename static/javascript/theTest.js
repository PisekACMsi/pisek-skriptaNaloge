function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {
               categories: {
                    actions: "Gibanje"
               }
          }
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
     introMaxHeight: "33%",
     maxListSize: 100,
     scrollbars: true,
     zoom: {
          controls: true,
          scale: 1
     },
     actionDelay: 400,
     blocklyColourTheme: "bwinf",
     maxInstructions: 666,
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: [
                    "move"
               ]
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [],
               singleBlocks: [],
               excludedBlocks: []
          }
     },
     startingExample: {
          blockly: ""
     },
     checkEndEveryTurn: false,
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		(context, lastTurn) => { robotEndConditions.checkItemExistence(context, lastTurn, {category: "coin"}, {}, exist=false) },
		(context, lastTurn) => { robotEndConditions.checkItemCoincidence(context, lastTurn, {category: "coin"}, {category: "coin"}, [], {}, {}) }
	])
},
     ignoreInvalidMoves: false,
     border: 0.02,
     backgroundColour: "#000000",
     backgroundTile: ".png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {
          robot0: {
               num: 5,
               img: "gasilec.png",
               zOrder: 5,
               category: {
                    "robot": true
               },
               value: 0,
               nbStates: 1,
               row: 3,
               col: 2
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
               initItems: [
                    {
                         row: 3,
                         col: 2,
                         type: "robot0",
                         dir: 0,
                         value: 0
                    }
               ]
          }
     ]
};
initBlocklySubTask(subTask); 
}