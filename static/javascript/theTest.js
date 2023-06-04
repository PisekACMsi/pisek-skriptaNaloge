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
		//
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
          ovira: {
               num: 9,
               img: "banana.png",
               zOrder: 9,
               category: {
                    "coin": true
               },
               value: 0
          },
          robot0: {
               num: 4,
               img: "cebela.png",
               zOrder: 4,
               category: {
                    "robot": true
               },
               value: 0,
               nbStates: 9
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[1, 9, 9, 9, 1], 
 [1, 7, 7, 7, 1], 
 [1, 5, 1, 3, 1], 
 [1, 5, 1, 1, 3], 
 [1, 1, 1, 1, 1]],
               initItems: [
                    {
                         row: 0,
                         col: 0,
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