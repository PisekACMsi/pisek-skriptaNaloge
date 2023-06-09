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
     maxInstructions: 0,
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: []
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
     backgroundColour: "white",
     backgroundTile: "",
     borderColour: "black",
     showLabels: true,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {
          robot0: {
               img: "cebela.png",
               zOrder: 10,
               category: {
                    "robot": true
               },
               value: 0,
               nbStates: 8
          },
          ovira: {
               num: 4,
               img: "hisa2.png",
               zOrder: 8,
               category: {
                    "transportable": true
               },
               value: 0,
               nbStates: 1
          },
          bb: {
               num: 5,
               img: "hisa2.png",
               zOrder: 9,
               category: {
                    "transportable": true
               },
               value: 0
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[5, 1, 1, 1, 1], 
 [1, 7, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1]],
               initItems: [
                    {
                         row: 1,
                         col: 1,
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