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
     backgroundTile: "asfalt.png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {
          robot0: {
               img: "avto.png",
               zOrder: 10,
               category: {
                    "robot": true
               },
               value: 0,
               nbStates: 9
          },
          obstacle0: {
               num: 3,
               img: "banana.png",
               zOrder: 2,
               category: {
                    "obstacle": true
               },
               value: 0
          },
          number0: {
               zOrder: 2,
               category: {
                    "number": true
               },
               value: "0",
               num: 5
          },
          number2: {
               zOrder: 2,
               category: {
                    "number": true
               },
               value: "2",
               num: 6
          },
          color0: {
               zOrder: 2,
               value: 0,
               colour: "green",
               num: 6
          },
          color1: {
               zOrder: 2,
               value: 0,
               colour: "red",
               num: 7
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[2, 1, 1, 1, 1], 
 [1, 5, 3, 1, 1], 
 [1, 1, 2, 1, 1], 
 [1, 1, 1, 6, 7], 
 [1, 1, 3, 1, 3]],
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